import urllib.request
import re

url = "https://sih.gov.in/sih2026PS"
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}

try:
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req) as response:
        html = response.read().decode('utf-8')
    
    # Find the modal ViewProblemStatement26001
    modal_id = "ViewProblemStatement26001"
    start_pos = html.find(f'id="{modal_id}"')
    if start_pos != -1:
        # Let's grab about 5000 characters from start_pos
        chunk = html[start_pos:start_pos+8000]
        # Find closing div of modal-content or similar
        print(chunk)
    else:
        print("Modal not found")
        
except Exception as e:
    print(f"Error: {e}")
