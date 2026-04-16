import requests
from bs4 import BeautifulSoup
import re
import time
from datetime import datetime

# ✅ Database import
from database import init_db, insert_data

# ✅ Initialize DB
init_db()


# ==============================
# 🔍 Fetch Threat News
# ==============================
def fetch_threat_news():
    print("\n🌐 Fetching Threat Intelligence Feeds...\n")

    url = "https://thehackernews.com/"

    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("a", class_="story-link")

        for article in articles[:5]:
            title = article.get_text(strip=True)
            link = article.get("href")

            print(f"📰 {title}")
            print(f"🔗 {link}\n")

            # ✅ Save to DB
            insert_data("news", title)

    except Exception as e:
        print("❌ Error fetching news:", e)


# ==============================
# ☠️ Fetch Malicious IOCs
# ==============================
def fetch_malicious_iocs():
    print("\n☠️ Fetching Known Malicious IOCs...\n")

    # Sample malicious URLs (simulate threat feed)
    malicious_list = [
        "http://malicious-site.com",
        "http://phishing-login.net",
        "http://badserver.xyz/malware",
    ]

    for url in malicious_list:
        print(f"⚠️ Malicious URL: {url}")

        # ✅ Save to DB
        insert_data("malicious_url", url)


# ==============================
# 🧠 IOC Detection
# ==============================
def detect_iocs(text):
    print("\n🧠 Running IOC Detection...\n")

    emails = re.findall(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", text)
    urls = re.findall(r"https?://[^\s]+", text)

    for email in emails:
        print(f"📧 Email Found: {email}")
        insert_data("email", email)

    for url in urls:
        print(f"🌍 URL Found: {url}")
        insert_data("url", url)

        if "malicious" in url:
            print("🚨 ALERT: High-risk URL detected!")
            insert_data("alert", url)


# ==============================
# 🤖 Simple AI Analysis
# ==============================
def ai_analyze(text):
    print("\n🤖 AI Threat Analysis...\n")

    risk_score = 0

    if "malicious" in text:
        risk_score += 3
    if "phishing" in text:
        risk_score += 2
    if "admin" in text:
        risk_score += 1

    print(f"📊 Risk Score: {risk_score}")

    if risk_score >= 5:
        print("🚨 Threat Level: HIGH")
    elif risk_score >= 3:
        print("⚠️ Threat Level: MEDIUM")
    else:
        print("✅ Threat Level: LOW")


# ==============================
# 🚀 Main Tool Runner
# ==============================
def run_tool():
    print("\n🚨 Dark Web Threat Intelligence Tool 🚨")
    print(f"🕒 {datetime.now()}")

    # Step 1: News
    fetch_threat_news()

    # Step 2: Malicious IOCs
    fetch_malicious_iocs()

    # Step 3: Sample Text Analysis
    sample_text = """
    Contact admin@test.com immediately.
    Visit http://malicious-site.com for details.
    """

    detect_iocs(sample_text)

    # Step 4: AI Analysis
    ai_analyze(sample_text)


# ==============================
# 🔁 Continuous Run
# ==============================
if __name__ == "__main__":
    try:
        while True:
            run_tool()
            print("\n⏳ Waiting 60 seconds before next scan...\n")
            time.sleep(60)

    except KeyboardInterrupt:
        print("\n🛑 Tool stopped by user. Exiting cleanly...")