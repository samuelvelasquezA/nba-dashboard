from flask import Flask, render_template, request
import requests

app = Flask(__name__)

BALDONTLIE_URL = "https://api.balldontlie.io/v1/players?search={}"

@app.route("/", methods=["GET", "POST"])
def index():
    stats = None

    if request.method == "POST":
        player = request.form["player"]

        # --- NUEVO MÉTODO: evita errores 500 en Render ---
        try:
            url = BALDONTLIE_URL.format(player)
            response = requests.get(url)

            if response.status_code == 200:
                data = response.json()
            else:
                data = {"data": []}

        except:
            data = {"data": []}

        # Resultado
        if data["data"]:
            stats = data["data"][0]
        else:
            stats = {"name": "No encontrado"}

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
