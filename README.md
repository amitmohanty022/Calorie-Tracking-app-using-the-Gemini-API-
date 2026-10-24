# Calorie Tracker with Gemini Vision

Upload a photo of your meal and the app uses Google Gemini's vision capability to identify each food item, estimate its calories, total them up, and say whether the meal is healthy.

## 🔗 Live demo

Not hosted yet. Deploy it for free on Streamlit Community Cloud: click the badge (or go to https://share.streamlit.io → **Create app**) and use repository `amitmohanty022/Calorie-Tracking-app-using-the-Gemini-API-`, branch `main`, main file `app.py`.

[![Deploy on Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/deploy?repository=amitmohanty022/Calorie-Tracking-app-using-the-Gemini-API-&branch=main&mainModule=app.py)

On the Streamlit deploy page, add `GOOGLE_API_KEY` under **Advanced settings → Secrets**.

## Features

- Upload a JPG/PNG photo of a meal
- Optional text prompt to add context (portion size, ingredients)
- Per-item calorie breakdown, total calories and a healthiness verdict

## Tech stack

Python, Streamlit, Google Gen AI SDK (`google-genai`), Gemini 3.8 Flash, Pillow

## Run locally

```bash
git clone https://github.com/amitmohanty022/Calorie-Tracking-app-using-the-Gemini-API-.git
cd Calorie-Tracking-app-using-the-Gemini-API-
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (or add the same keys to **Streamlit secrets** when deploying):

```env
GOOGLE_API_KEY=your_gemini_api_key   # get one at https://aistudio.google.com/apikey
# optional, defaults to gemini-3.8-flash
GEMINI_MODEL=gemini-3.8-flash
```

Then start the app:

```bash
streamlit run app.py
```

## Author

**Amit Kumar Mohanty** · [GitHub](https://github.com/amitmohanty022) · [LinkedIn](https://www.linkedin.com/in/amitkrmohanty/)
