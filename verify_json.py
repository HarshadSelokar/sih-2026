import json

with open("sih_2026_problem_statements.json", "r", encoding="utf-8") as f:
    data = json.load(f)

selected_ids = ["26001", "26003", "26039", "26041", "26107", "26110", "26115", "26146"]

for item in data:
    if item.get("id") in selected_ids:
        print(f"ID: {item.get('id')}")
        print(f"Title: {item.get('title')}")
        print(f"Theme: {item.get('theme')}")
        print(f"Description length: {len(item.get('description', ''))}")
        print(f"Description sample: {item.get('description', '')[:200]}...")
        print("-" * 50)
