# Smart India Hackathon (SIH) 2026: Mentors' Choice & Winning Strategy

This report provides a curated selection of problem statements from the **226 released challenges** of SIH 2026. Following your mentor's guidance, we have prioritized problems that offer **direct social betterment, improve quality of life, and uplift rural/marginalized communities**. 

> [!IMPORTANT]
> **Selection Strategy:** To guarantee selection in the internal round and advance to the national finals, a problem statement must not only be high-impact but also **highly feasible to prototype in a 36-hour hackathon**. We have graded each recommendation for feasibility to ensure your team can deliver a working, visually stunning demo.

## 📊 Summary of Social Betterment Challenges

Out of 226 total problem statements, we identified **178** statements that directly align with social betterment. Here is the distribution by theme:

| Theme | Number of Challenges | Target Beneficiaries |
| --- | --- | --- |
| Healthcare & MedTech | 90 | Rural farmers, patients, elderly, students, and marginalized groups |
| Agriculture, FoodTech & Rural Livelihoods | 70 | Rural farmers, patients, elderly, students, and marginalized groups |
| Disaster Management & Safety | 84 | Rural farmers, patients, elderly, students, and marginalized groups |
| Smart Education & Social Welfare | 84 | Rural farmers, patients, elderly, students, and marginalized groups |
| Clean Water & Environmental Protection | 31 | Rural farmers, patients, elderly, students, and marginalized groups |

---

## 🏆 The Gold Shortlist: Top 8 Recommendations

These 8 problem statements represent the absolute best intersection of **high social impact** (highly favored by SIH evaluators) and **high software buildability** (enabling your team to present a fully functional prototype).

### 1. PS ID 26003: AI-Based Cognitive Gaming and Memory Assistance Platform for Elderly Dementia Patients in North Eastern Region (NER)

- **Ministry/Organization:** Ministry of Development of North Eastern Region (MDoNER) (Ministry of Development of North Eastern Region (MDoNER))
- **Category:** Software | **Theme:** MedTech / BioTech / HealthTech
- **Feasibility:** **High**

#### 📝 Brief Description
```
Background:

The North Eastern Region (NER) is witnessing a gradual rise in age-related cognitive disorders such as dementia and memory loss among the elderly population. Many families in remote and rural areas face challenges in accessing specialized neurological care, cognitive therapy, and long-term elderly support services due to limited healthcare infrastructure and geographical barriers.

Elderly patients suffering from dementia often experience memory decline, confusion, anxiety, and social isolation, while caregivers face difficulties in continuous monitoring and engagement. There is limited availability of affordable and culturally inclusive digital therapeutic solutions tailored for elderly individuals in the North-Eastern Region.

To strengthen elderly healthcare and improve ...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
Directly improves quality of life for elderly dementia patients by providing cognitive games and memory aid, while offering support features in local languages.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
Pure software (mobile/web app). You can build a gamified frontend in React Native/Flutter, integrate simple cognitive AI tests (face/object recall), and a caregiver dashboard. It has high visual appeal for PPTs and live demos.

#### 🎯 Winning Pitch & PPT Strategy
Focus on 'Empathetic Tech' - highlight the multilingual interface, offline support for remote regions, and scientifically-backed gamified cognitive exercises. Show a mockup of the caregiver alerts.


---

### 2. PS ID 26180: A field-deployable AI-powered Smart Farming Assistant that helps farmers detect crop diseases, pests, nutrient deficiencies, and irrigation needs at an early stage, while improving resilience against droughts, floods, heat waves, and other agricultural risks common in India. The solution should enable higher yields, lower input costs, more efficient water usage, and faster response to emerging threats through real-time on-device intelligence.

- **Ministry/Organization:** Qualcomm Inc (Qualcomm Inc)
- **Category:** Hardware | **Theme:** Agriculture, FoodTech & Rural Development
- **Feasibility:** **Medium-High**

#### 📝 Brief Description
```
Background Agriculture remains a primary livelihood for millions of people in India, but farmers face recurring challenges from droughts, erratic rainfall, floods, pest infestations, crop diseases, heat stress, and soil degradation. Climate variability is increasing the frequency of these risks, affecting crop productivity and farm incomes. Many small and marginal farmers lack access to timely diagnostics and expert advice, particularly in regions with limited internet connectivity.

Environmental monitoring, edge AI, and local sensing technologies can help deliver real-time insights directly at the farm level without relying on continuous cloud access.Early detection of crop stress, pest outbreaks, irrigation issues, and adverse environmental conditions can significantly reduce crop lo...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
Agriculture is the backbone of India. Early detection of crop diseases, nutrient deficiencies, and irrigation needs directly impacts farmer incomes and food security.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
Highly software-buildable. You can train a MobileNet/ResNet model on crop leaves (custom datasets are publicly available, like PlantVillage). The mobile app can run this model offline (on-device AI via TensorFlow Lite), which is a huge scoring point.

#### 🎯 Winning Pitch & PPT Strategy
Highlight the 'Offline Edge AI' capability because internet is sparse in Indian farms. Show a clear workflow: Snap Leaf Photo -> Local Inference -> Treatment Action Plan in Vernacular Language.


---

### 3. PS ID 26038: Explainable AI for Diabetic Retinopathy Screening in Rural India

- **Ministry/Organization:** MathWorks (MathWorks)
- **Category:** Software | **Theme:** MedTech / BioTech / HealthTech
- **Feasibility:** **High**

