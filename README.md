
# 🔐 ShadowKey

**ShadowKey** is a hacker-styled password security toolkit built with Streamlit that helps users check the strength of their passwords, estimate how long they'd take to crack, and generate strong, secure passwords with customizable options.

Built with Python + Streamlit and designed for both desktop and mobile browsers.

---

## 🌐 Streamlit Cloud Deployment

[![Deploy to Streamlit Cloud](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/)

### Deploy to Streamlit Cloud:

1. Fork this repository
2. Go to [Streamlit Cloud](https://share.streamlit.io/)
3. Click "New app" and connect your GitHub account
4. Select your forked repository
5. Set the main file path to `streamlit_app.py`
6. Click "Deploy!"

---

## 🚀 Features

- ✅ **Password Strength Checker** with real-time analysis
- ✅ **Complexity Breakdown** (uppercase, lowercase, digits, symbols, length)  
- ✅ **Estimated Time to Crack** (based on brute-force attack)  
- ✅ **Password Generator** with custom options:
  - Length slider (4-64 characters)
  - Include uppercase, lowercase, digits, and/or symbols
  - Guarantees inclusion of all selected types
- ✅ **Copy to clipboard** functionality
- ✅ **Responsive UI** with hacker-styled dark theme
- ✅ **Interactive sidebar** with security tips and information

---

## 🧪 Live Demo

🌐 **Flask Version**: [Check out ShadowKey live on Render](https://shadowkey-yz4y.onrender.com)

🌐 **Streamlit Version**: Deploy to Streamlit Cloud using the button above!

---

## 📸 Screenshots

### Original Flask Version
![ShadowKey Web App Screenshot](https://your-screenshot-link.com)

### New Streamlit Version
> Screenshots of the modern Streamlit interface coming soon!

### Original Flask Version Screenshots
<img width="1450" height="774" alt="ShadowKey Flask Interface" src="https://github.com/user-attachments/assets/1105dcee-4711-4e32-804a-ccb1586ab02f" />

<img width="1399" height="480" alt="ShadowKey Password Generator" src="https://github.com/user-attachments/assets/2b8acd2a-6da8-46ee-86ac-7a35ae17f10f" />

---

## 🛠️ Tech Stack

| Tech       | Purpose              |
|------------|----------------------|
| Python     | Backend logic        |
| Streamlit  | Modern web framework |
| HTML/CSS   | Custom styling       |
| JavaScript | UI interactions      |

---

## 📦 How to Run Locally

1. **Clone the repository**  
```bash
git clone https://github.com/ubiiii/shadowkey.git
cd shadowkey
```

2. **Create virtual environment (optional but recommended)**  
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Install dependencies**  
```bash
pip install -r requirements.txt
```

4. **Run the Streamlit app**  
```bash
streamlit run streamlit_app.py
```

5. Visit [http://localhost:8501](http://localhost:8501) in your browser 🎉

---

## 📂 Project Structure

```
shadowkey/
├── streamlit_app.py     # Main Streamlit application
├── shadowkey.py         # CLI version (legacy)
├── utils.py             # Utility functions
├── requirements.txt     # Dependencies
├── render.yaml          # Render deployment config
├── .streamlit/
│   └── config.toml      # Streamlit configuration
├── templates/           # Original Flask templates (legacy)
│   └── index.html       # Flask Web UI
└── static/              # Original Flask static files (legacy)
```

---

## 🚀 Deployment Options

### Streamlit Cloud (Recommended)
- Free hosting for public repositories
- Automatic deployments from GitHub
- Built-in HTTPS and custom domains

### Other Platforms
- **Heroku**: Add `Procfile` with `web: streamlit run streamlit_app.py --server.port=$PORT --server.address=0.0.0.0`
- **Railway**: Direct deployment from GitHub
- **Render**: Web service deployment
- **Docker**: Use `streamlit` base image

---

## 🧠 Future Ideas

- 🔒 Integration with HaveIBeenPwned API
- 🎨 Theme toggling (dark/light)
- 📊 Entropy visualization
- 🌍 Custom domain deployment
- 🔐 Password history and favorites
- 📱 Mobile app version

---

## 🛡️ Security & Privacy

- **Local Processing**: All password analysis is done locally in your browser
- **No Data Storage**: No passwords are stored, transmitted, or logged
- **Open Source**: Full source code available for security review
- **No Tracking**: No analytics or user tracking

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share!

---

## ✨ Made by [@ubiiii](https://github.com/ubiiii)

Crafted for security learners, ethical hackers, and developers who care about password hygiene.
