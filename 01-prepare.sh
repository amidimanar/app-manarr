#!/bin/bash

echo "🔧 Mise à jour du système..."
sudo apt update && sudo apt upgrade -y

echo "📦 Installation des outils de base..."
sudo apt install -y \
    git \
    curl \
    wget \
    vim \
    unzip \
    apt-transport-https \
    ca-certificates \
    gnupg \
    lsb-release \
    software-properties-common

echo "✅ Préparation terminée !"

