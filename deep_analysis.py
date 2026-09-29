import json

with open('sih_2026_problem_statements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

# Filter: Software only, exclude agriculture/farm themes
agri_keywords = ['agriculture', 'foodtech', 'rural development', 'farm', 'crop', 'agri']

filtered = []
for d in data:
    cat = d.get('category', '').lower()
    theme = d.get('theme', '').lower()
    title = d.get('title', '').lower()
    desc = d.get('description', '').lower()
    
    if cat != 'software':
        continue
    
    # Skip agriculture/farm related
    is_agri = False
    for kw in agri_keywords:
        if kw in theme or kw in title:
            is_agri = True
            break
    if is_agri:
        continue
    
    filtered.append(d)

print(f"Software non-agriculture count: {len(filtered)}")
print("=" * 120)

for d in filtered:
    ps_id = d.get('id', '')
    theme = d.get('theme', '')
    org = d.get('organization', '')
    title = d.get('title', '')
    desc_len = len(d.get('description', ''))
    print(f"ID: {ps_id} | Theme: {theme}")
    print(f"  Org: {org}")
    print(f"  Title: {title[:150]}")
    print(f"  Desc length: {desc_len} chars")
    print("-" * 120)
