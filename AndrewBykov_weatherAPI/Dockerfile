# Вибір базового образу
#FROM node:14
# Встановлення робочої директорії
#WORKDIR /app
# Копіювання package.json і package-lock.json
#COPY package*.json ./
# Встановлення залежностей
#RUN npm install
# Копіювання всіх файлів у робочу директорію
#COPY . .
# Відкриття порту
#EXPOSE 8080
# Вказання команди для запуску додатку
#CMD ["node", "app.js"]
# Використання базового образу з Python
FROM python:3.12.3 
#-slim
# Встановлення робочої директорії
WORKDIR /app
# Копіювання файлів до контейнера
COPY requirements.txt requirements.txt
COPY app/ app/
# Встановлення залежностей
#RUN pip install -r requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
# Відкриття порту
EXPOSE 5000
# Команда для запуску додатку
CMD ["python", "app/server.py"]



