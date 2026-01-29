from flask import Flask, request, abort
import requests, os

app = Flask(__name__)

WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SECRET_TOKEN = os.getenv("SECRET_TOKEN")

def get_location(ip):
    try:
        response = requests.get(f"https://ipinfo.io/{ip}/json")
        if response.status_code == 200:
            data = response.json()
            cidade = data.get("city", "Desconhecida")
            regiao = data.get("region", "Desconhecida")
            pais = data.get("country", "Desconhecido")
            return f"{cidade}, {regiao}, {pais}"
    except:
        pass
    return "Localização não encontrada"

@app.route('/')
def home():
    token = request.args.get("token")
    if token != SECRET_TOKEN:
        abort(403)

    ip = request.remote_addr
    localizacao = get_location(ip)

    data = {
        "content": f"📢 Acesso autorizado!\nIP: {ip}\nLocalização: {localizacao}"
    }
    requests.post(WEBHOOK_URL, json=data)

    return "<h1>Bem-vindo, Marcos! Você tem acesso exclusivo.</h1>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)

