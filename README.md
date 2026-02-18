# 🌐 TransLingua - AI-Powered Language Translator

A modern, AI-powered translation application built with Streamlit and Google's Gemini API. Translate text between multiple languages instantly with a beautiful, user-friendly interface.

![TransLingua](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Google Gemini](https://img.shields.io/badge/Google%20Gemini-4285F4?style=for-the-badge&logo=google&logoColor=white)

## ✨ Features

- 🚀 **Fast AI Translation** - Powered by Google's Gemini 2.5 Flash model
- 🌍 **16+ Languages** - Support for major world languages
- 💡 **Smart Model Selection** - Automatically selects the best available model
- 📱 **Responsive Design** - Works on desktop and mobile
- 🎨 **Modern UI** - Clean, gradient-based interface
- 📋 **Easy Copy** - One-click copy of translated text
- 🔒 **Secure** - API keys stored securely in Streamlit secrets

## 🌍 Supported Languages

- English
- Spanish
- French
- German
- Chinese
- Hindi
- Japanese
- Korean
- Portuguese
- Italian
- Russian
- Arabic
- Dutch
- Turkish
- Polish
- Vietnamese

## 🚀 Quick Start

### Prerequisites

- Python 3.10 or higher
- Google Gemini API key ([Get one here](https://aistudio.google.com/apikey))

### Local Installation

1. **Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/translingua-ai-translator.git
cd translingua-ai-translator/translingua-ai-studio-main
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Set up your API key**

Create a `.streamlit/secrets.toml` file:
```toml
GEMINI_API_KEY = "your_api_key_here"
```

4. **Run the app**
```bash
streamlit run streamlit_app.py
```

The app will open in your browser at `http://localhost:8501`

## ☁️ Deploy to Streamlit Cloud

### Step 1: Push to GitHub

```bash
git add .
git commit -m "Initial commit"
git push origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Select your repository
4. Set main file path: `translingua-ai-studio-main/streamlit_app.py`
5. Click **"Advanced settings"**
6. Add your API key in **Secrets**:
```toml
GEMINI_API_KEY = "your_api_key_here"
```
7. Click **"Deploy"**

Your app will be live at: `https://your-app-name.streamlit.app`

## 📁 Project Structure

```
translingua-ai-studio-main/
├── streamlit_app.py          # Main application file
├── requirements.txt          # Python dependencies
├── .streamlit/
│   └── secrets.toml         # API key (local only, not committed)
├── .gitignore               # Git ignore file
└── README.md                # This file
```

## 🔧 Configuration

### API Key Setup

Get your free API key from [Google AI Studio](https://aistudio.google.com/apikey):

1. Sign in with your Google account
2. Click "Create API key"
3. Copy the key
4. Add it to your secrets (see Quick Start above)

### Rate Limits

Free tier limits:
- **20 requests per day** per model
- Multiple models available (automatic fallback)
- Upgrade for higher limits at [Google AI Pricing](https://ai.google.dev/pricing)

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web framework
- **[Google Gemini API](https://ai.google.dev/)** - AI translation
- **Python 3.10+** - Programming language

## 📝 Usage

1. Enter or paste text in the input box
2. Select source language
3. Select target language
4. Click **"Translate"**
5. Copy the translated text

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Google Gemini API for powerful AI translation
- Streamlit for the amazing web framework
- All contributors and users of this project

## 📧 Contact

For questions or support, please open an issue on GitHub.

## 🌟 Star History

If you find this project useful, please consider giving it a star ⭐

---

**Made with ❤️ using Streamlit and Google Gemini AI**

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://your-app-url.streamlit.app)
