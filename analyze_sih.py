import json
import os
import re

json_path = "sih_2026_problem_statements.json"
if not os.path.exists(json_path):
    print(f"Error: {json_path} not found. Please run scrape_sih.py first.")
    exit(1)

with open(json_path, 'r', encoding='utf-8') as f:
    problem_statements = json.load(f)

print(f"Loaded {len(problem_statements)} problem statements for analysis.")

# Define keyword lists for social betterment themes
SOCIAL_THEMES = {
    "Healthcare & MedTech": {
        "keywords": [r"health", r"medical", r"dementia", r"elderly", r"osteoarthritis", r"retinopathy", r"patient", r"disease", r"bovine mastitis", r"clinic", r"ayurveda", r"sif", r"fatality", r"trauma", r"stress", r"mental", r"blindness", r"disabled", r"rehabilitation"],
        "count": 0,
        "items": []
    },
    "Agriculture, FoodTech & Rural Livelihoods": {
        "keywords": [r"farmer", r"agriculture", r"crop", r"onion", r"bovine", r"milk", r"chilling can", r"feed", r"silage", r"khadi", r"artisan", r"rural", r"beekeeping", r"honey", r"agarbatti", r"land record", r"cadastral", r"ulpin", r"land governance", r"watershed", r"vegetables", r"cold storage"],
        "count": 0,
        "items": []
    },
    "Disaster Management & Safety": {
        "keywords": [r"disaster", r"landslide", r"flood", r"cyclone", r"rainfall", r"thunderstorm", r"lightning", r"weather forecast", r"early warning", r"rescue", r"safety", r"fire", r"emergency", r"inundation", r"mine safety", r"mine vehicles", r"fog", r"low-visibility", r"subsidence"],
        "count": 0,
        "items": []
    },
    "Smart Education & Social Welfare": {
        "keywords": [r"education", r"learning", r"pedagogy", r"mother tongue", r"vernacular", r"translation", r"career", r"skill", r"job", r"employment", r"cooperative", r"marginalized", r"social justice", r"atrocities", r"victim", r"Ambedkar", r"sc communities", r"gig services", r"disabled", r"livelihood mapping"],
        "count": 0,
        "items": []
    },
    "Clean Water & Environmental Protection": {
        "keywords": [r"water purification", r"water quality", r"waste collection", r"waste segregation", r"pollution", r"clean tech", r"green tech", r"solar-powered", r"renewable", r"sustainable", r"environmental monitoring", r"marine debris", r"oil spill", r"sanitization"],
        "count": 0,
        "items": []
    }
}

# Determine feasibility based on categories and complexity keywords
def evaluate_feasibility(ps):
    title = ps.get('title', '').lower()
    description = ps.get('description', '').lower()
    category = ps.get('category', '').lower()
    theme = ps.get('theme', '').lower()
    
    # Low feasibility: complex hardware, specialized polar/oceanic sensors, defense aerospace hardware, custom compilers/solvers
    low_feasibility_terms = [
        "subzero temperature", "low pressure", "high altitude", "anti-drone", "lidar mapping",
        "piston engines", "electronic warfare", "sonar transmitter", "iceberg trajectory", "antarctic research",
        "polar expedition", "seafloor metal", "ocean observation", "micro barometer", "conformal antenna",
        "precision guidance", "electronic fuze", "artillery shell", "quantum", "unidirectional ip", 
        "gpu-accelerated optimization", "steam stimulation", "sucker rod pump", "well-to-surface",
        "offset well", "dvr/nvr forensic", "forensic analysis tool"
    ]
    
    for term in low_feasibility_terms:
        if term in title or term in description:
            return "Low", "Requires highly specialized hardware, military/naval testing environments, or low-level mathematical modeling that is extremely difficult to prototype in 36 hours."

    if category == "hardware":
        # Check if it has a strong software dashboard/IoT component
        if "dashboard" in title or "dashboard" in description or "monitoring" in title:
            return "Medium-High", "Hardware-Software hybrid. Can be prototyped using standard IoT (ESP32/Arduino) with simulated sensors + web dashboard."
        return "Medium", "Pure hardware. Requires physical product design (CAD, 3D printing) and physical assembly, which can limit the live demonstration depth."
        
    return "High", "Software challenge (Web/Mobile/AI/ML). Highly buildable using modern full-stack web frameworks, standard machine learning libraries, and API integrations."

social_betterment_count = 0
social_betterment_statements = []

