#!/bin/bash

echo "⚙️ Installation de Jenkins dans un conteneur Docker..."

# Créer les volumes nécessaires
mkdir -p ~/jenkins_home

# Ajouter ton utilisateur au groupe docker (si ce n'est pas encore fait)
sudo usermod -aG docker $USER

# Lancer le conteneur Jenkins avec Docker
docker run -d \
  --name jenkins \
  --restart=unless-stopped \
  -p 8080:8080 -p 50000:50000 \
  -v ~/jenkins_home:/var/jenkins_home \
  -v /var/run/docker.sock:/var/run/docker.sock \
  jenkins/jenkins:lts

echo "✅ Jenkins est en cours d'exécution sur http://localhost:8080"

echo "🔑 Pour récupérer le mot de passe initial :"
echo "   docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword"

