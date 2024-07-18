from flask import Flask, render_template
import requests
import random

app = Flask(__name__)
url = "https://v6.exchangerate-api.com/v6/7dd77011d5d6f0ea8c237ad4/latest/USD"

def get_curency():
	response = requests.get(url)
	if response.status_code == 200:
		data = response.json()
		USD_UAH = data['conversion_rates']['UAH']
		USD_EUR = data['conversion_rates']['EUR']
		USD_GBP = data['conversion_rates']['GBP']
		return data['conversion_rates']
	else:
		return None 


@app.route('/')
def index():
    rates = get_curency()
    if rates:
        USD_UAH = rates.get('UAH')
        USD_EUR = rates.get('EUR')
        USD_GBP = rates.get('GBP')
    else:
        USD_UAH = USD_EUR = USD_GBP = None
    return render_template('index.html', USD_UAH=USD_UAH, USD_EUR=USD_EUR, USD_GBP=USD_GBP)

if __name__ == '__main__':
    app.run(debug=True)