for ps in problem_statements:
    title = ps.get('title', '').lower()
    description = ps.get('description', '').lower()
    theme = ps.get('theme', '').lower()
    org = ps.get('organization', '').lower()
    
    matched_themes = []
    for theme_name, theme_data in SOCIAL_THEMES.items():
        matched = False
        for kw in theme_data["keywords"]:
            if re.search(kw, title) or re.search(kw, description) or re.search(kw, theme) or re.search(kw, org):
                matched = True
                break
        if matched:
            matched_themes.append(theme_name)
            theme_data["items"].append(ps)
            theme_data["count"] += 1
            
    if matched_themes:
        ps['social_themes'] = matched_themes
        feasibility_grade, feasibility_reason = evaluate_feasibility(ps)
        ps['feasibility_grade'] = feasibility_grade
        ps['feasibility_reason'] = feasibility_reason
        social_betterment_statements.append(ps)
        social_betterment_count += 1
    else:
        ps['social_themes'] = []
        ps['feasibility_grade'] = "Medium"
        ps['feasibility_reason'] = "General challenge."

# Sort social betterment statements by ID
social_betterment_statements.sort(key=lambda x: int(x.get('id', 0)) if x.get('id', '').isdigit() else x.get('id', ''))

print(f"Found {social_betterment_count} problem statements related to Social Betterment.")
for t, d in SOCIAL_THEMES.items():
    print(f" - {t}: {d['count']} problem statements")

# Let's curate the TOP 8 "Gold Standard" Recommendations for the report.
# These will be explicitly analyzed in the markdown file.
gold_shortlist = [
    {
        "id": "26003",
        "why_social": "Directly improves quality of life for elderly dementia patients by providing cognitive games and memory aid, while offering support features in local languages.",
        "why_feasible": "Pure software (mobile/web app). You can build a gamified frontend in React Native/Flutter, integrate simple cognitive AI tests (face/object recall), and a caregiver dashboard. It has high visual appeal for PPTs and live demos.",
        "ppt_pitch": "Focus on 'Empathetic Tech' - highlight the multilingual interface, offline support for remote regions, and scientifically-backed gamified cognitive exercises. Show a mockup of the caregiver alerts."
    },
    {
        "id": "26180",
        "why_social": "Agriculture is the backbone of India. Early detection of crop diseases, nutrient deficiencies, and irrigation needs directly impacts farmer incomes and food security.",
        "why_feasible": "Highly software-buildable. You can train a MobileNet/ResNet model on crop leaves (custom datasets are publicly available, like PlantVillage). The mobile app can run this model offline (on-device AI via TensorFlow Lite), which is a huge scoring point.",
        "ppt_pitch": "Highlight the 'Offline Edge AI' capability because internet is sparse in Indian farms. Show a clear workflow: Snap Leaf Photo -> Local Inference -> Treatment Action Plan in Vernacular Language."
    },
    {
        "id": "26038",
        "why_social": "Screening for diabetic retinopathy in rural India prevents blindness. Using AI enables local health workers (ASHA) to screen patients without requiring an ophthalmologist.",
        "why_feasible": "Uses deep learning image classification on retinal images (readily available public datasets like Messidor/APTOS). Using 'Explainable AI' (Grad-CAM) highlights the exact lesion areas, which builds medical trust.",
        "ppt_pitch": "Emphasize 'Explainability' (Grad-CAM heatmaps) because AI in medicine needs justification. Pitch a low-cost smartphone attachments model for screening."
    },
    {
        "id": "26097",
        "why_social": "Helps SC/marginalized communities mapped to NSQF skilling programs. It addresses employment and livelihood upliftment at the grassroot level using a voice-based interface.",
        "why_feasible": "Uses Conversational AI (Bhashini API or standard TTS/STT) and a skill mapping recommendation engine. Excellent software project leveraging NLP.",
        "ppt_pitch": "Pitch the voice interface in regional dialects. Explain how a user can speak in their native tongue and get tailored skill development pathways."
    },
    {
        "id": "26092",
        "why_social": "Marginalized micro-entrepreneurs fail to benefit from government schemes due to information barriers. AI matching bridges this gap directly.",
        "why_feasible": "Can be built using Retrieval-Augmented Generation (RAG) over a database of government schemes. Standard frontend forms generate user profiles to match schemes.",
        "ppt_pitch": "Pitch a 'One-Stop Scheme Navigator'. Show how natural language queries ('I want to open a tailoring shop, what help can I get?') map to schemes using semantic search."
    },
    {
        "id": "26089",
        "why_social": "Provides a cooperative alternative to corporate gig apps (like Urban Company). Empowers local service providers (plumbers, cleaners, electricians) and retains profits in the community.",
        "why_feasible": "A location-based gig-matching platform (web/mobile app). Standard database and geolocation routing, but layered with a cooperative dividend-sharing dashboard.",
        "ppt_pitch": "Frame it as 'Ethical Gig Economy'. Highlight fair pricing, direct-to-worker payments, and the cooperative dashboard which shows collective earnings and welfare funds."
    },
    {
        "id": "26001",
        "why_social": "The North Eastern Region faces devastating landslides. Real-time predictive early warning systems save lives, protect roads, and maintain logistics.",
        "why_feasible": "A software GIS platform. You can pull public weather APIs (IMD/OpenWeather), combine with digital elevation models (DEM) and soil data, and show risk heatmaps on a Leaflet map. Add a portal for citizens to upload geo-tagged hazard photos.",
        "ppt_pitch": "Focus on 'Community-Driven Early Warning'. Show the GIS dashboard with active threat levels and explain the SMS alerting system for vulnerable villages."
    },
    {
        "id": "26040",
        "why_social": "Access to clean drinking water in mining-affected and rural areas is a critical health concern. Real-time monitoring prevents mass health crises.",
        "why_feasible": "Can be modeled as an IoT prototype. Use standard sensors (TDS, pH, turbidity, temperature) connected to an ESP32 micro-controller. Send telemetry to a beautiful dashboard via MQTT or HTTP.",
        "ppt_pitch": "Present a 'Low-Cost IoT Filtration Companion'. Show a physical prototype (or CAD design) connected to a real-time web portal that triggers automatic contamination alerts."
    }
]

