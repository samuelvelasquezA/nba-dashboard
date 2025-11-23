
from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)

API_KEY = "cb6ffc313a4970c3110fb44b919cc341"   # ← Tu KEY
API_URL = "https://v1.basketball.api-sports.io/players"

HEADERS = {
    "x-apisports-key": API_KEY,
    "x-apisports-host": "v1.basketball.api-sports.io"
}

@app.route("/", methods=["GET", "POST"])
def index():
    player_stats = None
    error = None

    if request.method == "POST":
        player_name = request.form["player"]

        try:
            # 🔍 Buscar jugador por nombre
            response = requests.get(
                API_URL,
                headers=HEADERS,
                params={"search": player_name, "league": 12, "season": 2024}  # NBA = league 12
            )

            if response.status_code != 200:
                error = "API Error"
                return render_template("index.html", stats=None, error=error)

            data = response.json()

            if data["response"]:
                player_stats = data["response"][0]   # Primer match
            else:
                error = "Jugador no encontrado"

        except Exception as e:
            error = f"Error: {str(e)}"

    return render_template("index.html", stats=player_stats, error=error)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

