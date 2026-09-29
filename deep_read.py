import json
import sys
import io

# Force UTF-8 output
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('sih_2026_problem_statements.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

candidates = [
    "26003", "26038", "26042", "26181", "26186",
    "26001", "26191", "26192", "26071", "26078", "26079", "26076", "26077",
    "26043", "26044", "26065", "26097",
    "26092", "26091", "26089", "26090", "26093", "26094", "26096",
    "26130", "26188", "26182", "26184",
    "26067", "26068", "26066",
    "26105", "26106", "26095", "26121",
]

outlines = []
for cid in candidates:
    match = [d for d in data if d.get('id') == cid]
    if match:
        d = match[0]
        outlines.append(f"{'='*100}")
        outlines.append(f"ID: {d.get('id')} | Category: {d.get('category')} | Theme: {d.get('theme')}")
        outlines.append(f"Organization: {d.get('organization')}")
        outlines.append(f"Title: {d.get('title')}")
        desc = d.get('description', '')[:2000]
        outlines.append(f"Description:\n{desc}")
        outlines.append("")

with open('deep_read_output.md', 'w', encoding='utf-8') as out:
    out.write('\n'.join(outlines))

print(f"Wrote {len(candidates)} candidate details to deep_read_output.md")
