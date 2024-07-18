from flask import render_template
import requests
from app import app

# Füge hier deinen API-Schlüssel ein
API_KEY = 'DEIN_API_KEY'

@app.route('/')
def index():
    headers = {
        'Authorization': f'Bearer {API_KEY}'
    }

    # URLs der APIs für Diesel, Benzin und Gas
    diesel_url = 'URL_FOR_DIESEL_API'
    gasoline_url = 'URL_FOR_GASOLINE_API'
    gas_url = 'URL_FOR_GAS_API'

    # Beispiel zum Abrufen von Daten von der API
    diesel_price = requests.get(diesel_url, headers=headers).json().get('price')
    gasoline_price = requests.get(gasoline_url, headers=headers).json().get('price')
    gas_price = requests.get(gas_url, headers=headers).json().get('price')

    return render_template('index.html', diesel=diesel_price, gasoline=gasoline_price, gas=gas_price)
