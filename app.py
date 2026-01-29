from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Olá, mundo! Este é o início do projeto.'

@app.route('/link-secreto')
def link_secreto():
    return 'Você acessou o link secreto com sucesso!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000, debug=False)


