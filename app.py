from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = os.getenv("API_KEY")

HEADERS = {
    "x-apisports-key": API_KEY
}

PLAYER_SEARCH_URL = "https://v1.basketball.api-sports.io/players?search={}"

@app.route("/", methods=["GET", "POST"])
def index():
    stats = None
    raw_api = None   # 👈 Para mostrar lo que llega realmente

    if request.method == "POST":
        player = request.form["player"]

        try:
            response = requests.get(
                PLAYER_SEARCH_URL.format(player),
                headers=HEADERS
            )

            raw_api = response.text  # 👈 Guardamos lo que responde la API

            data = response.json()
        except Exception as e:
            raw_api = f"ERROR: {str(e)}"
            data = {"response": []}

        if "response" in data and data["response"]:
            stats = data["response"][0]
        else:
            stats = None

    return render_template("index.html", stats=stats, raw_api=raw_api)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
