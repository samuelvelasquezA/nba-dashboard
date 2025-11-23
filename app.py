from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    stats = None

    if request.method == "POST":
        player = request.form["player"]

        # Esto es temporal: prueba de funcionamiento.
        # Luego yo te lo reemplazo con TODAS las funciones reales.
        url = f"https://www.balldontlie.io/api/v1/players?search={player}"
        data = requests.get(url).json()

        if data["data"]:
            stats = data["data"][0]
        else:
            stats = {"name": "No encontrado"}

    return render_template("index.html", stats=stats)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
