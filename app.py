import os

import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from PIL import Image

load_dotenv()


genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))

def get_gemini_response(input_prompt,image):
    model=genai.GenerativeModel(model_name='gemini-1.5-flash')
    response=model.generate_content([input_prompt,image])
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data=uploaded_file.getvalue()
        image_parts = {
            "mime_type": uploaded_file.type,
            "data": bytes_data
        }
        return image_parts
    else:
        raise FileNotFoundError("No File Uploaded")
    
    
st.set_page_config(page_title='ATS Resume Expert')

st.subheader('Calories Advisor APP')
uploaded_file=st.file_uploader('Choose An Image:',type=['jpg','jpeg','png'])
image=""
if uploaded_file is not None:
    image=Image.open(uploaded_file)
    st.image(image,caption="Uploaded Image",use_container_width=True)
submit=st.button('Tell me about the total calories')
    
    
input_prompt = '''
You are a world-class nutritionist and food analysis expert.

Your task is to look at the given image and **identify every food item clearly** from it. Based on typical portion sizes and visual estimation, you MUST provide an approximate total calorie count for the entire meal, and break it down by each food item.

Respond in the following clear format:

1. Food Item 1 – Approx. ___ calories  
2. Food Item 2 – Approx. ___ calories  
...  
...  
N. Food Item N – Approx. ___ calories

Then calculate and mention the **total calories**.

After that, provide a **macronutrient breakdown** as a percentage split of:
- Carbohydrates
- Fats
- Proteins
- Fiber
- Sugar

Finally, give a clear, confident conclusion about whether the meal is healthy overall or not, with specific reasoning.

Important: You are required to make a full assumption-based judgment based on the image. Avoid saying “it’s not possible” or “hard to tell” — this is a visual estimation task and you must do your best with the image provided.

Only return the formatted, confident answer.
'''

if submit:
    image_data=input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data)
    st.header("The Response is...")
    st.write(response)