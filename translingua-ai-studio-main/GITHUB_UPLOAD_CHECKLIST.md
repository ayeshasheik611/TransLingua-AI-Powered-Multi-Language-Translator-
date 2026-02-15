# GitHub Upload Checklist for Streamlit Deployment

## ✅ REQUIRED FILES (Must Upload)

These are the ONLY files you need for Streamlit deployment:

```
translingua-ai-studio-main/
├── streamlit_app.py              ✅ REQUIRED - Main application file
├── requirements-streamlit.txt    ✅ REQUIRED - Python dependencies
├── .gitignore                    ✅ REQUIRED - Prevents uploading secrets
├── README.md                     ✅ RECOMMENDED - Project description
├── DEPLOYMENT_GUIDE.md           ✅ RECOMMENDED - Deployment instructions
└── STREAMLIT_README.md           ✅ RECOMMENDED - Streamlit-specific docs
```

## ❌ DO NOT UPLOAD (Excluded by .gitignore)

These files contain secrets and should NEVER be uploaded:

```
❌ .streamlit/secrets.toml        - Contains your API key
❌ backend/.env                   - Contains your API key
❌ .env                           - Any environment files
```

## 📦 Optional Files (Not Needed for Streamlit)

These are for the React frontend - you don't need them for Streamlit deployment:

```
⚪ src/                           - React source code (not needed)
⚪ public/                        - React public files (not needed)
⚪ node_modules/                  - Node packages (not needed)
⚪ backend/app.py                 - Flask backend (not needed)
⚪ package.json                   - Node config (not needed)
⚪ vite.config.ts                 - Vite config (not needed)
⚪ All other React/Node files     - Not needed for Streamlit
```

---

## 🚀 Quick Upload Steps

### Option 1: Using GitHub Desktop (Easiest)

1. Download GitHub Desktop: https://desktop.github.com/
2. Open GitHub Desktop
3. Click "Add" → "Add Existing Repository"
4. Select the `translingua-ai-studio-main` folder
5. Click "Publish repository"
6. Uncheck "Keep this code private" (or keep it private if you prefer)
7. Click "Publish Repository"

### Option 2: Using Git Command Line

```bash
cd translingua-ai-studio-main

# Initialize git
git init

# Add all files (secrets are automatically excluded by .gitignore)
git add .

# Commit
git commit -m "Initial commit - TransLingua Streamlit App"

# Create repository on GitHub first, then:
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

### Option 3: Using GitHub Web Interface (Manual Upload)

1. Go to https://github.com/new
2. Create a new repository
3. Click "uploading an existing file"
4. Drag and drop these files:
   - `streamlit_app.py`
   - `requirements-streamlit.txt`
   - `.gitignore`
   - `README.md`
   - `DEPLOYMENT_GUIDE.md`
   - `STREAMLIT_README.md`
5. Click "Commit changes"

---

## ⚠️ IMPORTANT: Verify Before Uploading

Run this command to check what will be uploaded:

```bash
cd translingua-ai-studio-main
git status
```

Make sure you DON'T see:
- `.streamlit/secrets.toml`
- `backend/.env`
- `.env`

If you see these files, they will be uploaded! Stop and check your `.gitignore` file.

---

## 🔐 After Uploading to GitHub

1. Go to https://share.streamlit.io/
2. Click "New app"
3. Select your repository
4. Set main file: `streamlit_app.py`
5. Click "Advanced settings"
6. Add to Secrets:
```toml
GEMINI_API_KEY = "AIzaSyBXjnBGZTVIA2Z0hQxyAZFo2pZj4VEpU4c"
```
7. Click "Deploy"

Your app will be live at: `https://your-app-name.streamlit.app`

---

## 📋 Summary

**Minimum files needed:**
1. `streamlit_app.py` - The main app
2. `requirements-streamlit.txt` - Dependencies
3. `.gitignore` - Security

**That's it!** Everything else is optional.
