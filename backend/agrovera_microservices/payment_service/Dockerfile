FROM python:3.10-slim

WORKDIR /app

# Installer netcat
RUN apt-get update && apt-get install -y netcat-openbsd


COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Donner les droits d’exécution au script d'entrée
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
