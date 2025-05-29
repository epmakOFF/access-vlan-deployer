import subprocess

from flask import Flask

app = Flask(__name__)


@app.route("/ping/<ip>")  # URL вида /ping/8.8.8.8
def index(ip):
    result = subprocess.run(["ping", "-c", "4", ip], capture_output=True, text=True)
    return f"Ping to {ip}:<br><pre>{result.stdout}</pre>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
