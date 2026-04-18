from flask import Flask, render_template, jsonify
import sqlite3

app = Flask(__name__)

def get_data():
    conn = sqlite3.connect("threats.db")
    cursor = conn.cursor()
    cursor.execute("SELECT type, value FROM threats")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route("/")
def index():
    data = get_data()

    counts = {
        "alert": 0,
        "email": 0,
        "malicious_url": 0,
        "news": 0,
        "url": 0
    }

    for row in data:
        if row[0] in counts:
            counts[row[0]] += 1

    return render_template("index.html", data=data, counts=counts)

@app.route("/api/data")
def api_data():
    data = get_data()

    counts = {
        "alert": 0,
        "email": 0,
        "malicious_url": 0,
        "news": 0,
        "url": 0
    }

    for row in data:
        if row[0] in counts:
            counts[row[0]] += 1

    return jsonify({"data": data, "counts": counts})

if __name__ == "__main__":
    app.run(debug=True)