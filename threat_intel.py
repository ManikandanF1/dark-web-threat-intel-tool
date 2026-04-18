import requests
from bs4 import BeautifulSoup
import re
import time
import datetime
import logging
from database import init_db, insert_data

# Initialize DB
init_db()

# Logging setup
logging.basicConfig(filename="soc.log", level=logging.INFO)

# -------------------------------
# Fetch News
# -------------------------------
def fetch_news():
    print("\n🌐 Fetching Threat Intelligence Feeds...\n")
    url = "https://thehackernews.com/"

    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        articles = soup.find_all("a", class_="story-link")

        for article in articles[:5]:
            title = article.text.strip()
            link = article.get("href")

            print(f"📰 {title}")
            print(f"🔗 {link}\n")

            insert_data("news", title)

    except:
        print("Error fetching news")


# -------------------------------
# Fetch Malicious URLs
# -------------------------------
def fetch_malicious_iocs():
    print("\n☠️ Fetching Known Malicious IOCs...\n")

    url = "https://urlhaus.abuse.ch/downloads/text/"

    try:
        response = requests.get(url)
        lines = response.text.splitlines()

        for line in lines[:5]:
            if line.startswith("http"):
                print(f"⚠️ Malicious URL: {line}")
                insert_data("malicious_url", line)

    except:
        print("Error fetching IOCs")


# -------------------------------
# IOC Detection
# -------------------------------
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


# -------------------------------
# IOC ENRICHMENT (NEW)
# -------------------------------
def enrich_ip(ip):
    try:
        url = f"http://ip-api.com/json/{ip}"
        response = requests.get(url).json()

        country = response.get("country", "Unknown")
        isp = response.get("isp", "Unknown")

        return f"{ip} | {country} | {isp}"

    except:
        return f"{ip} | enrichment failed"


def extract_ip(url):
    match = re.findall(r"\d+\.\d+\.\d+\.\d+", url)
    return match[0] if match else None


# -------------------------------
# ADVANCED THREAT SCORING
# -------------------------------
def threat_score(text):
    score = 0

    if "malicious" in text:
        score += 5
    if "http" in text:
        score += 2
    if "@" in text:
        score += 2
    if re.search(r"\d+\.\d+\.\d+\.\d+", text):
        score += 4

    return score


def classify_threat(score):
    if score >= 7:
        return "HIGH"
    elif score >= 4:
        return "MEDIUM"
    else:
        return "LOW"


# -------------------------------
# AI ANALYSIS (UPDATED)
# -------------------------------
def ai_analyze(text):
    print("\n🤖 AI Threat Analysis...\n")

    score = threat_score(text)
    level = classify_threat(score)

    print(f"📊 Risk Score: {score}")
    print(f"🚨 Threat Level: {level}")

    insert_data("risk_score", str(score))
    insert_data("threat_level", level)


# -------------------------------
# MAIN TOOL
# -------------------------------
def run_tool():
    print("\n🚨 Dark Web Threat Intelligence Tool 🚨")
    print(f"🕒 {datetime.datetime.now()}")

    fetch_news()
    fetch_malicious_iocs()

    sample_text = "Contact admin@test.com or visit http://malicious-site.com or 8.8.8.8"

    detect_iocs(sample_text)

    # Enrichment example
    ip = extract_ip(sample_text)
    if ip:
        enriched = enrich_ip(ip)
        print(f"🌍 Enriched IP: {enriched}")
        insert_data("ip_info", enriched)

    ai_analyze(sample_text)


# -------------------------------
# LOOP
# -------------------------------
if __name__ == "__main__":
    try:
        while True:
            run_tool()
            print("\n⏳ Waiting 60 seconds before next scan...\n")
            time.sleep(60)

    except KeyboardInterrupt:
        print("\n🛑 Tool stopped by user. Exiting cleanly...")