# Find full details for the gold shortlist from the parsed list
selected_details = []
for item in gold_shortlist:
    matches = [p for p in problem_statements if p.get('id', '') == item['id']]
    if matches:
        detail = matches[0].copy()
        detail.update(item)
        selected_details.append(detail)

# Write Recommendation Report
report_path = "sih_2026_recommended_statements.md"
with open(report_path, 'w', encoding='utf-8') as f:
    f.write("# Smart India Hackathon (SIH) 2026: Mentors' Choice & Winning Strategy\n\n")
    f.write("This report provides a curated selection of problem statements from the **226 released challenges** of SIH 2026. Following your mentor's guidance, we have prioritized problems that offer **direct social betterment, improve quality of life, and uplift rural/marginalized communities**. \n\n")
    f.write("> [!IMPORTANT]\n")
    f.write("> **Selection Strategy:** To guarantee selection in the internal round and advance to the national finals, a problem statement must not only be high-impact but also **highly feasible to prototype in a 36-hour hackathon**. We have graded each recommendation for feasibility to ensure your team can deliver a working, visually stunning demo.\n\n")
    
    f.write("## 📊 Summary of Social Betterment Challenges\n\n")
    f.write(f"Out of 226 total problem statements, we identified **{social_betterment_count}** statements that directly align with social betterment. Here is the distribution by theme:\n\n")
    f.write("| Theme | Number of Challenges | Target Beneficiaries |\n")
    f.write("| --- | --- | --- |\n")
    for t, d in SOCIAL_THEMES.items():
        f.write(f"| {t} | {d['count']} | Rural farmers, patients, elderly, students, and marginalized groups |\n")
    f.write("\n---\n\n")
    
    f.write("## 🏆 The Gold Shortlist: Top 8 Recommendations\n\n")
    f.write("These 8 problem statements represent the absolute best intersection of **high social impact** (highly favored by SIH evaluators) and **high software buildability** (enabling your team to present a fully functional prototype).\n\n")
    
    for idx, ps in enumerate(selected_details):
        f.write(f"### {idx+1}. PS ID {ps['id']}: {ps['title']}\n\n")
        f.write(f"- **Ministry/Organization:** {ps.get('organization', 'N/A')} ({ps.get('department', 'N/A')})\n")
        f.write(f"- **Category:** {ps.get('category', 'N/A')} | **Theme:** {ps.get('theme', 'N/A')}\n")
        f.write(f"- **Feasibility:** **{ps['feasibility_grade']}**\n\n")
        
        f.write("#### 📝 Brief Description\n")
        desc = ps.get('description', '')
        # Truncate description slightly for readability if it's too long
        if len(desc) > 800:
            desc = desc[:797] + "..."
        f.write(f"```\n{desc}\n```\n\n")
        
        f.write(f"#### ❤️ Why it fits the Mentor's Advice (Social Impact)\n")
        f.write(f"{ps['why_social']}\n\n")
        
        f.write(f"#### ⚙️ Why it is Feasible for a 36-Hour Hackathon\n")
        f.write(f"{ps['why_feasible']}\n\n")
        
        f.write(f"#### 🎯 Winning Pitch & PPT Strategy\n")
        f.write(f"{ps['ppt_pitch']}\n\n")
        f.write("\n---\n\n")
        
    f.write("## 📋 Comprehensive Catalog of Social Betterment Statements\n\n")
    f.write("Below is the complete list of all problem statements matching the social impact criteria. Use this list to browse alternative options that may match your team's specific skills (e.g. mobile development, machine learning, IoT, GIS).\n\n")
    f.write("| PS ID | Category | Theme | Organization | Title | Feasibility |\n")
    f.write("| --- | --- | --- | --- | --- | --- |\n")
    for ps in social_betterment_statements:
        ps_id = ps.get('id', '')
        category = ps.get('category', '')
        theme = ps.get('theme', '')
        org = ps.get('organization', '')
        title = ps.get('title', '')
        feas = ps.get('feasibility_grade', 'Medium')
        
        # Escape pipe symbols
        title_esc = title.replace('|', '\\|')
        org_esc = org.replace('|', '\\|')
        theme_esc = theme.replace('|', '\\|')
        
        f.write(f"| {ps_id} | {category} | {theme_esc} | {org_esc} | {title_esc} | **{feas}** |\n")

    f.write("\n\n---\n\n")
    f.write("## 💡 General Strategy to Excel in the Internal Hackathon & Finals\n\n")
    f.write("To maximize your selection probability, structure your Idea PPT and development roadmap using the following guidelines:\n\n")
    f.write("### 1. The Ideal Team Composition\n")
    f.write("- **The UI/UX Specialist:** In hackathons, visual appeal represents 50% of the initial impression. Ensure you have one person dedicated entirely to building a gorgeous, premium frontend (Vite/React, Tailwind CSS, clean HSL colors, glassmorphism, responsive components).\n")
    f.write("- **The Backend/API Developer:** Connects database, implements business logic, and integrates external APIs (e.g., weather feeds, Bhashini translation, SMS gateways).\n")
    f.write("- **The AI/ML Engineer:** Focuses on pre-trained models, fine-tuning, or RAG setup. Note: Do not write complex model architectures from scratch during the hackathon. Use pre-trained weights (Hugging Face, TensorFlow Hub) and wrap them in FastAPI.\n")
    f.write("- **The Domain/Presenter:** One team member who deeply understands the problem statement, guidelines, and who can pitch the solution with clarity and passion. They will drive the Q&A sessions.\n\n")
    
    f.write("### 2. Crafting the Winning Idea PPT\n")
    f.write("- **Slide 1: Title & Team details** (Keep it neat, include your unique Team Name).\n")
    f.write("- **Slide 2: Problem Description** (Reframe the official problem statement. Use a user-centric story, e.g., 'Meet Ramesh, a farmer who lost 40% of his crop because...').\n")
    f.write("- **Slide 3: Proposed Solution** (List 3 core pillars of your solution. Don't be vague. Be extremely specific, e.g., 'An offline-first Android App, an AI-powered treatment recommender, and an AICTE-approved cooperative linkage dashboard').\n")
    f.write("- **Slide 4: Architecture Diagram** (A clean flow diagram showing Mobile/Web Client -> API Gateway -> ML Models & Database -> Third Party Integrations).\n")
    f.write("- **Slide 5: Technical Stack** (List modern, relevant tools. E.g., Flutter, Fastify, PyTorch, Supabase, Docker. Avoid listing outdated tech like PHP or JSP).\n")
    f.write("- **Slide 6: Use Cases & Beneficiaries** (Explicitly highlight the social impact, who benefits, and how it aligns with government initiatives).\n")
    f.write("- **Slide 7: Competitive Advantage / Innovation** (Why is your solution better than existing market apps? Highlight features like **low-bandwidth sync**, **multilingual voice assistance via Bhashini**, or **Explainable AI**).\n")
    f.write("- **Slide 8: Team Skills & Feasibility** (Prove that your team has the skills to build this in 36 hours).\n\n")
    
    f.write("### 3. Key High-Scoring Features to Include in Your Solution\n")
    f.write("- **Offline/Low-Network Support:** Essential for rural/disaster applications. Demonstrate SQLite/Hive storage syncing with the cloud once network is restored.\n")
    f.write("- **Multilingual Support:** Integrate the Bhashini API or Hugging Face translation models so users in the North East or rural areas can interact in their mother tongue.\n")
    f.write("- **Role-Based Dashboards:** Ensure there is an interface for the general public (citizens/farmers/patients) and a separate command dashboard for government administrators/doctors/caregivers.\n")

print(f"Saved Recommendation Report to {report_path}")
print("Analysis completed successfully!")
