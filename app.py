
from flask import Flask, redirect
from datetime import datetime
import requests

app = Flask(__name__)
acessos = []

WEBHOOK_URL = "https://discordapp.com/api/webhooks/1466478241031131217/mYik7TijEancs0yK6djeIoK3W8HM4St6O-J_uWWuKdne9g4Z1mj_qRke9D_0z1hEkwzg"

def enviar_discord(horario):
    data = {"content": f"🚨 O link secreto foi acessado em {horario}"}
    try:
        requests.post(WEBHOOK_URL, json=data)
    except Exception as e:
        print(f"Erro ao enviar para Discord: {e}")

@app.route("/link-secreto")
def registrar():
    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    acessos.append(agora)
    print(f"Acesso registrado: {agora}")
    enviar_discord(agora)
    # 👉 Redireciona direto para a imagem no Facebook
    return redirect("https://scontent.fslz4-1.fna.fbcdn.net/v/t1.6435-9/70734133_937164883300936_3042617985685520384_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_eui2=AeEg_ul9WZc-DS93rlNlOvlLMWfAYLq_TjgxZ8Bgur9OOCBzJzZDDI0Q8bBy6ADwqNwLk_tRNpVEDGEJRUpQ2bhH&_nc_ohc=LXvgAnZY96kQ7kNvwEA6hzE&_nc_oc=AdlHDutrdG9VlHs8KMW-I7-heWmbBC8aOs5WxJmqtyXMKSLcP8rRv7l767odzcKqyaA&_nc_zt=23&_nc_ht=scontent.fslz4-1.fna&_nc_gid=C0bAZCzNcVxUvYE66iOBtQ&oh=00_AfrxQnHPENWTQ-11vaxzkoWAev_bAPA-yNF3hmJnja-4cw&oe=69A31831")

@app.route("/relatorio")
def relatorio():
    return f"""
    <h2>Total de acessos: {len(acessos)}</h2>
    <ul>
        {''.join(f'<li>{hora}</li>' for hora in acessos)}
    </ul>
    """

if __name__ == "__main__":
    app.run(debug=True)

