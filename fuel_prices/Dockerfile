# Verwenden eines Basis-Images mit Python
FROM python:3.9-slim

# Arbeitsverzeichnis festlegen
WORKDIR /app

# Dateien in den Container kopieren
COPY requirements.txt requirements.txt
COPY app/ app/

# Abhängigkeiten installieren
RUN pip install -r requirements.txt

# Port öffnen
EXPOSE 5000

# Befehl zum Starten der Anwendung
CMD ["python", "app/main.py"]
