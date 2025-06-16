FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \
    apt-get install -y docker.io && \
    apt-get clean

# Remplacer 998 par le vrai GID obtenu
RUN groupmod -g 984 docker && usermod -aG docker jenkins

USER jenkins

