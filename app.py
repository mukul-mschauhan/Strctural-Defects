from PIL import Image
from dotenv import load_dotenv
load_dotenv()
import streamlit as st
import google.generativeai as genai
import os
import textwrap
import pathlib

genai.configure(api_key=os.getenv("GOOGLE-API"))
prompt = '''
Act as a Structural & Civil Engineer & Generate Bullet Point Answer in Crisp One to 2 Line Max.
Based on the provided image, find the answers to the following:-
1. Is there a structural defect (such as a crack, damage, hole, bend) visible in the image. Give the probability of the defect in Percentage
2. What is the severity level of the defect (minor, moderate, severe) and what is the likelihood (in percentage) that this is a structural defect?
3. What are the possible causes of the defect, considering material properties, environmental factors, and construction practices?
4. Under what conditions (environment & mechanical impact) will the crack propagate further in terms of length, width, and depth?
5. If a different grade of concrete were used, which properties (e.g., compressive strength, tensile strength, shrinkage) would be most relevant in mitigating the crack?
6. How would rebar placement (e.g., spacing, diameter, location) influence the crack propagation and structural integrity?
7. What is the estimated reduction in the safe live load capacity due to the presence of these cracks? What are the safety implications for the structure's intended use?
8. What are the recommended steps for rectifying these cracks, including material selection and application techniques? What is the recommended gauging area for the rectification process?
9. What specific criteria (e.g., crack width, depth, pattern, location) would necessitate the rejection of the slab?
10. Is a dehumidifier required during the rectification process?
11. Would non-destructive testing (NDT) methods be beneficial in further assessing the crack and the overall structural integrity?
12. Is long-term monitoring of the crack and the structure recommended?
13. Does the observed crack violate any relevant building codes or industry standards? 
'''

def get_gemini_response(input,image):
    model = genai.GenerativeModel('gemini-1.5-flash')
    if input!="":
        response = model.generate_content([input,image])
    else:
        response = model.generate_content(image)
    return response.text

# Design the Page
# Header
st.header("🏗️:blue[Construction Defect] Detection System")
st.subheader(":orange[Prototype for Automated Defect Analysis]", divider = True)
with st.expander("About this Application"):
        st.markdown("""
        This prototype demonstrates an AI-powered system for detecting and analyzing construction defects. The key features include:
        - **Defect Detection**: Automatically identifies common construction defects like cracks, misalignments, and welding issues
        - **Solution Recommendations**: Provides recommended solutions based on the detected defect type
        - **Report Generation**: Creates detailed PDF reports for documentation and communication
        
        In a production environment, this system would be:
        - Integrated with a mobile app for on-site inspections
        - Connected to a database for tracking defects and remediation history
        - Trained on your company's specific construction defect images""")


# Display instructions when no image is uploaded
#st.markdown("""<div style="text-align: center; padding: 2rem;">
#            <img src="https://cdn-icons-png.flaticon.com/512/4492/4492182.png" width="100">
#            <h3>No Image Selected</h3>
#            <p>Please upload a construction image or select a sample image from the sidebar to begin analysis.</p>
#            </div>""", unsafe_allow_html=True)

# Sidebar
st.sidebar.title("Upload Construction Image")
uploaded_file = st.sidebar.file_uploader(label = "Upload the Image", type=["jpg", "jpeg", "png"])

img=""  
if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.sidebar.image(img, caption="Uploaded Image", use_container_width=True)

analyze_button = st.sidebar.button("Analyze for Defects")

# Modelling
if analyze_button:
    response = get_gemini_response(prompt, img)
    st.subheader("The :orange[Response] is: ")
    st.write(response)
    
# Footer
st.markdown("""
            <div style="text-align: center; margin-top: 2rem; padding-top: 1rem; border-top: 1px solid #eee;">
            <p>Construction Defect Detection System - Prototype Version 1.0</p>
            </div>""", unsafe_allow_html=True)