#### 📝 Brief Description
```
Background:

India has over 77 million diabetic adults - the second highest globally. Diabetic Retinopathy (DR) affects ~18% of this population and is a leading cause of preventable blindness. Early screening can prevent90% of vision loss, but India has only ~1 ophthalmologist per 100,000 rural population, making mass manual screening infeasible. Existing AI solutions function as black boxes, lack clinical validation rigor, and fail with variable image quality from portable fundus cameras in field conditions. A robust, explainable, and validated screening system is essential for deployment in primary healthcare centres across rural India.

Description:

Design a MATLAB-based retinal image analysis pipeline for automated DR screening addressing real-world deployment challenges:

1. Image...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
Screening for diabetic retinopathy in rural India prevents blindness. Using AI enables local health workers (ASHA) to screen patients without requiring an ophthalmologist.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
Uses deep learning image classification on retinal images (readily available public datasets like Messidor/APTOS). Using 'Explainable AI' (Grad-CAM) highlights the exact lesion areas, which builds medical trust.

#### 🎯 Winning Pitch & PPT Strategy
Emphasize 'Explainability' (Grad-CAM heatmaps) because AI in medicine needs justification. Pitch a low-cost smartphone attachments model for screening.


---

### 4. PS ID 26097: AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY

- **Ministry/Organization:** Ministry of Social Justice and Empowerment (MoSJE) (Department of Social Justice and Empowerment)
- **Category:** Software | **Theme:** Agriculture, FoodTech & Rural Development
- **Feasibility:** **High**

#### 📝 Brief Description
```
• Background
• The Pradhan Mantri Anusuchit Jaati Abhyuday Yojana (PM-AJAY) aims to reduce poverty among Scheduled Caste (SC) communities through livelihood promotion, skill development, and enterprise support under its Grant-in-Aid (GIA) component. A major challenge in implementation is the identification of appropriate skill training pathways that align with both the aspirations of beneficiaries and the actual livelihood opportunities available in their local regions.
• Many target beneficiaries face barriers such as low digital literacy, limited awareness of modern trades, language constraints, and difficulty navigating text-heavy digital systems. As a result, there is often a mismatch between enrolled training programs and the beneficiaryâ€™s interests, capabilities, or local market...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
Helps SC/marginalized communities mapped to NSQF skilling programs. It addresses employment and livelihood upliftment at the grassroot level using a voice-based interface.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
Uses Conversational AI (Bhashini API or standard TTS/STT) and a skill mapping recommendation engine. Excellent software project leveraging NLP.

#### 🎯 Winning Pitch & PPT Strategy
Pitch the voice interface in regional dialects. Explain how a user can speak in their native tongue and get tailored skill development pathways.


---

### 5. PS ID 26092: AI-Driven Scheme Matching for Marginalized Entrepreneurs

- **Ministry/Organization:** Ministry of Social Justice and Empowerment (MoSJE) (Department of Social Justice and Empowerment)
- **Category:** Software | **Theme:** Smart Automation
- **Feasibility:** **High**

#### 📝 Brief Description
```
• Background To promote the socio-economic empowerment of the Scheduled Caste (SC) population, the government provides concessional financial assistance and educational loans. Beneficiaries with an annual family income of up to ?5.00 Lakhs are eligible for various tailored financial products covering up to 90% of their project or education costs at highly concessional interest rates (typically 6.5% to 8% per annum).

However, direct loan applications are not entertained. Instead, funds are routed through a 'Channel Finance System' comprising over 100 Channel Partners, including State Channelizing Agencies (SCAs), Public Sector Banks (PSBs), Regional Rural Banks (RRBs), and NBFC-MFIs.

• Challenge Citizens often lack awareness regarding which specific credit scheme fits their needsâ€”suc...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
Marginalized micro-entrepreneurs fail to benefit from government schemes due to information barriers. AI matching bridges this gap directly.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
Can be built using Retrieval-Augmented Generation (RAG) over a database of government schemes. Standard frontend forms generate user profiles to match schemes.

#### 🎯 Winning Pitch & PPT Strategy
Pitch a 'One-Stop Scheme Navigator'. Show how natural language queries ('I want to open a tailoring shop, what help can I get?') map to schemes using semantic search.


---

### 6. PS ID 26089: Cooperative Gig Services Platform for Household & Community Services

- **Ministry/Organization:** Ministry of Cooperation (National Council for Cooperative Training (NCCT))
- **Category:** Software | **Theme:** Agriculture, FoodTech & Rural Development
- **Feasibility:** **High**

#### 📝 Brief Description
```
• Background Labour Cooperative Federations and Labour Cooperative Societies possess a large pool of skilled workers such as electricians, plumbers, carpenters, painters, domestic helpers, caregivers, drivers, gardeners,cleaners, and technicians. However, they lack a structured digital platform to connect these workers with households and institutions requiring such services.Private platforms currently dominate this market, while cooperative workers often remain underutilized despite having skills and local presence.
• Problem Statement To develop a cooperative-owned digital service marketplace platform that enables Labour Cooperative Federations and Labour Cooperative Societies to provide verified household and community services while ensuring fair wages, worker welfare, and consumer ...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
Provides a cooperative alternative to corporate gig apps (like Urban Company). Empowers local service providers (plumbers, cleaners, electricians) and retains profits in the community.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
A location-based gig-matching platform (web/mobile app). Standard database and geolocation routing, but layered with a cooperative dividend-sharing dashboard.

#### 🎯 Winning Pitch & PPT Strategy
Frame it as 'Ethical Gig Economy'. Highlight fair pricing, direct-to-worker payments, and the cooperative dashboard which shows collective earnings and welfare funds.


---

### 7. PS ID 26001: AI-Based early warning and landslide Risk Monitoring System in NER

- **Ministry/Organization:** Ministry of Development of North Eastern Region (MDoNER) (Ministry of Development of North Eastern Region (MDoNER))
- **Category:** Software | **Theme:** Disaster Management
- **Feasibility:** **High**

#### 📝 Brief Description
```
Background:

The North Eastern Region (NER) frequently faces landslides, flash floods, road blockages, and slope failures due to heavy rainfall, fragile terrain, and unplanned hill cutting. These incidents often disrupt connectivity, damage infrastructure, delay emergency response, and isolate remote villages for days. Currently, monitoring of vulnerable zones is mostly reactive and dependent on manual reporting. There is limited use of real-time predictive systems for identifying high-risk zones and issuing early warnings to authorities and local communities. With increasing climate vulnerability in the region, there is a need for an AI-enabled real-time monitoring and prediction system that can help authorities take preventive action before disasters occur.

Description:

This problem...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
The North Eastern Region faces devastating landslides. Real-time predictive early warning systems save lives, protect roads, and maintain logistics.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
A software GIS platform. You can pull public weather APIs (IMD/OpenWeather), combine with digital elevation models (DEM) and soil data, and show risk heatmaps on a Leaflet map. Add a portal for citizens to upload geo-tagged hazard photos.

#### 🎯 Winning Pitch & PPT Strategy
Focus on 'Community-Driven Early Warning'. Show the GIS dashboard with active threat levels and explain the SMS alerting system for vulnerable villages.


---

### 8. PS ID 26040: Smart Water Purification and Quality Monitoring System for Rural and Mining-Affected Areas.

- **Ministry/Organization:** Governmcnt of Jharkhand (Department of Higher & Technical Education)
- **Category:** Hardware | **Theme:** Clean & Green Technology
- **Feasibility:** **Medium-High**

#### 📝 Brief Description
```
Background:

