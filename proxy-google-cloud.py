from flask import Flask, Response
import requests, os

app = Flask(__name__)
BASE_URL = "https://mt1.google.com"

@app.route("/vt/lyrs=s&x=<int:x>&y=<int:y>&z=<int:z>")
def get_tile(z, x, y):
    url = f"{BASE_URL}/vt/lyrs=s&x={x}&y={y}&z={z}"
    try:
        r = requests.get(url, verify=False, timeout=10)
        if r.status_code == 200:
            return Response(r.content, content_type="image/png")
        else:
            return f"Upstream error {r.status_code}", r.status_code
    except Exception as e:
        return str(e), 500

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
