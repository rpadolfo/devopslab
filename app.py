from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "<H1>Olá! Como vai você?</H1>"