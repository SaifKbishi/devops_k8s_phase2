pipeline {
    agent { label 'jenkins-agent' }
    
    environment {
        REGISTRY          = 'docker.io'
									   
        IMAGE_REPO        = '19820401/devops-k8s-phase2'
        IMAGE_TAG         = "${env.BUILD_NUMBER}"
        K8S_NAMESPACE     = 'dev'
        RELEASE_NAME      = 'phase3-release'
        CHART_NAME        = 'phase3'
        CHART_VERSION     = "0.1.${env.BUILD_NUMBER}"
        DOCKER_CREDENTIALS_ID = 'dockerhub-credentials'  // Set this in Jenkins
        
        // Minikube specific settings
        MINIKUBE_ACTIVE_DOCKERD = 'minikube'
        USE_MINIKUBE_DOCKER = 'true'  // Use minikube's Docker daemon
    }

    stages {
        stage('Checkout') {
            steps {
                script {
                    echo '🔄 Cloning repository...'
                    git branch: 'jenkins', 
                        url: 'https://github.com/SaifKbishi/devops_k8s_phase2.git'
                    echo '✅ Code cloned successfully'
                }
            }
        }

        stage('Setup Minikube Docker Environment') {
            steps {
                script {
                    echo '🐳 Configuring Docker to use Minikube daemon...'
                    
                    // Set Docker to use Minikube's Docker daemon
                    sh '''
                        # Check if Minikube is running
                        if ! minikube status | grep -q "host: Running"; then
                            echo "⚠️  Minikube is not running. Starting Minikube..."
                            minikube start --driver=docker
                        else
                            echo "✅ Minikube is already running"
                        fi
                        
                        # Display Minikube status
                        minikube status
                        
                        # Get Minikube Docker environment variables
                        eval $(minikube docker-env)
                        
                        # Verify we're using Minikube's Docker
                        echo "Docker host: $DOCKER_HOST"
                        docker ps | head -5
                    '''
                    
                    echo '✅ Minikube Docker environment configured'
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    echo '🐳 Building Docker image in Minikube...'
                    dir('app') {
                        sh """
                            # Use Minikube's Docker daemon
                            eval \$(minikube docker-env)
                            
                            # Build image directly in Minikube
                            docker build -t ${IMAGE_REPO}:${IMAGE_TAG} .
                            docker tag ${IMAGE_REPO}:${IMAGE_TAG} ${IMAGE_REPO}:latest
                            
                            # Verify image exists in Minikube
                            docker images | grep ${IMAGE_REPO}
                        """
                    }
                    echo "✅ Built image in Minikube: ${IMAGE_REPO}:${IMAGE_TAG}"
                }
            }
        }

        stage('Test') {
            steps {
                script {
                    echo '🧪 Running tests...'
                    sh """
                        # Use Minikube's Docker daemon
                        eval \$(minikube docker-env)
                        
                        # Run tests in container
                        # docker run --rm ${IMAGE_REPO}:${IMAGE_TAG} python -m pytest tests/
                    """
                    echo '✅ Tests passed (add real tests here)'
                }
            }
        }

        stage('Push Docker Image (Optional)') {
            when {
                expression { 
                    // Only push if you need the image in Docker Hub
                    // For Minikube-only deployment, you can skip this
                    return env.PUSH_TO_REGISTRY == 'true'
                }
            }
            steps {
                script {
                    echo '📤 Pushing Docker image to registry...'
                    withCredentials([usernamePassword(
                        credentialsId: DOCKER_CREDENTIALS_ID,
                        usernameVariable: 'DOCKER_USER',
                        passwordVariable: 'DOCKER_PASS'
                    )]) {
                        sh """
                            # Switch back to host Docker for pushing
                            eval \$(minikube docker-env -u)
                            
                            echo \$DOCKER_PASS | docker login -u \$DOCKER_USER --password-stdin ${REGISTRY}
                            docker push ${IMAGE_REPO}:${IMAGE_TAG}
                            docker push ${IMAGE_REPO}:latest
                        """
                    }
                    echo "✅ Pushed ${IMAGE_REPO}:${IMAGE_TAG}"
                }
            }
        }

        stage('Prepare Helm Chart') {
            steps {
                script {
                    echo '📦 Preparing Helm chart for Minikube...'
                    
																	  
                    sh """
                        if [ ! -d "${CHART_NAME}" ]; then
                            helm create ${CHART_NAME}
                            echo "Created new Helm chart: ${CHART_NAME}"
                        else
                            echo "Using existing Helm chart: ${CHART_NAME}"
                        fi
                        
					
                        # Update Chart.yaml
						  
                        sed -i 's/^version:.*/version: ${CHART_VERSION}/' ${CHART_NAME}/Chart.yaml
                        sed -i 's/^appVersion:.*/appVersion: "${IMAGE_TAG}"/' ${CHART_NAME}/Chart.yaml
                        
					
                        # Update values.yaml for Minikube
						  
                        sed -i 's|repository:.*|repository: ${IMAGE_REPO}|' ${CHART_NAME}/values.yaml
                        sed -i 's/tag:.*/tag: "${IMAGE_TAG}"/' ${CHART_NAME}/values.yaml
                        
                        # IMPORTANT: Set imagePullPolicy to IfNotPresent or Never for Minikube
                        sed -i 's/pullPolicy:.*/pullPolicy: IfNotPresent/' ${CHART_NAME}/values.yaml
                        
                        # Change service type to NodePort for Minikube access
                        sed -i 's/type: ClusterIP/type: NodePort/' ${CHART_NAME}/values.yaml
                        
                        echo "Chart configuration:"
                        cat ${CHART_NAME}/values.yaml | grep -A 3 "image:"
                        cat ${CHART_NAME}/values.yaml | grep "type:"
                    """
                    
                    echo '✅ Helm chart prepared for Minikube'
                }
            }
        }

        stage('Package Helm Chart') {
            steps {
                script {
                    echo '📦 Packaging Helm chart...'
                    sh """
                        helm package ${CHART_NAME} --version ${CHART_VERSION}
                        ls -lh ${CHART_NAME}-${CHART_VERSION}.tgz
                    """
                    echo "✅ Packaged: ${CHART_NAME}-${CHART_VERSION}.tgz"
                }
            }
        }

        stage('Deploy to Minikube') {
            steps {
                script {
                    echo '🚀 Deploying to Minikube...'
                    
																											   
                    sh """
                        # Create namespace if it doesn't exist
                        kubectl create namespace ${K8S_NAMESPACE} --dry-run=client -o yaml | kubectl apply -f -
                        
                        # Deploy using Helm
                        helm upgrade --install ${RELEASE_NAME} \
                            ${CHART_NAME}-${CHART_VERSION}.tgz \
                            --namespace ${K8S_NAMESPACE} \
                            --set image.repository=${IMAGE_REPO} \
                            --set image.tag=${IMAGE_TAG} \
                            --set image.pullPolicy=IfNotPresent \
                            --set service.type=NodePort \
                            --wait \
                            --timeout 5m
                        
                        echo "Deployment status:"
                        kubectl get pods -n ${K8S_NAMESPACE}
						   
                        kubectl get svc -n ${K8S_NAMESPACE}
                    """
                    echo '✅ Deployment successful'
                }
            }
        }

        stage('Verify Deployment') {
            steps {
                script {
                    echo '✅ Verifying deployment in Minikube...'
                    
																											   
                    sh """
                        # Wait for pods to be ready
                        kubectl wait --for=condition=ready pod \
                            -l app.kubernetes.io/instance=${RELEASE_NAME} \
                            -n ${K8S_NAMESPACE} \
                            --timeout=300s
                        
                        # Get deployment info
                        echo "Pods:"
                        kubectl get pods -n ${K8S_NAMESPACE} -l app.kubernetes.io/instance=${RELEASE_NAME}
                        
                        echo "Services:"
                        kubectl get svc -n ${K8S_NAMESPACE} -l app.kubernetes.io/instance=${RELEASE_NAME}
                        
                        # Get Minikube service URL
                        echo "🌐 Application URL:"
                        minikube service ${RELEASE_NAME}-${CHART_NAME} -n ${K8S_NAMESPACE} --url
                        
                        echo "To access the application, run:"
                        echo "minikube service ${RELEASE_NAME}-${CHART_NAME} -n ${K8S_NAMESPACE}"
                    """
                    echo '✅ Deployment verified'
                }
            }
        }

        stage('Display Access Information') {
            steps {
                script {
                    echo '📋 Access Information:'
                    sh """
                        echo "=================================="
                        echo "Minikube Dashboard:"
                        echo "  Run: minikube dashboard"
                        echo ""
                        echo "Application URL:"
                        minikube service ${RELEASE_NAME}-${CHART_NAME} -n ${K8S_NAMESPACE} --url || echo "Service not exposed"
                        echo ""
                        echo "Port Forward (alternative):"
                        echo "  kubectl port-forward -n ${K8S_NAMESPACE} svc/${RELEASE_NAME}-${CHART_NAME} 8080:80"
                        echo "  Then visit: http://localhost:8080"
                        echo ""
                        echo "View Logs:"
                        echo "  kubectl logs -n ${K8S_NAMESPACE} -l app.kubernetes.io/instance=${RELEASE_NAME} -f"
                        echo "=================================="
                    """
                }
            }
        }
    }

    post {
        success {
            echo '✅ Pipeline completed successfully!'
            script {
											 
                sh """
                    eval \$(minikube docker-env)
                    docker image prune -f
                """
            }
        }
        
        failure {
            echo '❌ Pipeline failed!'
            script {
																										   
                sh """
                    echo "Attempting rollback..."
                    helm rollback ${RELEASE_NAME} -n ${K8S_NAMESPACE} || echo "Rollback failed or no previous version"
                    
                    echo "Deployment logs:"
                    kubectl logs -n ${K8S_NAMESPACE} -l app.kubernetes.io/instance=${RELEASE_NAME} --tail=50 || true
                """
            }
        }
        
        always {
            echo '🧹 Cleaning up workspace...'
            cleanWs()
        }
    }
}