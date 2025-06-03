#servico_2/app.py
from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/data', methods=['GET'])
def get_data():
    # Lógica para obter e processar dados
    data = {'message': 'Dados obtidos com sucesso do serviço 2!'}
    return jsonify(data)
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)