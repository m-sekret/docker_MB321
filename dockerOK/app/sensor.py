import requests # Імпортуємо бібліотеку requests для виконання HTTP-запитів
api_key = "dab2647b113b40fc264d2352a1a9a715" # Зберігаємо ваш API-ключ у змінній
city = "Kyiv" # Вказуємо місто, для якого хочемо отримати дані про погоду
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}" # Створюємо URL для запиту з містом та API-ключем
local_url = 'http://localhost:5000/update'

while True:
    data_a = requests.get(url)
    response = requests.post(local_url, json=data_a)
    print(f"Sent data: {food_shares}, Response: {response.status_code}")
    time.sleep(30)
