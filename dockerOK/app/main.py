from flask import Flask, request, jsonify, render_template
app = Flask(__name__)

weather_data = {"hryvnia_dollar": 0.0,
                "dollar_euro": 0.0,
                "dollar_pound": 0.0}
update_sensor = ["hryvnia_dollar", "dollar_euro", "dollar_pound"]

@app.route('/update', methods=['POST'])
def update_weather():
        global weather_data
        data = request.json
        for key in update_sensor:
                weather_data[key] = data.get(key, weather_data[key])
        return jsonify({"status": "success"}), 200

@app.route('/current_weather', methods=['GET'])
def get_weather():
        return jsonify(weather_data), 200

@app.route('/')
def index():
        return render_template('index.html')

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0',  port=5000)
