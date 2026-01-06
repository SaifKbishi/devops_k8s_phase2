# My Containerized Docker App on K8s
## Overview
A simple Flask application containerized with Docker, demonstrating multiple routes and basic web functionalities.
Orchestrated using Kubernetes, with ReplicaSet for managing the application, exposed externally using a Kubernetes Service.
With implementation of Horizontal Pod Autoscaling (HPA) based on CPU usage.
Use ConfigMaps and Secrets to manage configuration, set up with Kubernetes CronJobs to automate periodic tasks.
Implementation of Liveness and Readiness Probes for monitoring application health.
Packaged with Helm Chart

## Features
- Flask server with multiple routes
- Dockerized for easy deployment
- non-Responsive HTML templates
- Environment configuration management
- Scalable and highly available application
- Orchestrated using Kubernetes
- Helm Chart packaged

## Technologies
- Python 3.10-slim
- Flask
- Docker
- Minikube
- K8s: HPA, ConfigMaps and Secrets, CronJobs, Liveness and Readiness Probes
- Helm Chart

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
	git checkout phase3
```
- Build and Run Docker container
```bash
	cd app
	docker-compose up -d --build
```
- Push to your docker hub (wiht your dockerhub username)
```bash
	docker push 19820401/devops-k8s-phase2:3.0.0
```
- Create helm chart (already created)
```bash
	helm create phase3
```

- Package helm chart
```bash
	helm package phase3
```

- To make sure you don't have the same release installed:
```bash
	helm list	
```
- Install helm release
```bash
	helm install phase3-release ./phase3-0.1.0.tgz
```

- Upgrade helm release (if needed)
```bash
	helm upgrade phase3-release ./phase3-0.1.0.tgz
```

- Get the application URL by running these commands:
```bash
  export POD_NAME=$(kubectl get pods --namespace default -l "app.kubernetes.io/name=phase3,app.kubernetes.io/instance=phase3-release" -o jsonpath="{.items[0].metadata.name}")
  export CONTAINER_PORT=$(kubectl get pod --namespace default $POD_NAME -o jsonpath="{.spec.containers[0].ports[0].containerPort}")
  echo "Visit http://127.0.0.1:8080 to use your application"
  kubectl --namespace default port-forward $POD_NAME 8080:$CONTAINER_PORT
```

- If you need to uninstall a helm chart
```bash
	helm uninstall phase3-release
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

