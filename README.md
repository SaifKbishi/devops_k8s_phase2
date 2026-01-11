# My Containerized Docker App on K8s
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
- Scalable and highly available application
- Orchestrated using Kubernetes

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
- [Kubectl](https://kubernetes.io/docs/tasks/tools/) installed

### Setup from Github 
Build and Run the Project:
- In your terminal, navigate to the project directory and run:
- Clone the repository
```bash
    git clone https://github.com/SaifKbishi/devops_k8s_phase2
    cd devops_k8s_phase2
```
- Build and Run Docker container
```bash
	cd app
	docker-compose build --no-cache
	docker-compose up -d
```
- Push to your docker hub (wiht your dockerhub username)
```bash
	docker push 19820401/devops-k8s-phase2:3.0.0
```
- Deploy yaml files
```bash
	cd ..
	kubectl apply -f .
	minikube addons enable metrics-server
```

- Verify Service:
```bash
	kubectl get pods
	kubectl get svc
	kubectl get pvc
	kubectl get hpa
```
- Access via Minikube:
```bash
	minikube service devops-k8s-phase2-service
```

