from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "cb6ffc313a4970c3110fb44b919cc341"

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
            stats = data["response"][0]
        else:
            stats = None

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
