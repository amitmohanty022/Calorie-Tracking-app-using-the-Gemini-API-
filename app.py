import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()

API_KEY = os.getenv("GOOGLE_API_KEY")
MODEL = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")

st.set_page_config(page_title="Gemini Health App")
st.header("Gemini Health App")

if not API_KEY:
    st.error("GOOGLE_API_KEY is not set. Copy .env.example to .env and paste your Gemini API key.")
    st.stop()

client = genai.Client(api_key=API_KEY)


def get_gemini_response(instructions, uploaded_file, user_prompt):
    image_part = types.Part.from_bytes(data=uploaded_file.getvalue(), mime_type=uploaded_file.type)
    contents = [instructions, image_part]
    if user_prompt:
        contents.append(user_prompt)
    response = client.models.generate_content(model=MODEL, contents=contents)
    return response.text


user_input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", width="stretch")

submit = st.button("Tell me the total calories")

input_prompt = """
You are an expert in nutritionist where you need to see the food items from the image and calculate the total calories,also provide the details of every food items with calories intakein the below format
                1.Item 1 - no of calories
                2.Item 2 - no of calories
                ----
                ----
        Finally you can also mention whether the food is healthy or not

"""

if submit:
    if uploaded_file is None:
        st.warning("Please upload a food image first.")
    else:
        with st.spinner("Analyzing..."):
            response = get_gemini_response(input_prompt, uploaded_file, user_input)
        st.header("The Response is")
        st.write(response)
