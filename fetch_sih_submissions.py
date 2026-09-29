import urllib.request
import json
import os

def main():
    url = "https://raw.githubusercontent.com/Zaidusyy/sih-2026-problem-statements/main/data/problem-statements.json"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    
    print(f"Fetching full SIH problem statements from {url}...")
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=30) as resp:
        raw_data = json.loads(resp.read().decode("utf-8"))
        
    print(f"Loaded {len(raw_data)} problem statements.")
    
    # Process and enrich each statement
    enriched_statements = []
    for item in raw_data:
        cap = int(item.get("cap", 500) or 500)
        submitted = int(item.get("submitted", 0) or 0)
        remaining = max(0, cap - submitted)
        fill_percentage = round((submitted / cap) * 100, 2) if cap > 0 else 0.0
        status = "FROZEN (Max 500 Reached)" if submitted >= cap else ("FILLING FAST (>80%)" if fill_percentage >= 80 else "OPEN")
        
        enriched = {
            "id": item.get("psNumber", ""),
            "title": item.get("title", ""),
            "organization": item.get("organisation", "") or item.get("organization", ""),
            "ministry_or_department": item.get("department", "") or item.get("organisation", ""),
            "category": item.get("category", ""),
            "theme": item.get("theme", ""),
            "current_submissions_count": submitted,
            "max_slots_cap": cap,
            "remaining_slots": remaining,
            "fill_percentage": fill_percentage,
            "status": status,
            "deadline": item.get("deadline", "30 September 2026"),
            "description": item.get("description", ""),
            "youtube_link": item.get("youtube") or None,
            "dataset_link": item.get("dataset") or None
        }
        enriched_statements.append(enriched)

    # Let's save a primary JSON file sorted by submission count descending (most popular to least popular)
    # Also save with complete slot metrics
    json_path = os.path.join(os.path.dirname(__file__), "sih_2026_problem_statements_with_submissions.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(enriched_statements, f, indent=2, ensure_ascii=False)
    print(f"Saved primary JSON dataset to {json_path}")
    
    # Save JSON file sorted in strict ASCENDING order of submission count (lowest submissions first)
    sorted_ascending = sorted(enriched_statements, key=lambda x: (x["current_submissions_count"], x["id"]))
    json_ascending_path = os.path.join(os.path.dirname(__file__), "sih_2026_problem_statements_ascending.json")
    with open(json_ascending_path, "w", encoding="utf-8") as f:
        json.dump(sorted_ascending, f, indent=2, ensure_ascii=False)
    print(f"Saved ascending-sorted JSON dataset to {json_ascending_path}")

    # Let's also save an arranged version sorted by remaining slots (most available slots first)
    sorted_by_availability = sorted(enriched_statements, key=lambda x: (x["remaining_slots"], -x["current_submissions_count"]), reverse=True)
    json_avail_path = os.path.join(os.path.dirname(__file__), "sih_2026_sorted_by_available_slots.json")
    with open(json_avail_path, "w", encoding="utf-8") as f:
        json.dump(sorted_by_availability, f, indent=2, ensure_ascii=False)
    print(f"Saved availability-sorted JSON dataset to {json_avail_path}")
    
    # Statistical analysis
    total = len(enriched_statements)
    frozen_count = sum(1 for x in enriched_statements if x["current_submissions_count"] >= 500)
    open_count = total - frozen_count
    total_submissions = sum(x["current_submissions_count"] for x in enriched_statements)
    
    print("\n--- SUMMARY STATISTICS ---")
    print(f"Total Problem Statements: {total}")
    print(f"Total Submissions Recorded: {total_submissions:,}")
    print(f"Frozen Statements (500/500 Cap reached): {frozen_count} ({round(frozen_count/total*100, 1)}%)")
    print(f"Open Statements (Slots available < 500): {open_count} ({round(open_count/total*100, 1)}%)")
    
    print("\nTop 5 Most Submitted (Open / Available):")
    open_list = [x for x in enriched_statements if x["current_submissions_count"] < 500]
    open_list_sorted = sorted(open_list, key=lambda x: x["current_submissions_count"], reverse=True)
    for x in open_list_sorted[:5]:
        print(f"  [{x['id']}] {x['title'][:50]}... | {x['current_submissions_count']}/500 ({x['remaining_slots']} slots left) | {x['organization']}")
        
    print("\nTop 5 Least Submitted (Hidden Gems with Maximum Slots):")
    least_submitted = sorted(open_list, key=lambda x: x["current_submissions_count"])
    for x in least_submitted[:5]:
        print(f"  [{x['id']}] {x['title'][:50]}... | {x['current_submissions_count']}/500 ({x['remaining_slots']} slots left) | {x['organization']}")

if __name__ == "__main__":
    main()
