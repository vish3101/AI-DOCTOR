#  AI Doctor – Food Image Calorie & Nutrition Analyzer

**AI Doctor** is a simple yet powerful end-to-end AI application that lets users upload an image of their food, which is then analyzed using **Google's Gemini Vision model**. The model identifies the food items, estimates calories, breaks down key nutrients, and even offers healthy suggestions or alternatives.

Despite its simplicity, this project effectively combines GenAI's vision capabilities with real-world health utility.

---

##  Features

- Upload a food image and get instant AI-powered analysis.
- Outputs:
  - Estimated **calories**.
  - Key **nutritional breakdown** (carbs, fats, protein, etc.).
  - Suggestions for a **healthier diet** if needed.
- Uses **Gemini 1.5 Flash Vision Model** to understand and describe food items.

---

##  Technologies Used

- `streamlit` – for building a simple and interactive UI.
- `python-dotenv` – to securely manage your API key.
- `google-generativeai` – to interact with Gemini Vision model.

---

##  Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd ai-doctor
```

### 2. Create a Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install streamlit python-dotenv google-generativeai
```

### 4. Set up the `.env` File

Create a `.env` file in the root directory and add your Gemini API key like this:

```
GOOGLE_API_KEY=your_google_generativeai_api_key
```

> **Note:** Do not share or commit this key publicly.

---

## Run the App

```bash
streamlit run app.py
```

---

##  File Structure

```
ai-doctor/
├── app.py           # Main Streamlit application
├── .env             # Contains the API key
└── README.md        # Project overview
```

---

## Why It Matters

This project shows how simple GenAI-powered tools can be highly effective in everyday use-cases like dietary awareness. With just a photo, users can get meaningful nutritional feedback — encouraging better health choices.

---
