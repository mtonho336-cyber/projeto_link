# teste para forçar alteração
from flask import Flask, request
import requests

app = Flask(__name__)

# 👉 Cole aqui o seu webhook do Discord
WEBHOOK_URL = "COLOQUE_SEU_WEBHOOK_AQUI"

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
    ip = request.remote_addr
    localizacao = get_location(ip)

    data = {
        "content": f"📢 Alguém acessou a página inicial!\nIP: {ip}\nLocalização: {localizacao}"
    }
    requests.post(WEBHOOK_URL, json=data)

    return '''
        <h1>Olá, mundo! Este é o início do projeto.</h1>
        <img src="https://scontent.fslz4-1.fna.fbcdn.net/v/t1.6435-9/70734133_937164883300936_3042617985685520384_n.jpg"
             alt="Minha Foto" width="400">
    '''

@app.route('/link-secreto')
def link_secreto():
    ip = request.remote_addr
    localizacao = get_location(ip)

    data = {
        "content": f"🔑 Alguém acessou o link secreto!\nIP: {ip}\nLocalização: {localizacao}"
    }
    requests.post(WEBHOOK_URL, json=data)

    return 'Você acessou o link secreto com sucesso!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)

