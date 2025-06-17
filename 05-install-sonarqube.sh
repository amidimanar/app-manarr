#!/bin/bash

echo "🚀 Installation de SonarQube..."

# Créer un réseau Docker dédié (optionnel mais recommandé)
docker network create sonarnet 2>/dev/null || true

# Lancer la base de données PostgreSQL pour SonarQube
docker run -d \
  --name sonarqube-postgres \
  --network sonarnet \
  -e POSTGRES_USER=sonar \
  -e POSTGRES_PASSWORD=sonar \
  -e POSTGRES_DB=sonar \
  postgres:15-alpine

# Lancer SonarQube, connecté au réseau et à la base de données
docker run -d \
  --name sonarqube \
  --network sonarnet \
  -p 9000:9000 \
  -e SONAR_JDBC_URL=jdbc:postgresql://sonarqube-postgres:5432/sonar \
  -e SONAR_JDBC_USERNAME=sonar \
  -e SONAR_JDBC_PASSWORD=sonar \
  sonarqube:latest

echo "✅ SonarQube démarré sur http://localhost:9000"

