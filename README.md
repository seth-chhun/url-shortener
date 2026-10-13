# 🔗 url-shortener

A simple link shortener built with **Flask** and **SQLite** — my first full-stack web project!

Turn long, ugly URLs into short, shareable links. Built from scratch to understand how the web actually works.

![Python](https://img.shields.io/badge/Python-3.14.8-blue)
![Flask](https://img.shields.io/badge/Flask-2.1.3-black)
![SQLite](https://img.shields.io/badge/SQLite-3-lightgrey)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📖 About

This is my **first web development project**. I built it to answer a simple question:  
*"How do link shorteners like bit.ly actually work?"*

From this project, I have learned alot including:

- **How link shorteners work** under the hood (generate short codes → store mapping → redirect on visit)
- **How web protocols work** : the request/response cycle, HTTP status codes (especially `301` and `302` redirects)
- **How routing works** in web frameworks : dynamic URL parameters like `/<code>`
- **How to use Flask** : request handling and templating(for flash())
-  **How storage works** : designing a schema, using SQLite, and querying with SQL

---

## ✨ Features

- Shorten any long URL into a compact code (using generic *secrets* module)
- Redirect short links to their original URLs
- Persistent storage with SQLite

---

## 🛠️ Tech Stack

| Layer     | Tech          |
|-----------|---------------|
| Backend   | Python, Flask |
| Database  | SQLite        |
| Frontend  | HTML, Jinja2 templates |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.10+
- pip

### Installation

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/flask-link-shortener.git
   cd flask-link-shortener

2. **Create a virtual environment**
    ```bash
    python -m venv .venv
    source .venv/Scripts/activate

3. **Install dependencies**
    ```bash
    pip install -r requirement.txt

4. **Run the app**
    ```bash
    flask run

5. **Open in your browser**

    ```bash
    http://127.0.0.1:5000

---

## 🧭 How It Works

1. User submits a URL through the homepage form.

2. The app generates a unique code (e.g., abc123).

3. The (code → url) mapping is saved in SQLite.

4. When someone visits /code, Flask looks up the code and issues an HTTP redirect to the original URL.

---

## 📸 Screenshots

![example](/image/example.png)

---

### 🗺️ Future Improvements
- User accounts and custom short codes
- Click analytics dashboard
- Expiring links

---

### 💡 What I Learned
This project was a big step for me. Before this, I didn't understand how a request even reached my code. Now I understand:

- The difference between GET and POST requests

- What a route really is and why dynamic routes matter

- How HTTP redirects work (and why 302 is better than 301 here)

- How to talk to a database from Python 

- Why virtual environments exist 😅

---

### 🤝 Contributing
This is a learning project, but feedback is welcome! Feel free to open an issue or reach out.

---

### 📄 License
MIT

### 🙏 Acknowledgments
Google Gemini for being the first want to reach out when I search on Google.

