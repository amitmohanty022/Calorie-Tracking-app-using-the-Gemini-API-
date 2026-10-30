# Calorie Tracking App (Gemini Vision)

Upload a photo of your meal and the app lists each food item, its calories, the total, and whether the meal is healthy. Built with Streamlit and Google Gemini.

## How to run (step by step)

You need **Python 3.10 or newer** ([download](https://www.python.org/downloads/)).

**1. Download the project**

```bash
git clone https://github.com/amitmohanty022/Calorie-Tracking-app-using-the-Gemini-API-.git
cd Calorie-Tracking-app-using-the-Gemini-API-
```

**2. Create a virtual environment and activate it**

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate
```

**3. Install the requirements**

```bash
pip install -r requirements.txt
```

**4. Add your Gemini API key**

- Get a free key at https://aistudio.google.com/apikey
- Copy `.env.example` to a new file named `.env`
  - Windows: `copy .env.example .env`
  - macOS / Linux: `cp .env.example .env`
- Open `.env` and paste your key after `GOOGLE_API_KEY=`

**5. Start the app**

```bash
streamlit run app.py
```

Your browser opens at http://localhost:8501.

**6. Use it**

1. Upload a JPG or PNG photo of food.
2. Optionally type extra context in "Input Prompt" (for example "this is a large portion").
3. Click **Tell me the total calories**.

## How it works

1. The uploaded image and an instruction prompt are sent to the Gemini model (`gemini-3.8-flash` by default).
2. Gemini identifies the food items and estimates calories for each.
3. The app shows the breakdown, the total, and a short health note.

To use a different Gemini model, set `GEMINI_MODEL` in `.env`.

## Troubleshooting

| Problem | Fix |
|---|---|
| "GOOGLE_API_KEY is not set" | Make sure the file is named exactly `.env` (not `.env.txt`) and is in the project folder. |
| `streamlit: command not found` | Activate the virtual environment (step 2) first. |
| `404 model not found` | Your key may not have access to that model. Set `GEMINI_MODEL=gemini-3.6-flash` in `.env`. |
