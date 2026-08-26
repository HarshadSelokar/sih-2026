import sys
import os
import json
import urllib.request
import re

# 1. Install beautifulsoup4 dynamically if not present
try:
    from bs4 import BeautifulSoup
except ImportError:
    print("BeautifulSoup4 not found. Installing...")
    import subprocess
    subprocess.run([sys.executable, "-m", "pip", "install", "beautifulsoup4"])
    from bs4 import BeautifulSoup

url = "https://sih.gov.in/sih2026PS"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

print(f"Fetching problem statements from {url}...")
try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    print("Page fetched successfully.")
except Exception as e:
    print(f"Error fetching page: {e}")
    sys.exit(1)

print("Parsing HTML...")
soup = BeautifulSoup(html, 'html.parser')

# Find all modal divs with ID starting with ViewProblemStatement
modal_divs = soup.find_all('div', id=re.compile(r'^ViewProblemStatement'))
print(f"Found {len(modal_divs)} problem statement modals in the HTML.")

problem_statements = []

for modal in modal_divs:
    table = modal.find('table')
    if not table:
        continue
    
    ps_data = {}
    rows = table.find_all('tr')
    for row in rows:
        th = row.find('th')
        td = row.find('td')
        if not th or not td:
            continue
        
        # Get label and clean it
        label = th.get_text(strip=True).lower().replace(":", "").replace("statement ", "")
        # Label mapping:
        # "problem id" -> "id"
        # "problem title" -> "title"
        # "description" -> "description"
        # "organization" -> "organization"
        # "department" -> "department"
        # "category" -> "category"
        # "theme" -> "theme"
        # "youtube link" -> "youtube_link"
        # "dataset link" -> "dataset_link"
        # "contact info" -> "contact_info"
        
        key = label.replace(" ", "_")
        if key == "problem_id":
            key = "id"
        elif key == "problem_title":
            key = "title"
            
        # Clean value
        if key in ["youtube_link", "dataset_link"]:
            link = td.find('a')
            if link and link.has_attr('href'):
                val = link['href'].strip()
            else:
                val = td.get_text(strip=True)
        elif key == "description":
            # Clean description text but preserve formatting (newlines)
            # Find the inner div that contains the description
            style2_div = td.find('div', class_='style-2')
            if style2_div:
                # Replace <br> and <br/> with \n to preserve lines
                for br in style2_div.find_all('br'):
                    br.replace_with('\n')
                val = style2_div.get_text().strip()
            else:
                # Fallback to general text
                for br in td.find_all('br'):
                    br.replace_with('\n')
                val = td.get_text().strip()
            
            # Remove redundant spaces before/after newlines
            val = "\n".join([line.strip() for line in val.split("\n")])
        else:
            val = td.get_text(strip=True)
            
        ps_data[key] = val
        
    if ps_data:
        # Standardize empty values
        for k in ["youtube_link", "dataset_link", "contact_info"]:
            if k in ps_data and (ps_data[k] == "" or ps_data[k] == " " or ps_data[k] is None):
                ps_data[k] = None
        problem_statements.append(ps_data)

# Sort problem statements by ID (numeric if possible, otherwise string)
def get_sort_key(ps):
    ps_id = ps.get('id', '')
    try:
        return int(ps_id)
    except ValueError:
        return ps_id

problem_statements.sort(key=get_sort_key)

print(f"Successfully parsed {len(problem_statements)} problem statements.")

# Write to JSON
json_path = "sih_2026_problem_statements.json"
with open(json_path, 'w', encoding='utf-8') as f:
    json.dump(problem_statements, f, indent=4, ensure_ascii=False)
print(f"Saved JSON data to {json_path}")

# Write to Markdown Catalog
md_path = "sih_2026_problem_statements_catalog.md"
with open(md_path, 'w', encoding='utf-8') as f:
    f.write("# Smart India Hackathon (SIH) 2026 Problem Statements Catalog\n\n")
    f.write(f"This document lists all **{len(problem_statements)}** problem statements crawled from the official SIH 2026 portal on August 26, 2026. You can search this file using your editor, or refer to `sih_2026_problem_statements.json` for raw data.\n\n")
    f.write("| PS ID | Category | Theme | Organization | Title |\n")
    f.write("| --- | --- | --- | --- | --- |\n")
    for ps in problem_statements:
        ps_id = ps.get('id', '')
        category = ps.get('category', '')
        theme = ps.get('theme', '')
        org = ps.get('organization', '')
        title = ps.get('title', '')
        
        # Escape pipe symbols in fields for markdown table compliance
        title_esc = title.replace('|', '\\|')
        org_esc = org.replace('|', '\\|')
        theme_esc = theme.replace('|', '\\|')
        
        f.write(f"| {ps_id} | {category} | {theme_esc} | {org_esc} | {title_esc} |\n")
        
print(f"Saved Markdown Catalog to {md_path}")
print("Scraping completed successfully!")
