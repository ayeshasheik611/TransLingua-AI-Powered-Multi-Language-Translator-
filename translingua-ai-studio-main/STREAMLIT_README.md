# TransLingua - Streamlit Deployment

This is the Streamlit version of the TransLingua AI translation application.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements-streamlit.txt
```

### 2. Configure API Key

Make sure you have your Gemini API key in `backend/.env`:

```
GEMINI_API_KEY=your_api_key_here
```

### 3. Run the Application

```bash
streamlit run streamlit_app.py
```

The application will open in your browser at `http://localhost:8501`

## Deployment Options

### Deploy to Streamlit Cloud

1. Push your code to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io)
3. Connect your GitHub repository
4. Set the main file path to: `streamlit_app.py`
5. Add your `GEMINI_API_KEY` in the Secrets section:
   ```toml
   GEMINI_API_KEY = "your_api_key_here"
   ```
6. Click Deploy!

### Deploy to Other Platforms

You can also deploy to:
- **Heroku**: Use the Procfile method
- **Railway**: Connect your GitHub repo
- **Google Cloud Run**: Containerize with Docker
- **AWS EC2**: Run on a virtual machine

## Features

- Real-time AI translation using Google Gemini
- Support for 16+ languages
- Clean and intuitive UI
- Character count (max 5000)
- Copy translated text
- Swap languages with one click
- Responsive design

## File Structure

```
translingua-ai-studio-main/
├── streamlit_app.py          # Main Streamlit application
├── requirements-streamlit.txt # Python dependencies for Streamlit
├── backend/
│   └── .env                  # API key configuration
└── STREAMLIT_README.md       # This file
```
