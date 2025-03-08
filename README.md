# SDNET2018 Concrete Crack Detection
## Overview
This repository contains an implementation of concrete crack detection using the **SDNET2018 dataset**, which includes over **56,000 images** of cracked and non-cracked concrete surfaces, such as bridge decks, walls, and pavements. The dataset is designed for training, validation, and benchmarking of AI-based crack detection algorithms, particularly focusing on **deep learning convolutional neural networks (CNNs)** for structural health monitoring.

https://drive.google.com/file/d/1aFsB1_5N8DHtc2q6gLPVwvO9wxf4rk5W/view?usp=sharing

## Dataset Description
- **Total Images:** 230 high-resolution images segmented into 256x256 px sub-images.
- **Categories:**
    * Bridge Decks: 54 images
    * Walls: 72 images
    * Pavements: 104 images
- **Labeling:**
  * Each sub-image is labeled as **'Cracked'** or **'Non-cracked'** based on the presence of cracks.
  * Crack Size Range: From as narrow as **0.06 mm** to as wide as **25 mm.**
  * **Challenges:** Dataset includes images with shadows, surface roughness, edges, holes, and background debris.

## Data Collection
**Equipment:** Captured using a 16 MP Nikon digital camera.
**Locations:**
**Bridge Decks:** SMASH laboratory, Utah State University.
**Walls:** Russell/Wanlass Performance Hall, USU campus.
**Pavements:** Roads and sidewalks on the USU campus.

## Purpose
The dataset serves as a benchmark for developing and evaluating crack detection algorithms using deep learning techniques, aiding in the advancement of **structural health monitoring systems.**

📋 Table of Contents
* Overview
* Features
* Installation
* Usage
* Configuration
* Prompt Design
* Technologies Used
* Contributing

## 🛠️ Overview
This prototype demonstrates an AI-powered system for detecting and analyzing construction defects using the Gemini API and Streamlit. It can automatically identify structural issues in concrete surfaces, provide severity levels, possible causes, and suggest rectification steps.

## 🚀 Features
* **Defect Detection:** Identifies cracks, damage, holes, and bends with probability levels.
* **Severity Assessment:** Classifies defects as minor, moderate, or severe.
* **Root Cause Analysis:** Considers material properties, environmental factors, and construction practices.
* **Recommendations:** Provides solutions and rectification steps.
* **Integration Ready:** Designed for mobile apps and database integration in a production environment.

🖥️ Installation
To run the project locally, follow these steps:

1. **Clone the repository:**

- `git clone https://github.com/your-username/construction-defect-detection.git`
- `cd construction-defect-detection`

2. **Create and activate a virtual environment:**
- `python -m venv .venv`
- `.venv\Scripts\activate`  # On Windows
- `source .venv/bin/activate`  # On Linux/Mac

3. **Install required packages:**
- `pip install -r requirements.txt`

4. **Create a .env file for API Key:**
- `GOOGLE-API=your_google_api_key_here`

## 🛠️ Usage
Run the application using Streamlit:
- `streamlit run app.py`

5. **Upload an Image**
- Upload a construction image (JPG, JPEG, PNG) from the sidebar.
- Click "Analyze for Defects" to get a detailed report.

## ⚙️ Configuration
- `.env file setup:`

## 📋 Prompt Design
The prompt provided to the Gemini API includes:

- Defect Detection: Identifies structural defects like cracks, damage, or bends.
- Severity Level: Assesses the defect's severity (minor, moderate, severe).
- Root Cause Analysis: Suggests possible causes based on material properties and environmental factors.
- Recommendations: Advises on rectification steps and materials.
- Compliance Check: Verifies if the defect violates any relevant building codes.

## 🛠️ Technologies Used
- **Python:** Core programming language.
- **Streamlit:** Web framework for deploying machine learning models.
- **PIL:** For image handling.
- **dotenv:** For managing API keys securely.

## 🤝 Contributing
- Contributions, issues, and feature requests are welcome!
- Feel free to fork the repository and submit pull requests.

## 📜 License

This project is open-source and available under the MIT License.







