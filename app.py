from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "cb6ffc313a4970c3110fb44b919cc341"  # tu llave
BASE_URL = "https://v1.basketball.api-sports.io/players?search={}"

headers = {
    "x-apisports-key": API_KEY
}

@app.route("/", methods=["GET", "POST"])
def index():
    stats = None

    if request.method == "POST":
        player = request.form["player"]

        try:
            url = BASE_URL.format(player)
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                data = response.json()
            else:
                data = {"response": []}

        except:
            data = {"response": []}

        # la API de API-SPORTS devuelve "response"
        if data.get("response"):
            stats = data["response"][0]
        else:
            stats = {"name": "No encontrado"}

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
