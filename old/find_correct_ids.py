import json

with open("sih_2026_problem_statements.json", "r", encoding="utf-8") as f:
    data = json.load(f)

search_terms = ["dementia", "retinopathy", "water purification", "farming assistant", "livelihood mapping", "scheme matching", "gig services", "landslide"]

for term in search_terms:
    print(f"Searching for: '{term}'")
    found = False
    for item in data:
        title = item.get("title", "").lower()
        desc = item.get("description", "").lower()
        if term in title or term in desc:
            print(f" -> Found ID: {item.get('id')} | Title: {item.get('title')} | Theme: {item.get('theme')}")
            found = True
    if not found:
        # Let's try looser search
        words = term.split()
        for item in data:
            title = item.get("title", "").lower()
            if any(w in title for w in words):
                print(f" -> (Partial) Found ID: {item.get('id')} | Title: {item.get('title')}")
                found = True
    print("-" * 50)
