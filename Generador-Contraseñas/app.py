from flask import Flask, render_template, request, jsonify
import random
import string
from flask_cors import CORS #Es importante solo si el front es independiente del back

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generar', methods=['POST'])
def generar_contraseña():
    datos = request.get_json()
    longitud = int(datos['longitud'])
    mayusculas = datos['mayusculas']
    minusculas = datos['minusculas']
    numeros = datos['numeros']
    simbolos = datos['simbolos']

    caracteres = ""
    if mayusculas:
        caracteres += string.ascii_uppercase
    if minusculas:
        caracteres += string.ascii_lowercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return jsonify({"contraseña": "Selecciona al menos una opción"})

    contraseña = "".join(random.choice(caracteres) for _ in range(longitud))
    return jsonify({"contraseña": contraseña})

if __name__ == '__main__':
    app.run(debug=True)