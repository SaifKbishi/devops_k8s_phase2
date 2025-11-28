# My Flask Docker App
## Overview
A simple Flask application containerized with Docker, demonstrating multiple routes and basic web functionalities.
Orchestrated using Kubernetes, with ReplicaSet for managing the application, exposed externally using a Kubernetes Service.
With implementation of Horizontal Pod Autoscaling (HPA) based on CPU usage.
Use ConfigMaps and Secrets to manage configuration, set up with Kubernetes CronJobs to automate periodic tasks.
Implementation of Liveness and Readiness Probes for monitoring application health.

## Features
- Flask server with multiple routes
- Dockerized for easy deployment
- non-Responsive HTML templates
- Environment configuration management

## Technologies
- Python 3.10-slim
- Flask
- Docker
- Minikube
- K8s: HPA, ConfigMaps and Secrets, CronJobs, Liveness and Readiness Probes

## Getting Started

### Prerequisites
- [Python](https://www.python.org/downloads/) installed
- [Docker](https://www.docker.com/get-started) installed
- [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) installed
- [Minikube](https://minikube.sigs.k8s.io/docs/start/?plugin_version=chrome_4.0.13&arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download) installed


### Setup from Github 
Build and Run the Project:
- In your terminal, navigate to the project directory and run:
- Clone the repository
```bash
    git clone https://github.com/SaifKbishi/devops_k8s_phase2
    cd devops_k8s_phase2
```
```bash
    docker build -t 19820401/devops_k8s_phase2:1.0.0 .
```
```bash
    docker run -d -p 5008:5008 --name devops_k8s_phase2-cntnr1 -v devops_k8s_phase2_volume:/app/static 19820401/devops_k8s_phase2:1.0.0
```

    Then in your browser go to (http://127.0.0.1:5008/)

### Setup from Docker hub 
Build and Run the Project:
- In your terminal, navigate to the project directory and run:
- Pull the image from Docker Hub:
```bash
    docker pull 19820401/devops_k8s_phase2:1.0.0
```
```bash
    docker run -d -p 5008:5008 --name devops_k8s_phase2-cntnr1 -v devops_k8s_phase2_volume:/app/static 19820401/devops_k8s_phase2:1.0.0
```
    Then in your browser go to (http://127.0.0.1:5008/)