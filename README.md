
# 🔐 ShadowKey

**ShadowKey** is a hacker-styled password security toolkit that helps users check the strength of their passwords, estimate how long they'd take to crack, and generate strong, secure passwords with customizable options.

Built with Python + Flask and designed for both desktop and mobile browsers.

---

## 🚀 Features

- ✅ Password Strength Checker  
- ✅ Complexity Breakdown (uppercase, lowercase, digits, symbols, length)  
- ✅ Estimated Time to Crack (based on brute-force attack)  
- ✅ Password Generator with custom options:
  - Length (slider)
  - Include uppercase, lowercase, digits, and/or symbols
  - Guarantees inclusion of all selected types
- ✅ Copy to clipboard
- ✅ Responsive UI (works great on mobile too)

---

## 🧪 Live Demo

🌐 [Check out ShadowKey live on Render](https://your-render-app-url.com)

*(Replace this with your actual Render URL once deployed)*

---

## 📸 Screenshot

![ShadowKey Web App Screenshot](https://your-screenshot-link.com)

*(Optional — add a screenshot here after deployment)*

---

## 🛠️ Tech Stack

| Tech       | Purpose              |
|------------|----------------------|
| Python     | Backend logic        |
| Flask      | Web framework        |
| HTML/CSS   | Frontend structure   |
| Bootstrap  | Responsive design    |
| JavaScript | UI interaction       |

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

4. **Run the app**  
```bash
python app.py
```

5. Visit [http://localhost:5000](http://localhost:5000) in your browser 🎉

---

## 📂 Project Structure

```
shadowkey/
├── app.py               # Main Flask app
├── requirements.txt     # Dependencies
├── render.yaml          # Render deployment config
├── templates/
│   └── index.html       # Web UI
├── static/
│   ├── style.css        # Custom styles (optional)
│   └── script.js        # Frontend JS (inline for now)
```

---

## 🧠 Future Ideas

- 🔒 Integration with HaveIBeenPwned API
- 🎨 Theme toggling (dark/light)
- 📊 Entropy visualization
- 🌍 Custom domain deployment

---

## 📜 License

This project is licensed under the MIT License. Feel free to use, modify, and share!

---

## ✨ Made by [@ubiiii](https://github.com/ubiiii)

Crafted for security learners, ethical hackers, and developers who care about password hygiene.
