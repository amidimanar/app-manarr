# Utiliser une image officielle de Python
FROM python:3.11-slim

# Variables d'environnement
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Installer les dépendances système
RUN apt-get update && apt-get install -y build-essential libpq-dev netcat-openbsd && rm -rf /var/lib/apt/lists/*
RUN apt-get update && \
    apt-get install -y build-essential libpq-dev netcat-openbsd curl && \
    rm -rf /var/lib/apt/lists/*

# Définir le répertoire de travail dans le conteneur
WORKDIR /app

# Copier les fichiers requirements
COPY requirements.txt /app/

# Installer les dépendances Python
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
# Installer kubectl
RUN curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl" \
    && chmod +x kubectl && mv kubectl /usr/local/bin/

# Copier tout le projet
COPY . /app/

# Exposer le port Django (par exemple 8000)
EXPOSE 8000

# Commande pour démarrer l’application
CMD ["gunicorn", "auth_service.wsgi:application", "--bind", "0.0.0.0:8000"]

