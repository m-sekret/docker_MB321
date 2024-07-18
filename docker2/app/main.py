from flask import render_template
import requests
from app import app
@app.route('/')
def index():
	# Приклад отримання даних з API
	diesel_price = requests.get('').json().get('price')
	gasoline_price = requests.get('').json().get('price')
	gas_price = requests.get('').json().get('price')
	return render_template('index.html', diesel=diesel_price, gasoline=gasoline_price, gas=gas_price)
