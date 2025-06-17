#!/bin/bash

echo "🐳 Installation de Docker..."

# Supprimer d'anciens paquets Docker s'ils existent
sudo apt remove -y docker docker-engine docker.io containerd runc

# Installer les dépendances nécessaires
sudo apt update
sudo apt install -y ca-certificates curl gnupg

# Ajouter la clé GPG officielle de Docker
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Ajouter le dépôt officiel de Docker
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | \
  sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Mise à jour et installation de Docker Engine
sudo apt update
sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Activer et démarrer Docker
sudo systemctl enable docker
sudo systemctl start docker

# Ajouter l'utilisateur courant au groupe docker
sudo usermod -aG docker $USER

echo "✅ Docker installé avec succès."

# Affichage des versions
docker --version
docker compose version

echo "⚠️ Tu dois maintenant exécuter la commande suivante OU redémarrer ta session pour activer le groupe 'docker' :"
echo "   newgrp docker"

