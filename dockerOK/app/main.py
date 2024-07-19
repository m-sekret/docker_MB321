from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

import requests # Імпортуємо бібліотеку requests для виконання HTTP-запитів
api_key = "dab2647b113b40fc264d2352a1a9a715" # Зберігаємо ваш API-ключ у змінній
city = "Kyiv" # Вказуємо місто, для якого хочемо отримати дані про погоду
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" # Створюємо URL для запиту з містом та API-ключем

weather_data = {"hryvnia_dollar": 0.0,
                "dollar_euro": 0.0,
                "dollar_pound": 0.0}
#update_sensor = ["hryvnia_dollar", "dollar_euro", "dollar_pound"]
while True:
        data = response.json(requests.get(url))
        response = requests.post(local_url, json=data_a)
	weather_data['hryvnia_dollar']=data['weather'][0]['description']
        time.sleep(30)
#@app.route('/update', methods=['POST'])
#def update_weather():
#        global weather_data
#        data = request.json
        #for key in update_sensor:
        #        weather_data[key] = data.get(key, weather_data[key])
#        print(data)
#        weather_data['hryvnia&dollar'] = data.get(['weather'][0]['description'], weather_data['hryvnia&dollar'])
#        return jsonify({"status": "success"}), 200

@app.route('/current_weather', methods=['GET'])
def get_weather():
        return jsonify(weather_data), 200

@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0',  port=5000)
