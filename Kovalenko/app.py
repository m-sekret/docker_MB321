from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)
API_KEY = '7dd77011d5d6f0ea8c237ad4'
BASE_URL = 'https://v6.exchangerate-api.com/v6'

@app.route('/update', methods=['GET'])
def update_exchange_rates():
    response = requests.get(f'{BASE_URL}/{API_KEY}/latest/USD')
    data = response.json()
    return jsonify(data), 200

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)