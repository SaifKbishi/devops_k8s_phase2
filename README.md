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

- In jenkins UI create a job and setup the follwoing:
	- SCM: Git
	- Repository URL: https://github.com/SaifKbishi/devops_k8s_phase2.git
	- Branch Specifier: */jenkins
	- Script Path: app/Jenkinsfile
	Save

I have used the architecture jenkinscontroller and jenkins agent are on 2 different EC2 instances, on the same subnet.
- I used Ubuntu Server 24.04 LTS AMI
- Setup Jenkins Controller
	1. Update the System and Install Java 
		```bash
			sudo apt update && sudo apt upgrade -y
			sudo apt install openjdk-17-jdk -y
			java -version
		```
	2. Add the Jenkins Repository and GPG Key 
		```bash
			curl -fsSL https://pkg.jenkins.io/debian-stable/jenkins.io-2023.key | sudo tee \
			/usr/share/keyrings/jenkins-keyring.asc > /dev/null
			echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
			https://pkg.jenkins.io/debian-stable binary/ | sudo tee \
			/etc/apt/sources.list.d/jenkins.list > /dev/null
			sudo apt update
		```
	3. Install Jenkins
		```bash
			sudo apt install jenkins -y
		```
	4. Manage the Jenkins Service and Firewall 
		```bash
			sudo systemctl start jenkins
			sudo systemctl enable jenkins
			sudo systemctl status jenkins
		```
	5. Access the Jenkins Web Interface 
		```bash
			sudo cat /var/lib/jenkins/secrets/initialAdminPassword
		```

- To install Git on Ubuntu Server 24.04 LTS using the apt package manager, follow these steps: 
	1. Update the system packages
		```bash
	sudo apt update && sudo apt upgrade -y

	2. Install Git 
	sudo apt install git -y

	3. Verify the installation
	git --version

	4. Configure Git
	git config --global user.name "SaifKbishi"
	git config --global user.email "saifkbishi@gmail.com"

	5. Confirm your configuration
	git config --global --list

	- Follow this article to set up Jenkins Agent Using SSH keys
		https://devopscube.com/setup-slaves-on-jenkins-2/#setup-jenkins-agentsslaves-on-jenkins


	- Setup Jenkins agent
		Setting up Jenkins Agent Using SSH keys

		1. Update the System and Install Java 
		```bash
			sudo apt update && sudo apt upgrade -y
			sudo apt install openjdk-17-jdk -y
			java -version
		```

		2. install Docker
		```bash
			sudo apt update && sudo apt upgrade -y
			sudo apt install apt-transport-https ca-certificates curl software-properties-common gnupg -y
		```

		2.1 Add Docker's official GPG key:
		```bash
			curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
		```

		2.2 Set up the Docker repository:
		```bash
			echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu noble stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
		```

		2.3 Update the package index:
		```bash
			sudo apt update
		```

		2.4 Install Docker Engine:
		```bash
			sudo apt install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin -y
		```

		2.5 Verify the installation:
		```bash
			sudo systemctl status docker
			sudo docker run hello-world
		```

		3. Install Git
		4. Install Minikube

- Parameters you need to choose
	Branch to checkout: jenkins
	Dokerfile path: app/Dockerfile
	Docker hub namespace: saifkbishi
	Image name in Docker hub: devops_k8s_phase2
	IMAGE_TAG: 3.0.0
	Container port: 8080
	HTTP healthcheck: /health
	Helm release name: phase3
	Docker hub credintials: docker-hub-saif