from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/calcular_propina', methods=['POST'])
def calcular_propina():
    data = request.json
    total_factura = float(data['total_factura'])
    porcentaje_propina = float(data['porcentaje_propina'])

    propina = total_factura * (porcentaje_propina / 100)
    total_con_propina = total_factura + propina

    return jsonify({
        'propina': round(propina, 2),
        'total_con_propina': round(total_con_propina, 2)
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)#Tenía el 6000