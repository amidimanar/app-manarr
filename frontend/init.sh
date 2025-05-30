#!/bin/bash

# Chemin du dossier racine
ROOT_DIR="microservices"

# Liste des services avec ports
declare -A services=(
  [auth_service]=8001
  [user_service]=8002
  [stats_service]=8003
)

# Créer le dossier racine
mkdir -p "$ROOT_DIR"
cd "$ROOT_DIR"

# Création des services Django
for service in "${!services[@]}"
do
  port=${services[$service]}

  echo "🚀 Création du service $service sur le port $port"

  mkdir -p $service
  cd $service

  # Créer le projet Django dans le dossier
  django-admin startproject $service .

  # Ajouter requirements.txt
  echo -e "Django>=4.2\npsycopg2-binary" > requirements.txt

  # Ajouter Dockerfile
  cat <<EOF > Dockerfile
FROM python:3.10-slim

WORKDIR /app
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:$port"]
EOF

  # Configurer PostgreSQL dans settings.py
  SETTINGS_FILE="$service/settings.py"
  sed -i "/DATABASES = {/,\#}/c\DATABASES = {\n    'default': {\n        'ENGINE': 'django.db.backends.postgresql',\n        'NAME': 'coredb',\n        'USER': 'postgres',\n        'PASSWORD': 'admin',\n        'HOST': 'db',\n        'PORT': '5432',\n        'OPTIONS': {\n            'client_encoding': 'UTF8',\n        },\n    }\n}" $SETTINGS_FILE

  cd ..
done

# Générer docker-compose.yml
cat <<EOF > docker-compose.yml
version: '3.9'

services:
  db:
    image: postgres:17
    environment:
      POSTGRES_DB: coredb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: admin
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  auth_service:
    build: ./auth_service
    ports:
      - "8001:8001"
    depends_on:
      - db

  user_service:
    build: ./user_service
    ports:
      - "8002:8002"
    depends_on:
      - db

  stats_service:
    build: ./stats_service
    ports:
      - "8003:8003"
    depends_on:
      - db

volumes:
  postgres_data:
EOF

echo "✅ Tous les microservices sont créés et prêts à l'emploi."
echo "▶️ Tu peux lancer : docker-compose up --build"
