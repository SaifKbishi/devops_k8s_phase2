# My Containerized Docker App on K8s
## Overview
A CI/CD project for a simple Flask application containerized with Docker, demonstrating multiple routes and basic web functionalities.
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
- CI/CD using Jenkins and Github

## Technologies
- Python 3.10-slim
- Flask
- Docker
- Minikube
- K8s: HPA, ConfigMaps and Secrets, CronJobs, Liveness and Readiness Probes
- Helm Chart
- Jenkins

## Getting Started

### Prerequisites
- [Python](https://www.python.org/downloads/) installed
- [Docker](https://www.docker.com/get-started) installed
- [Docker Desktop](https://docs.docker.com/desktop/setup/install/windows-install/) installed
- [Minikube](https://minikube.sigs.k8s.io/docs/start/?plugin_version=chrome_4.0.13&arch=%2Fwindows%2Fx86-64%2Fstable%2F.exe+download) installed
- [Kubectl](https://kubernetes.io/docs/tasks/tools/) installed
- [Java] installed
- [Jenkins] installed

### Setup 
You need to have a Jenkins controller running, java istalled (openjdk-17-jdk), a jenkins agent is configured and connected. 

```bash
    docker run -d -p 8080:8080 -p 50000:50000 --name jenkins -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```
- In jenkins UI create a job and setup the follwoing:
	- SCM: Git
	- Repository URL: https://github.com/SaifKbishi/devops_k8s_phase2.git
	- Branch Specifier: */jenkins
	- Script Path: app/Jenkinsfile
	Save

I have used the architecture for Minikube + Jenkins where everything on One Machine



- Run the job in jenkins UI