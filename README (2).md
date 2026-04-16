\# 🚨 Dark Web Threat Intelligence Tool



\## 📌 Overview

This project is a SOC-focused Threat Intelligence Tool that collects cybersecurity data from public sources, detects Indicators of Compromise (IOCs), and visualizes them through a web dashboard.



It simulates a real-world Security Operations Center (SOC) workflow.



\---



\## 🔍 Features

\- 📰 Fetches real-time cybersecurity news

\- ☠️ Collects malicious URLs (IOC feeds)

\- 📧 Detects emails and URLs from text

\- 🚨 Generates alerts for suspicious activity

\- 🤖 AI-based risk scoring

\- 🗄️ Stores data using SQLite database

\- 🌐 Web dashboard using Flask

\- 📊 Visual charts and search functionality



\---



\## 🧠 Tech Stack

\- Python

\- Flask

\- SQLite

\- BeautifulSoup

\- Requests

\- HTML/CSS



\---



\## ⚙️ How It Works

1\. `threat\_intel.py` collects threat data

2\. Detects IOCs (URLs, emails)

3\. Stores results in SQLite database

4\. `app.py` reads data and displays it

5\. Dashboard shows threats in real-time



\---



\## 🚀 How to Run



\### Step 1: Install dependencies



pip install flask requests beautifulsoup4 feedparser





\### Step 2: Run threat collector



python threat\_intel.py





\### Step 3: Run dashboard (in new terminal)



python app.py





\### Step 4: Open browser



http://127.0.0.1:5000





\---



\## 📊 Output

\- Threat Intelligence Dashboard

\- IOC detection results

\- Alerts for malicious activity

\- Risk scoring



\---



\## 🎯 Use Case

This tool is useful for:

\- SOC Analysts

\- Cybersecurity monitoring

\- Threat detection practice

\- Learning real-world workflows



\---



\## 🔮 Future Improvements

\- Integration with real threat feeds APIs

\- Machine Learning-based threat detection

\- User authentication system

\- Cloud deployment



\---



\## 👨‍💻 Author

\*\*Manikandan G\*\*