Access to safe drinking water remains a significant challenge in many rural and mining-affected regions of Jharkhand. Groundwater and surface water sources are often contaminated by suspended particles, excessive minerals, microbial impurities, and mining-related pollutants, making them unsafe for consumption. Additionally, the lack of real-time water quality monitoring makes it difficult for communities to assess water safety and take timely corrective actions.

There is a need for an affordable and intelligent solution that can both monitor water quality and purify, contaminated water. A smart water purification and quality monitoring system can help ensure access to safe drinking water, improve public health, and support sustainable water management in underserved commun...
```

#### ❤️ Why it fits the Mentor's Advice (Social Impact)
Access to clean drinking water in mining-affected and rural areas is a critical health concern. Real-time monitoring prevents mass health crises.

#### ⚙️ Why it is Feasible for a 36-Hour Hackathon
Can be modeled as an IoT prototype. Use standard sensors (TDS, pH, turbidity, temperature) connected to an ESP32 micro-controller. Send telemetry to a beautiful dashboard via MQTT or HTTP.

#### 🎯 Winning Pitch & PPT Strategy
Present a 'Low-Cost IoT Filtration Companion'. Show a physical prototype (or CAD design) connected to a real-time web portal that triggers automatic contamination alerts.


---

## 📋 Comprehensive Catalog of Social Betterment Statements

Below is the complete list of all problem statements matching the social impact criteria. Use this list to browse alternative options that may match your team's specific skills (e.g. mobile development, machine learning, IoT, GIS).

| PS ID | Category | Theme | Organization | Title | Feasibility |
| --- | --- | --- | --- | --- | --- |
| 26001 | Software | Disaster Management | Ministry of Development of North Eastern Region (MDoNER) | AI-Based early warning and landslide Risk Monitoring System in NER | **High** |
| 26002 | Software | Transportation & Logistics | Ministry of Development of North Eastern Region (MDoNER) | Al-Based Smart Logistics and Accessibility Intelligence Platform for North Eastern Region (NER) | **High** |
| 26003 | Software | MedTech / BioTech / HealthTech | Ministry of Development of North Eastern Region (MDoNER) | AI-Based Cognitive Gaming and Memory Assistance Platform for Elderly Dementia Patients in North Eastern Region (NER) | **High** |
| 26004 | Hardware | MedTech / BioTech / HealthTech | Ministry of Development of North Eastern Region (MDoNER) | Al-Assisted Early Detection System for Osteoarthritis (OA) Risk Markers in North Eastern Region (NER) | **Medium-High** |
| 26005 | Hardware | Agriculture, FoodTech & Rural Development | Ministry of Development of North Eastern Region (MDoNER) | Solar-Powered Smart Mini Cold Storage System for Fresh Vegetables in North Eastern Region (NER) | **Medium** |
| 26006 | Software | Transportation & Logistics | Ministry of Steel | Development of an Intelligent Freight Forecasting Model for Optimized Vessel Chartering and Bulk Cargo Procurement from overseas to East Coast of India | **High** |
| 26007 | Hardware | Smart Automation | Ministry of Steel | Safe and Efficient Operation of Mine Vehicles in Fog and Low-Visibility Conditions in Open Cast Iron Ore Mines. | **Medium** |
| 26008 | Hardware | Smart Automation | Ministry of Steel | Belt Joint Rupture and Conveyor Belt Damages in Iron Ore Mining Industry: Intelligent Monitoring and Prediction of Conveyor Belt Joint Rupture and Damages in Iron Ore Mining Industry. | **Medium-High** |
| 26009 | Software | Space Technology | Ministry of Steel | Using AI/ML and Space Technology to Identify Manganese Reserves and Overcome Production Shortfalls. | **High** |
| 26010 | Hardware | Agriculture, FoodTech & Rural Development | Ministry of Rural Development | Survey/Resurvey of Rural Agricultural Land in lndia | **Medium** |
| 26011 | Software | Smart Automation | Ministry of Rural Development | 3D ULPIN Generation and vertical Property Mapping SYstem | **High** |
| 26012 | Software | Smart Automation | Ministry of Rural Development | AI-Based Automated Urban Parcel Mapping and Cadastral Feature Extraction System using Drone lmagery | **High** |
| 26013 | Software | Smart Automation | Ministry of Rural Development | Automated lntegration and lntelligent Harmonization of Multi-source Geospatial Data for urban Land Record Management. | **High** |
| 26014 | Software | Agriculture, FoodTech & Rural Development | Ministry of Rural Development | An lntegrated GIS-based Digital Public lnfrastructure for Land Governance | **High** |
| 26015 | Software | Agriculture, FoodTech & Rural Development | Ministry of Rural Development | Application of Geospatial Techniques for visualization and analysis to interpret Geo-Coded lmages to enhance watershed Development Outcomes. | **High** |
| 26016 | Software | Smart Automation | Ministry of Rural Development | Real-Time National Land Acquisition & Management System for End-to-End Digital Monitoring and Decision Support | **High** |
| 26017 | Software | Smart Automation | Ministry of Rural Development | Predictive Analytics System for Early Detection of Land Acquisition Delays | **High** |
| 26018 | Software | Smart Automation | Ministry of Rural Development | Intelligent Land Record Digitization and Validation System | **High** |
| 26019 | Software | Smart Automation | Ministry of Rural Development | National Digital Platform for Research, Policy Innovation, and Evidence-Based Land Governance | **High** |
| 26020 | Hardware | Agriculture, FoodTech & Rural Development | Ministry of MSME | Design and Development of Innovative Hand-Spinning Equipment for Enhancing Khadi Artisan Productivity and Income | **Medium** |
| 26021 | Software | Agriculture, FoodTech & Rural Development | Ministry of MSME | Honey Chain: A block chain-based system for honey traceability and smart beekeeping management. | **High** |
| 26022 | Hardware | Agriculture, FoodTech & Rural Development | Ministry of MSME | Design and develop a smart, solar-powered drying and compact packaging system to support home-based agarbatti manufacturing by rural women artisans. | **Medium** |
| 26024 | Software | Smart Automation | Ministry of Coal | AI-Based Smart Governance and Compliance Monitoring System for Coal Mines | **High** |
| 26025 | Hardware | Smart Automation | Ministry of Coal | Development of an AI-enabled Low Cost Real Time Mine Subsidence Monitoring, Prediction and Early Warning System for Underground Coal Mines in India | **Medium-High** |
| 26026 | Hardware | Blockchain & Cybersecurity | Ministry of Railways | Development of Mobile (Quadruped)/Handheld Device/System for Real-Time Detection of Narcotics and Explosives across Indian Railways. | **Medium-High** |
| 26027 | Software | Transportation & Logistics | Ministry of Railways | Al-Powered Automatic Block Planning to Maximize Asset Availability for Train Operations on Indian Railways | **High** |
| 26028 | Software | Smart Automation | Ministry of Railways | Dynamic Forecast of Expected Time of Arrival (ETA) for Coaching Trains | **High** |
| 26029 | Hardware | Smart Automation | Ministry of Consumer Affairs, Food & Public Distribution | Automated High-Current Short-Circuit Test System for IEC 60898-1:2015 MCB Compliance. | **Medium** |
| 26030 | Hardware | Smart Automation | Ministry of Consumer Affairs, Food & Public Distribution | Automated Cable Specimen Preparation System for IS 10810 and IS 7098 Compliance. | **Medium** |
| 26031 | Software | Smart Automation | Ministry of Consumer Affairs, Food & Public Distribution | Quality assessment and grading of onions are often subjective and vary across procurement centers, resulting in disputes and inconsistencies. | **High** |
| 26032 | Software | Smart Automation | Ministry of Consumer Affairs, Food & Public Distribution | Farmers often face long waiting times, lack of information regarding procurement schedules, and uncertainty about procurement status. | **High** |
| 26033 | Software | Agriculture, FoodTech & Rural Development | Ministry of Consumer Affairs, Food & Public Distribution | Multiple intermediaries reduce farmers earnings and increase consumer prices. | **High** |
| 26035 | Software | Miscellaneous | Ministry of Consumer Affairs, Food & Public Distribution | Development of a Software Program/Application for Generation of Test Reports for Non-Automatic Weighing Instruments (NAWI) as per OIML Recommendation R- 76 | **High** |
| 26037 | Software | Smart Vehicles | MathWorks | Adaptive Path Planning and Collision Avoidance for Autonomous Vehicles on Unstructured Indian Roads | **High** |
| 26038 | Software | MedTech / BioTech / HealthTech | MathWorks | Explainable AI for Diabetic Retinopathy Screening in Rural India | **High** |
| 26039 | Hardware | Smart Automation | Governmcnt of Jharkhand | Al-Powered Underground Mine Safety, Monitoring and Rescue System. | **Medium-High** |
| 26040 | Hardware | Clean & Green Technology | Governmcnt of Jharkhand | Smart Water Purification and Quality Monitoring System for Rural and Mining-Affected Areas. | **Medium-High** |
| 26041 | Software | Smart Education | Governmcnt of Jharkhand | AR-Based Vocational Training Simulator for Industrial Safety in Jharkhand's Mining & Manufacturing Sector | **High** |
| 26042 | Software | Smart Education | Governmcnt of Jharkhand | Al-Powered Vernacular Pedagogy and Real-Time Translation Tool for Mother Tongue-Based Primary Education | **High** |
| 26043 | Software | Smart Education | Governmcnt of Jharkhand | A digital platform to crowdsource societal challenges and facilitate collaborative problem solving through universities and industry partnerships | **High** |
| 26044 | Software | Smart Automation | Ministry of Ayush | Portal for Academia - Industry collaboration for Skill Mapping, Internships and Placement | **High** |
| 26045 | Software | MedTech / BioTech / HealthTech | Ministry of Ayush | IP-SAKTI Sahayak a multilingual, RAG-based (source-cited) AI assistant for Intellectual Property and regulatory guidance in Ayurveda, across national and international regimes. | **High** |
| 26046 | Software | MedTech / BioTech / HealthTech | Ministry of Ayush | AIIA Clinical Trials Dashboard - a real-time, cloud-based, GCP-compliant Clinical Trial Management System (CTMS) for Ayurveda research, with CDISC/FHIR-interoperable data, role-based KPIs, and integrated ethics, regulatory (CTRI / NDCT Rules 2019) and pharma covigilance tracking. | **High** |
| 26047 | Software | MedTech / BioTech / HealthTech | Ministry of Ayush | Patient Case-Taking Software | **High** |
| 26048 | Hardware | MedTech / BioTech / HealthTech | Ministry of Ayush | iKwath - a pod-based smart Kwatha (Kadha) maker that prepares a fresh, AFI/API-standardized decoction from coarse powder (yavaku?a c?r?a) on demand, in the shortest practical time without altering the decoctions quality or yield | **Medium** |
| 26049 | Hardware | Smart Automation | DRDO | Modifications to improve the reliability, efficiency,and lifespan of electrical and electronic equipment and systems in the ambient condition of subzero temperature and low pressure of High Altitude Areas(HAA) and Super High Altitude Areas (SHAA) of Ladakh region. | **Low** |
| 26050 | Hardware | Robotics and Drones | DRDO | High Altitude Performance Optimization and Robust Design of Anti-Drone System. | **Low** |
| 26051 | Software | Miscellaneous | DRDO | Software Based Model Development for Design of Area Specific Shelter for Thermal Comfort Maintenance. | **Low** |
| 26052 | Hardware | Miscellaneous | DRDO | To develop an AI/ML-enabled adaptive noise cancellation (ANC) system that effectively suppresses stationary, non-stationary, and impulsive defence noises while maintaining high speech intelligibility and real-time performance on embedded hardware. | **Medium** |
| 26053 | Software | Smart Vehicles | DRDO | Adaptive Variable Resolution 2.5D Lidar Mapping for Dynamic Environment Perception | **Low** |
| 26054 | Software | Robotics and Drones | DRDO | AI-Enabled Real-Time Digital Twin System for Health Monitoring, Fault Prediction and Mission Reliability Enhancement of Aero Piston Engines used in MALE UAVs. | **Low** |
| 26055 | Software | Robotics and Drones | DRDO | Smart Scan strategy for Electronic Warfare | **Low** |
| 26057 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | AI-Powered Automated Underwater Marine Debris and Anomaly Detection System using Side-Scan Sonar Imagery | **High** |
| 26058 | Hardware | Robotics and Drones | Ministry of Earth Sciences (MoES) | Development of a Low-Power, Real-Time Adaptive Software-Defined Sonar Transmitter Payload for Autonomous Underwater Vehicles (AUVs) | **Low** |
| 26060 | Software | Smart Automation | Ministry of Earth Sciences (MoES) | Digital Platform for efficient remote management of Indian Antarctic Research Stations | **Low** |
| 26061 | Software | Clean & Green Technology | Ministry of Earth Sciences (MoES) | AI-Driven Smart Energy Management System for Polar Research Stations | **High** |
| 26062 | Software | Smart Automation | Ministry of Earth Sciences (MoES) | Integrated Polar Expedition Logistics and Asset Management System | **Low** |
| 26063 | Software | Smart Education | Ministry of Earth Sciences (MoES) | Integrated Polar Science Outreach, Knowledge Repository and Media Dissemination Portal | **High** |
| 26066 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | OceanEmbed - Satellite Embedding-Based Deep Learning Framework for Reconstruction of Subsurface Ocean Temperature from Surface Satellite Observations. | **High** |
| 26067 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | Develop a web-based interactive 3D visualization platform that integrates numerical ocean model outputs and in-situ observations. | **High** |
| 26068 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | WeatherGPT: Conversational AI for Weather Forecasting, Alerts, and Climate Information | **High** |
| 26069 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | National Weather Big Data Analytics Platform | **High** |
| 26070 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | To develop an Artificial Intelligence (AI) / Machine Learning (ML) based system for identification, classification, and prediction of different tropical cyclone patterns using multi-source satellite data. | **High** |
| 26071 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | AI/ML-Based Integrated heavy rainfall Early Warning and Inundation Prediction System using Satellite, Radar, observational Weather and numerical weather prediction model data. | **High** |
| 26072 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | AIML based Nowcasting of thunderstorm and lightning using atmospheric observation including multiple radars, satellite, lightning and model data. | **High** |
| 26073 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | AI/ML-Based Intelligent Anomaly Detection for Automatic Weather Stations (AWS) | **High** |
| 26074 | Software | Agriculture, FoodTech & Rural Development | Ministry of Earth Sciences (MoES) | Downscaling of weather forecast from Block level to Panchayat level: Inferring high-resolution plots/ data/ information from low-resolution plot /data /information /variables for agro-meteorological advisory services. | **High** |
| 26075 | Software | Smart Education | Ministry of Earth Sciences (MoES) | Participants are invited to design and develop **CAPACITY CONNECT A Digital Capacity Building and Learning Management Portal** to support organizational training, competency development, and knowledge sharing through a centralized web-based platform. | **High** |
| 26076 | Software | Smart Automation | Ministry of Earth Sciences (MoES) | Development of personalized homepage for 'Mausam' mobile application: | **High** |
| 26077 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | AI-Driven Hyper-Local Early Warning System for Severe Weather Nowcasting | **High** |
| 26078 | Software | Smart Automation | Ministry of Earth Sciences (MoES) | AI-Driven Spatio-Temporal Tracking of Extreme Weather Anomalies in Medium-Range Forecasts | **High** |
| 26079 | Software | Smart Automation | Ministry of Earth Sciences (MoES) | AI-Based Forecast Bust Detection for Medium-Range Weather Forecasts | **High** |
| 26080 | Software | Smart Automation | Ministry of Earth Sciences (MoES) | Regime-Aware AI Post-Processing of Monsoon Rainfall Forecasts | **High** |
| 26081 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | Hybrid AI–NWP Multi-Model Forecast Blending System | **High** |
| 26082 | Software | Clean & Green Technology | Ministry of Earth Sciences (MoES) | Air Pollution–Weather Coupled Forecasting System (Delhi NCR Focus) | **High** |
| 26083 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | Extreme Heatwave Early Warning and Human Thermal Stress Index | **High** |
| 26084 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | Convective scale nowcasting for Thunderstorms, Hail & Cloudbursts (06 hr) | **High** |
| 26085 | Software | Disaster Management | Ministry of Earth Sciences (MoES) | Urban Flood Nowcasting System (Drainage and Rainfall Coupling) | **High** |
| 26086 | Software | Agriculture, FoodTech & Rural Development | Ministry of Earth Sciences (MoES) | Hyperlocal Monsoon Onset & Break Prediction System (Block/Village Scale) | **High** |
| 26087 | Hardware | Smart Education | Ministry of Cooperation | AI-Enabled Cooperative Capacity Building, ERP & Employment Ecosystem | **Medium-High** |
| 26088 | Hardware | Agriculture, FoodTech & Rural Development | Ministry of Cooperation | Multilingual Cooperative Governance & Legal Assistance Chatbot | **Medium** |
| 26089 | Software | Agriculture, FoodTech & Rural Development | Ministry of Cooperation | Cooperative Gig Services Platform for Household & Community Services | **High** |
| 26090 | Software | Heritage & Culture | Ministry of Social Justice and Empowerment (MoSJE) | AI-Driven Market Linkage and Smart Cataloging Mobile Application for Marginalized Artisans | **High** |
| 26091 | Software | Agriculture, FoodTech & Rural Development | Ministry of Social Justice and Empowerment (MoSJE) | AI-Driven Hyper-Local Business Advisory and Financial Structuring Assistant for Rural Micro-Entrepreneurs | **High** |
| 26092 | Software | Smart Automation | Ministry of Social Justice and Empowerment (MoSJE) | AI-Driven Scheme Matching for Marginalized Entrepreneurs | **High** |
| 26093 | Software | MedTech / BioTech / HealthTech | Ministry of Social Justice and Empowerment (MoSJE) | AI-Based Real-Time Stress and Trauma Assessment Module for Victims/Complainants Accessing NHAA (14566) and Integrated Portal | **High** |
| 26094 | Software | MedTech / BioTech / HealthTech | Ministry of Social Justice and Empowerment (MoSJE) | AI-Powered Dynamic Mental Health Monitoring and Distress Prediction System for Victims of Atrocities | **High** |
| 26095 | Software | Smart Automation | Ministry of Social Justice and Empowerment (MoSJE) | Smart Real-Time Monitoring & Inspection Mobile App | **High** |
| 26096 | Hardware | Smart Education | Ministry of Social Justice and Empowerment (MoSJE) | Digital Heritage Archive for Memorials, Manuscripts & Ambedkar: AI-Powered Institutional Archive and Audio-Visual Knowledge Platform | **Medium** |
| 26097 | Software | Agriculture, FoodTech & Rural Development | Ministry of Social Justice and Empowerment (MoSJE) | AI-Driven voice Assistant for livelihood Mapping and NSQF-Aligned Skilling Recommendations for SC Communities under GIA component of PM-AJAY | **High** |
| 26098 | Hardware | Smart Vehicles | Ministry of Defence (MoD) | Development of a Low-Cost Precision Guidance and Smart Electronic Fuze System for a 155 mm Artillery Shell | **Low** |
| 26099 | Software | Smart Automation | Ministry of Petroleum & Natural Gas | AI-Driven Standardization and Harmonization of Material Codes Across CPSEs | **High** |
| 26100 | Software | Smart Automation | Ministry of Petroleum & Natural Gas | AI-Powered Integrated Bid Compliance Verification Platform for GeM Procurement | **High** |
| 26101 | Software | Smart Education | MoSPI | Develop an AI enabled learning platform that identifies competency gaps, recommends personalized training through integration with the iGOT Karmayogi ecosystem, and capable of generating Quizzes and Multiple choice questions (MCQs) from uploaded learning materials to strengthen capacity building in India's Official Statistical System. | **High** |
| 26102 | Software | Smart Automation | MoSPI | Development of an AI-powered system to detect anomalies, fraud, and inefficiencies in MPLAD Scheme implementation regd. | **High** |
| 26103 | Software | Smart Automation | MoSPI | Use case on web-based integrated project-monitoring platform | **High** |
| 26104 | Software | Blockchain & Cybersecurity | All India Council for Technical Education (AICTE) | AI-Powered Real-Time Detection and Prevention of Voice Cloning Impersonation Attacks | **High** |
| 26105 | Software | Blockchain & Cybersecurity | All India Council for Technical Education (AICTE) | AI-Powered Continuous Cyber Risk Quantification and Investment Optimization Platform | **High** |
| 26106 | Software | Blockchain & Cybersecurity | All India Council for Technical Education (AICTE) | AI-Powered Email Threat Detection, GeoLocation and Forensic Intelligence Platform | **High** |
| 26108 | Software | Smart Automation | Ministry of Consumer Affairs, Food & Public Distribution | AI-Powered Recommendation Engine for Identifying Applicable Indian Standards for Procurement Specifications | **High** |
| 26109 | Hardware | Agriculture, FoodTech & Rural Development | Ministry of Fisheries, Animal Husbandry & Dairying | Al-Based Predictive Modelling for Early Forecasting of Bovine Mastitis in lndian Dairy Farms | **Medium-High** |
| 26110 | Hardware | Agriculture, FoodTech & Rural Development | Ministry of Fisheries, Animal Husbandry & Dairying | Development of a Low-Cost Light-weight Milk Chilling Can for Small-Scale Dairy Farmers | **Medium** |
| 26111 | Software | Agriculture, FoodTech & Rural Development | Ministry of Fisheries, Animal Husbandry & Dairying | Smart Al-Enabled Rapid Feed and Silage Quality Testing System for Dairy Farmers | **High** |
| 26113 | Hardware | MedTech / BioTech / HealthTech | Autodesk | Human augmentation technologies are transforming healthcare,rehabilitation, industrial ergonomics, assistive living, sports, and personal mobility by improving human capabilities and enhancing quality of life. | **Medium** |
| 26114 | Software | Miscellaneous | Autodesk | Smart City Site Planning using Autodesk Forma Site Design | **High** |
| 26115 | Software | MedTech / BioTech / HealthTech | Autodesk | Design and Develop a Smart Mobile Medical-Waste Collection and Segregation System | **High** |
| 26116 | Software | Miscellaneous | Autodesk | Urban Mixed-Use Design Challenge-Design a centrally located mixed-use building in Autodesk Revit with commercial spaces (Ground + 1st floor) and residential units (up to 8 floors). 1 Level of Basement (Car Parking + EV Charging), Total (B+G+9)(Note: Plot size and all required dimensions may be assumed by students (in mm units). | **High** |
| 26118 | Hardware | Smart Automation | Mangalore Refinery and Petrochemicals Limited (MRPL) | Passive Colorimetric H2S Exposure-Dosimeter Wristband with AI-Based Quantitative Reading | **Medium** |
| 26122 | Software | Smart Automation | Oil India Limited | Intelligent Data Capture & Schedule-Linking Layer for Infrastructure Project Management: Real-Time Actual Progress Tracking (Planning-to-Execution Bridge) | **High** |
| 26124 | Software | Smart Automation | Bharat Electronics Limited | AI-Powered Mobile Urban Intelligence Platform Using Public Transport Fleet | **High** |
| 26126 | Software | Smart Automation | Bharat Electronics Limited | Vision Based Autonomous Navigation for Unmanned Ground Vehicle for Outdoor environment | **High** |
| 26127 | Software | Smart Automation | Bharat Electronics Limited | City-Wide AI Engine for Multi-Camera ANPR Trajectory Tracking and Urban Traffic Analytics | **High** |
| 26128 | Software | MedTech / BioTech / HealthTech | Government Of Maharashtra | Efficient systems for early detection,prevention,and management of livestock diseases and animal health issues | **High** |
| 26130 | Software | Miscellaneous | Government Of Maharashtra | Efficiency in streamlining industrial approvals,compliance processes,and access to government support services | **High** |
| 26131 | Software | Agriculture, FoodTech & Rural Development | Government Of Maharashtra | Early detection and management of crop diseases and pest infestations | **High** |
| 26132 | Software | Agriculture, FoodTech & Rural Development | Government Of Maharashtra | Strengthening market linkages and price discovery for farmers | **High** |
| 26133 | Software | MedTech / BioTech / HealthTech | Government Of Maharashtra | Accessibility and quality of public healthcare services,particularly in rural and underserved areas | **High** |
| 26134 | Software | Miscellaneous | Government Of Maharashtra | Challenges in aligning skill development programs with industry requirements and emerging job market demands | **High** |
| 26135 | Software | Miscellaneous | Government Of Maharashtra | Difficulties in tracking employment outcomes,skill gaps, and the impact of skilling initiatives | **High** |
| 26136 | Software | Miscellaneous | Government Of Maharashtra | Startup friendly public procurement mechanism that enables government departments to identify,pilot, procure,and scale innovative solutions from eligible startups | **High** |
| 26138 | Software | Clean & Green Technology | Egreen Quanta | Quantum-Inspired Fuel Consumption Prediction and Green Fleet Optimization | **Low** |
| 26139 | Software | MedTech / BioTech / HealthTech | Egreen Quanta | Hybrid Quantum Machine Learning Platform for Early Disease Detection | **Low** |
| 26140 | Software | Smart Education | Egreen Quanta | AI-Based Interactive Quantum Algorithm Learning Platform | **Low** |
| 26141 | Software | Blockchain & Cybersecurity | Egreen Quanta | Quantum-Inspired Cyber Threat Detection for Digital Signature Security | **Low** |
| 26142 | Software | Space Technology | National Technical Research Organisation (NTRO) | Deep Learning Based Super Resolution Mapping (SRM) from Medium Resolution Satellite Imageries | **High** |
| 26143 | Software | Disaster Management | National Technical Research Organisation (NTRO) | Leveraging satellite imagery to determine Oil spills at sea along with AIS data correlations to identify vessel responsible for the spill. | **High** |
| 26144 | Hardware | Smart Automation | National Technical Research Organisation (NTRO) | Design & Development of a High-Sensitivity Micro barometer Infrasound sensor | **Low** |
| 26145 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | AI-Based Detection of Cyber Threats in Unidirectional IP Traffic | **Low** |
| 26149 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | Design and Development of an Integrated Secure Data Erasure and Advanced File Recovery Tool for Digital Forensics and Data Sanitization | **High** |
| 26150 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | Development of a Multi-Vendor DVR/NVR Forensic Analysis Tool for Standardized Acquisition, Recovery, and Analysis of Surveillance Evidence. | **Low** |
| 26152 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | Social Media Analytics | **High** |
| 26153 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | AI based Network Attack Forecasting from Network Traffic Data | **High** |
| 26154 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | Gen AI Platform for Automated Content Transformation | **High** |
| 26155 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | AI-Driven Multi-Vendor Network Security Compliance Auditor | **High** |
| 26156 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | Universal Log Pre-processing Framework | **High** |
| 26157 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | Supervisory Analytics Tool for SOC Assessment (SAT-SA) | **High** |
| 26158 | Software | Robotics and Drones | National Technical Research Organisation (NTRO) | Single-Pass Drone Video to Accurate 3D Model Generation System | **High** |
| 26159 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | SecureMailScope: AI-Assisted Cryptographic Security Posture Assessment for Secure Email Communications | **High** |
| 26160 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | AI-Powered IPsec VPN Protocol Analyzer and Security Assessment Framework | **High** |
| 26161 | Software | Disaster Management | National Technical Research Organisation (NTRO) | Dam Break Inundation Modelling Using Hydrodynamic Modelling of any River | **High** |
| 26162 | Software | Disaster Management | National Technical Research Organisation (NTRO) | AI-Based Detection and Classification of Industrial Fires and Persistent Thermal Sources Using NASA FIRMS, OSM & Satellite Data | **High** |
| 26164 | Software | Blockchain & Cybersecurity | National Technical Research Organisation (NTRO) | Enterprise Cryptographic Discovery & Analysis Tool (ECDAT) | **Low** |
| 26165 | Software | Smart Automation | Oil India Limited | AI/NLP Engine to Detect Serious Injury & Fatality (SIF) Precursors in OIL's Unsafe-Act/Unsafe-Condition and Near-Miss Reports | **High** |
| 26167 | Software | Space Technology | Indian Space Research Organisation(ISRO) | SatQuery AI - An Interactive Vision-Language Assistant for Multimodal Remote Sensing Image Analysis through Text Queries | **High** |
| 26168 | Software | Smart Vehicles | Indian Space Research Organisation(ISRO) | AI-ML based Intelligent Dead Reckoning system for seamless navigation | **High** |
| 26169 | Software | Smart Automation | Indian Space Research Organisation(ISRO) | Development of an AI-Based Virtual Camera Tracking System for Coarse Alignment of Mobile Free Space Optical Communication (FSOC) Terminals | **High** |
| 26170 | Software | Smart Automation | Indian Space Research Organisation(ISRO) | AI-Driven Anomaly Detection in Component Burn-In & Screening | **High** |
| 26171 | Software | Smart Automation | Indian Space Research Organisation(ISRO) | On-device Visual Perception for Light-weight Browser Agents | **High** |
| 26172 | Hardware | Smart Automation | Indian Space Research Organisation(ISRO) | Low Latency and Efficient Voice Activator for Edge Devices | **Medium** |
| 26173 | Software | Smart Automation | Indian Space Research Organisation(ISRO) | iTantra -Indian Multilingual TTS & STT Aided Neural Transceiver Radio Access for low bitrate links | **High** |
| 26174 | Software | Space Technology | Indian Space Research Organisation(ISRO) | AI Human Activity Recognition for On-board BAS Experiments | **High** |
| 26175 | Software | Disaster Management | Indian Space Research Organisation(ISRO) | DepthWizard - Single-View Height Estimation and 3D Flythrough | **High** |
| 26176 | Software | Disaster Management | Indian Space Research Organisation(ISRO) | ORCA Marine EcOsystem Reasoning with Collaborative Agents | **High** |
| 26177 | Hardware | Robotics and Drones | Qualcomm Inc | A deployable AI-powered autonomous drone that aids search-and-rescue operations by detecting people and hazards, thereby improving responder safety and reducing victim discovery time. | **Medium-High** |
| 26178 | Hardware | Disaster Management | Qualcomm Inc | A resilient, AI-powered environmental monitoring network that provides early detection, localized intelligence, and actionable alerts for floods, forest fires, pollution events, and other environmental hazards common in India, enabling authorities and communities to shift from reactive disaster response to proactive risk prevention. | **Medium-High** |
| 26180 | Hardware | Agriculture, FoodTech & Rural Development | Qualcomm Inc | A field-deployable AI-powered Smart Farming Assistant that helps farmers detect crop diseases, pests, nutrient deficiencies, and irrigation needs at an early stage, while improving resilience against droughts, floods, heat waves, and other agricultural risks common in India. The solution should enable higher yields, lower input costs, more efficient water usage, and faster response to emerging threats through real-time on-device intelligence. | **Medium-High** |
| 26181 | Hardware | MedTech / BioTech / HealthTech | Qualcomm Inc | A secure, AI-powered Personal Health Companion that delivers real-time, privacy-preserving health monitoring and early warning capabilities, helping individuals recognize health risks before they become emergencies. The solution should improve resilience during heat waves, floods, pollution events, and other disasters common in India while enabling continuous health support through on-device intelligence. | **Medium-High** |
| 26182 | Software | Blockchain & Cybersecurity | Ministry of Home Affairs | Automated Attribution of Unknown Cryptocurrency Wallets to Nearest Virtual Asset Service Providers (VASPs) through Blockchain Intelligence APIs | **High** |
| 26183 | Software | Blockchain & Cybersecurity | Ministry of Home Affairs | Real-Time Identification of Fraud-Linked Cryptocurrency Exchanges from Victim-Reported Suspect Wallet Addresses through Automated Blockchain Analytics | **High** |
| 26186 | Software | MedTech / BioTech / HealthTech | Ministry of Home Affairs | AI-Based Predictive Personnel Stress and Welfare Monitoring System for Uniformed Forces | **High** |
| 26187 | Software | Blockchain & Cybersecurity | Ministry of Home Affairs | AI-Based Intelligent Video Analytics Platform for Border Surveillance using existing CCTV Infrastructure. | **High** |
| 26189 | Software | Blockchain & Cybersecurity | Ministry of Home Affairs | AI-Powered Criminal Network Analysis System | **High** |
| 26191 | Software | Disaster Management | Ministry of Home Affairs | Intelligent Identification of Hazard-Based Red Zones, Carrying Capacity Assessment, and Immediate Relocation Needs for Vulnerable Habitations | **High** |
| 26192 | Software | Disaster Management | Ministry of Home Affairs | Flash Flood Prediction System for Hilly Regions using Multi-Source Data Theme | **High** |
| 26193 | Software | Agriculture, FoodTech & Rural Development | AICTE | Student Innovation-Developing solutions, keeping in mind the need to enhance the primary sector of India - Agriculture and to manage and process our agriculture produce. | **High** |
| 26195 | Software | Clean & Green Technology | AICTE | Student Innovation-Solutions could be in the form of waste segregation, disposal, and improve sanitization system. | **High** |
| 26198 | Software | MedTech / BioTech / HealthTech | AICTE | Student Innovation-Cutting-edge technology in these sectors continues to be in demand. Recent shifts in healthcare trends, growing populations also present an array of opportunities for innovation. | **High** |
| 26200 | Software | Renewable / Sustainable Energy | AICTE | Student Innovation-Innovative ideas that help manage and generate renewable /sustainable sources more efficiently | **High** |
| 26201 | Software | Robotics and Drones | AICTE | Student Innovation-There is a need to design drones and robots that can solve some of the pressing challenges of India such as handling medical emergencies, search and rescue operations, etc. | **High** |
| 26206 | Software | Disaster Management | AICTE | Student Innovation-Disaster management includes ideas related to risk mitigation, Planning and management before, after or during a disaster. | **High** |
| 26207 | Software | Smart Education | AICTE | Student Innovation-Smart education,a concept that describes learning in digital age. It enables learners to learn more effectively, efficiently, flexibly and comfortably. | **High** |
| 26210 | Hardware | Agriculture, FoodTech & Rural Development | AICTE | Student Innovation-Developing solutions, keeping in mind the need to enhance the primary sector of India - Agriculture and to manage and process our agriculture produce. | **Medium** |
| 26212 | Hardware | Clean & Green Technology | AICTE | Student Innovation-Solutions could be in the form of waste segregation, disposal, and improve sanitization system. | **Medium** |
| 26215 | Hardware | MedTech / BioTech / HealthTech | AICTE | Student Innovation-Cutting-edge technology in these sectors continues to be in demand. Recent shifts in healthcare trends, growing populations also present an array of opportunities for innovation. | **Medium** |
| 26217 | Hardware | Renewable / Sustainable Energy | AICTE | Student Innovation-Innovative ideas that help manage and generate renewable /sustainable sources more efficiently | **Medium** |
| 26218 | Hardware | Robotics and Drones | AICTE | Student Innovation-There is a need to design drones and robots that can solve some of the pressing challenges of India such as handling medical emergencies, search and rescue operations, etc. | **Medium** |
| 26223 | Hardware | Disaster Management | AICTE | Student Innovation-Disaster management includes ideas related to risk mitigation, Planning and management before, after or during a disaster. | **Medium** |
| 26224 | Hardware | Smart Education | AICTE | Student Innovation-Smart education,a concept that describes learning in digital age. It enables learners to learn more effectively, efficiently, flexibly and comfortably. | **Medium** |


---

## 💡 General Strategy to Excel in the Internal Hackathon & Finals

To maximize your selection probability, structure your Idea PPT and development roadmap using the following guidelines:

### 1. The Ideal Team Composition
- **The UI/UX Specialist:** In hackathons, visual appeal represents 50% of the initial impression. Ensure you have one person dedicated entirely to building a gorgeous, premium frontend (Vite/React, Tailwind CSS, clean HSL colors, glassmorphism, responsive components).
- **The Backend/API Developer:** Connects database, implements business logic, and integrates external APIs (e.g., weather feeds, Bhashini translation, SMS gateways).
- **The AI/ML Engineer:** Focuses on pre-trained models, fine-tuning, or RAG setup. Note: Do not write complex model architectures from scratch during the hackathon. Use pre-trained weights (Hugging Face, TensorFlow Hub) and wrap them in FastAPI.
- **The Domain/Presenter:** One team member who deeply understands the problem statement, guidelines, and who can pitch the solution with clarity and passion. They will drive the Q&A sessions.

### 2. Crafting the Winning Idea PPT
- **Slide 1: Title & Team details** (Keep it neat, include your unique Team Name).
- **Slide 2: Problem Description** (Reframe the official problem statement. Use a user-centric story, e.g., 'Meet Ramesh, a farmer who lost 40% of his crop because...').
- **Slide 3: Proposed Solution** (List 3 core pillars of your solution. Don't be vague. Be extremely specific, e.g., 'An offline-first Android App, an AI-powered treatment recommender, and an AICTE-approved cooperative linkage dashboard').
- **Slide 4: Architecture Diagram** (A clean flow diagram showing Mobile/Web Client -> API Gateway -> ML Models & Database -> Third Party Integrations).
- **Slide 5: Technical Stack** (List modern, relevant tools. E.g., Flutter, Fastify, PyTorch, Supabase, Docker. Avoid listing outdated tech like PHP or JSP).
- **Slide 6: Use Cases & Beneficiaries** (Explicitly highlight the social impact, who benefits, and how it aligns with government initiatives).
- **Slide 7: Competitive Advantage / Innovation** (Why is your solution better than existing market apps? Highlight features like **low-bandwidth sync**, **multilingual voice assistance via Bhashini**, or **Explainable AI**).
- **Slide 8: Team Skills & Feasibility** (Prove that your team has the skills to build this in 36 hours).

### 3. Key High-Scoring Features to Include in Your Solution
- **Offline/Low-Network Support:** Essential for rural/disaster applications. Demonstrate SQLite/Hive storage syncing with the cloud once network is restored.
- **Multilingual Support:** Integrate the Bhashini API or Hugging Face translation models so users in the North East or rural areas can interact in their mother tongue.
- **Role-Based Dashboards:** Ensure there is an interface for the general public (citizens/farmers/patients) and a separate command dashboard for government administrators/doctors/caregivers.
