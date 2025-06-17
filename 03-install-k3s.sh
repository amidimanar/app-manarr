#!/bin/bash

echo "☸️ Installation de Kubernetes avec k3s..."

# Installer k3s via le script officiel
curl -sfL https://get.k3s.io | sh -

# Vérifier que le service est actif
sudo systemctl status k3s

# Installer kubectl (inclus avec k3s)
echo "export KUBECONFIG=/etc/rancher/k3s/k3s.yaml" >> ~/.bashrc
export KUBECONFIG=/etc/rancher/k3s/k3s.yaml

# Vérification
kubectl get nodes

echo "✅ k3s installé avec succès. Le cluster est prêt !"

