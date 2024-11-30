from flask import Flask, jsonify

app = Flask(__name__)

# Ruta para el endpoint GET
@app.route('/saludo', methods=['GET'])
def saludo():
    return jsonify({'mensaje': 'Hola Mundo'}), 200

@app.route('/f1', methods=['GET'])
def f1():
    return jsonify({'mensaje': 'para acabar primero, primero tienes que acabar'}), 200

@app.route('/test', methods=['GET'])
def test():
    return jsonify({'mensaje': 'test exitoso'}), 200

# Ejecución de la app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')