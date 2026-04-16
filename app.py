from flask import Flask, render_template, request
from collections import Counter
from database import fetch_data, init_db

app = Flask(__name__)

# VERY IMPORTANT
init_db()


@app.route("/")
def index():
    query = request.args.get("q", "").lower()

    data = fetch_data()

    # Filter search
    if query:
        data = [d for d in data if query in d["value"].lower()]

    # Chart data
    types = [d["type"] for d in data]
    count = Counter(types)

    return render_template(
        "index.html",
        data=data,
        labels=list(count.keys()),
        values=list(count.values())
    )


if __name__ == "__main__":
    app.run(debug=True)