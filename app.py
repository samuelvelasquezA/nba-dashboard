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

    if request.method == "POST":
        player = request.form["player"]

        try:
            response = requests.get(
                PLAYER_SEARCH_URL.format(player),
                headers=HEADERS
            )

            data = response.json()
        except:
            data = {"response": []}

        if "response" in data and data["response"]:
            stats = data["response"][0]  # Primer jugador encontrado
        else:
            stats = None

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
