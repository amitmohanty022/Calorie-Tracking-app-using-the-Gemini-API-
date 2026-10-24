import os

import streamlit as st
from dotenv import load_dotenv
from google import genai
from google.genai import types
from PIL import Image

load_dotenv()


def get_api_key():
    """Read the Gemini API key from Streamlit secrets or the environment."""
    try:
        if "GOOGLE_API_KEY" in st.secrets:
            return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        pass
    return os.getenv("GOOGLE_API_KEY")


MODEL_NAME = os.getenv("GEMINI_MODEL", "gemini-3.8-flash")


def get_gemini_response(input_prompt, image_parts, user_prompt):
    client = genai.Client(api_key=get_api_key())
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=[input_prompt, image_parts[0], user_prompt],
    )
    return response.text


def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        return [types.Part.from_bytes(data=bytes_data, mime_type=uploaded_file.type)]
    raise FileNotFoundError("No file uploaded")


### STREAMLIT APP

st.set_page_config(page_title="Gemini Health App")

st.header("Gemini Health App")
input = st.text_input("Input Prompt: ", key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image = ""
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
    if not get_api_key():
        st.error("GOOGLE_API_KEY is not set. Add it to a .env file or to Streamlit secrets.")
    elif uploaded_file is None:
        st.warning("Please upload an image of your meal first.")
    else:
        image_data = input_image_setup(uploaded_file)
        response = get_gemini_response(input_prompt, image_data, input)
        st.header("The Response is")
        st.write(response)
