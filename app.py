from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return '''
        <h1>Olá, mundo! Este é o início do projeto.</h1>
        <img src="https://scontent.fslz4-1.fna.fbcdn.net/v/t1.6435-9/70734133_937164883300936_3042617985685520384_n.jpg?_nc_cat=102&ccb=1-7&_nc_sid=833d8c&_nc_eui2=AeEg_ul9WZc-DS93rlNlOvlLMWfAYLq_TjgxZ8Bgur9OOCBzJzZDDI0Q8bBy6ADwqNwLk_tRNpVEDGEJRUpQ2bhH&_nc_ohc=LXvgAnZY96kQ7kNvwEA6hzE&_nc_oc=AdlHDutrdG9VlHs8KMW-I7-heWmbBC8aOs5WxJmqtyXMKSLcP8rRv7l767odzcKqyaA&_nc_zt=23&_nc_ht=scontent.fslz4-1.fna&_nc_gid=eP0pJWkz0r7fHGQitLZmjw&oh=00_Afrscey8UpeuwwrI7H20gUJs737VNnGdFG3a8qP4qYaBFw&oe=69A35071" 
             alt="Minha Foto" width="400">
    '''

@app.route('/link-secreto')
def link_secreto():
    return 'Você acessou o link secreto com sucesso!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)

