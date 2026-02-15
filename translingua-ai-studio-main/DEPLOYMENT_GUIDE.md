# TransLingua - Complete Deployment Guide

## Method 1: Local Development with Streamlit Secrets

### Step 1: Your API key is already configured!
I've created `.streamlit/secrets.toml` with your API key.

### Step 2: Run the app
```bash
streamlit run streamlit_app.py
```

The app will automatically use the API key from `.streamlit/secrets.toml`

---

## Method 2: Deploy to Streamlit Cloud (FREE)

### Step 1: Push to GitHub

1. Initialize git (if not already done):
```bash
cd translingua-ai-studio-main
git init
git add .
git commit -m "Initial commit"
```

2. Create a new repository on GitHub (https://github.com/new)

3. Push your code:
```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Streamlit Cloud

1. Go to https://share.streamlit.io/

2. Click "New app"

3. Connect your GitHub account (if not already connected)

4. Select your repository

5. Set the following:
   - **Main file path**: `streamlit_app.py`
   - **Python version**: 3.10 or higher

6. Click "Advanced settings"

7. In the "Secrets" section, add:
```toml
GEMINI_API_KEY = "AIzaSyBXjnBGZTVIA2Z0hQxyAZFo2pZj4VEpU4c"
```

8. Click "Deploy!"

### Step 3: Wait for deployment
Your app will be live at: `https://YOUR_APP_NAME.streamlit.app`

---

## Visual Guide for Adding Secrets on Streamlit Cloud

When you're on the deployment page:

1. **Click "Advanced settings"** (bottom left)

2. You'll see a text box labeled **"Secrets"**

3. **Copy and paste this exactly**:
```toml
GEMINI_API_KEY = "AIzaSyBXjnBGZTVIA2Z0hQxyAZFo2pZj4VEpU4c"
```

4. **Click "Save"**

5. **Click "Deploy"**

---

## Method 3: Using Environment Variables (Alternative)

If you prefer using `.env` file instead of secrets:

1. Make sure `backend/.env` exists with:
```
GEMINI_API_KEY=AIzaSyBXjnBGZTVIA2Z0hQxyAZFo2pZj4VEpU4c
```

2. Run:
```bash
streamlit run streamlit_app.py
```

The app will automatically detect and use the `.env` file.

---

## Troubleshooting

### Error: "GEMINI_API_KEY not found"

**Solution 1 (Local):**
- Check if `.streamlit/secrets.toml` exists
- Make sure it contains: `GEMINI_API_KEY = "your_key_here"`

**Solution 2 (Streamlit Cloud):**
- Go to your app settings
- Click "Secrets" in the left menu
- Add your API key in TOML format
- Click "Save"
- Reboot the app

### Error: "404 models/gemini not found"

**Solution:**
- Your API key might be invalid
- Get a new key from: https://makersuite.google.com/app/apikey
- Update the key in secrets.toml or Streamlit Cloud secrets

---

## File Structure

```
translingua-ai-studio-main/
├── streamlit_app.py              # Main Streamlit app (THIS IS THE MAIN FILE)
├── requirements-streamlit.txt    # Python dependencies
├── .streamlit/
│   └── secrets.toml             # Local secrets (DO NOT COMMIT)
├── backend/
│   └── .env                     # Alternative: Environment variables
└── DEPLOYMENT_GUIDE.md          # This file
```

---

## Quick Start Commands

```bash
# Install dependencies
pip install -r requirements-streamlit.txt

# Run locally
streamlit run streamlit_app.py

# The app will open at http://localhost:8501
```

---

## Important Notes

⚠️ **Never commit secrets to Git!**
- `.streamlit/secrets.toml` is in `.gitignore`
- `backend/.env` is in `.gitignore`

✅ **For Streamlit Cloud deployment:**
- Use the Secrets management in the dashboard
- Don't include secrets in your repository

🔒 **Keep your API key secure:**
- Don't share it publicly
- Regenerate if exposed
- Use environment variables in production
