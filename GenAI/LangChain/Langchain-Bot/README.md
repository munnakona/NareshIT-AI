# KonaGPT (LangChain + Gemini Streamlit Bot)

KonaGPT is a lightweight Streamlit chatbot built with **LangChain** and **Google Gemini**. It uses a simple prompt template and chains the model response to a Streamlit UI for interactive Q&A.

## Features
- Streamlit web UI for live chat
- LangChain prompt + output parser pipeline
- Google Gemini (gemini-2.5-flash) model integration
- Optional LangSmith tracing via environment variables

## Project Structure
```
Langchain-Bot/
├─ konagpt.py          # Streamlit app
├─ .env                # Local environment variables (not for git)
└─ README.md
```

## Prerequisites
- Python 3.9+
- A Google Generative AI API key (Gemini)
- (Optional) LangSmith API key for tracing

## Setup
1. **Create and activate a virtual environment** (recommended).
2. **Install dependencies**:
   ```bash
   pip install streamlit langchain langchain-google-genai python-dotenv
   ```
3. **Create a `.env` file** in `LangChain/Langchain-Bot/`:
   ```env
   GOOGLE_API_KEY=**
   LANGSMITH_TRACING=true
   LANGSMITH_ENDPOINT=https://api.smith.langchain.com
   LANGSMITH_API_KEY=**
   LANGSMITH_PROJECT=KonaGPT
   ```

## Run the App
From the `LangChain/Langchain-Bot/` directory:
```bash
streamlit run konagpt.py
```

Then open the local URL shown in your terminal.

## Notes
- Do **not** commit `.env` files or API keys to git.
- You can customize the prompt template in `konagpt.py`.
- Model used: `gemini-2.5-flash` (you can swap with another Gemini model).

## License
This project is for learning/demo purposes.