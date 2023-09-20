#!/bin/bash

# For CentOS
sudo yum update -y
sudo wget -O /etc/yum.repos.d/jenkins.repo https://pkg.jenkins.io/redhat-stable/jenkins.repo
sudo rpm --import https://pkg.jenkins.io/redhat-stable/jenkins.io-2023.key
sudo yum upgrade
sudo yum install java -y

# sudo yum clean packages    # If only remove packages

# Install Jenkins in CentOS
sudo yum install jenkins docker git -y
sudo systemctl enable jenkins
sudo systemctl start jenkins

# Start Docker
# sudo systemctl start docker

# Add your user to the docker group.
sudo usermod -aG docker $USER
# sudo usermod -a -G docker jenkins
# newgrp docker

# Docker start in Boot
sudo systemctl enable docker.service
sudo systemctl start docker.service

# sudo systemctl enable containerd.service