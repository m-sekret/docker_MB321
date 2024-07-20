# Виберіть базовий образ
FROM python:3.11-slim

# Встановіть робочу директорію
WORKDIR /app

# Копіюйте файли вашого проекту до контейнера
COPY requirements.txt /app

# Створіть віртуальне середовище
RUN python -m venv venv

# Активуйте віртуальне середовище і встановіть залежності
RUN . venv/bin/activate 
RUN pip install --no-cache-dir -r requirements.txt

# Копіюйте решту файлів проекту
COPY . /app

EXPOSE 5000

# Використовуйте віртуальне середовище для запуску додатку
COPY start.sh /app/start.sh
RUN chmod +x /app/start.sh

CMD ["python", "/app/app.py"]
