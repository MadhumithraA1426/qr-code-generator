# 🔳 QR Code Generator Web App

A simple and responsive **QR Code Generator** built using **Python (Flask)**.  
Users can enter a URL, generate a QR code instantly, preview it on the screen, and download it as an image.

---

## 🚀 Features

- Generate QR codes for any URL
- Instant QR preview on the webpage
- Download QR code as PNG
- Clean and responsive UI
- Deployed-ready Flask application

---

## 🛠️ Tech Stack

- **Backend:** Python, Flask
- **Frontend:** HTML, CSS, JavaScript
- **Libraries:** qrcode, Pillow
- **Server:** Gunicorn

---

## 📂 Project Structure

qr-code-generator/
│── main.py
│── requirements.txt
│── .gitignore
│── templates/
│ └── index.html
│── static/
│ └── style.css


---

## ⚙️ Installation & Run Locally

### 1️⃣ Clone the repository
git clone https://github.com/MadhumithraA1426/qr-code-generator.git
cd qr-code-generator

### 2️⃣ Create virtual environment (optional)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate

### 3️⃣ Install dependencies
pip install -r requirements.txt

### 4️⃣ Run the application
python main.py

Open your browser and visit:
http://127.0.0.1:5000

## 🌐 Deployment

This project is deployment-ready for platforms like Render, Railway, or Heroku.
Start Command:
gunicorn main:app

## 📄 License

This project is open-source and available under the MIT License.

## 🙌 Author

Madhu Mithra A
Computer Science Engineering Student
Interested in Web Development & AI Projects
