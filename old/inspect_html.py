import urllib.request
import re

url = "https://sih.gov.in/sih2026PS"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    
    print(f"HTML Length: {len(html)}")
    
    # Let's search for some text from the page in the HTML
    search_term = "AI-Based early warning and landslide Risk Monitoring"
    matches = [m.start() for m in re.finditer(search_term, html, re.IGNORECASE)]
    print(f"Found {len(matches)} matches for '{search_term}'")
    
    for idx, pos in enumerate(matches):
        print(f"Match {idx+1} at index {pos}:")
        print(html[max(0, pos-200):min(len(html), pos+400)])
        print("-" * 50)
        
except Exception as e:
    print(f"Error: {e}")
