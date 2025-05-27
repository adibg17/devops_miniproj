# Complete Deployment Instructions for Portfolio App

This guide will walk you through setting up, building, and deploying your Flask portfolio app using Docker, Kubernetes (with Minikube), and Jenkins for CI/CD. All commands are for Windows PowerShell, but can be adapted for other OSes.

---

## 1. Prerequisites
- **Git**: [Download & Install](https://git-scm.com/download/win)
- **Python 3.8+**: [Download & Install](https://www.python.org/downloads/)
- **Docker Desktop**: [Download & Install](https://www.docker.com/products/docker-desktop/)
- **kubectl**: [Install Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-windows/)
- **Minikube**: [Install Guide](https://minikube.sigs.k8s.io/docs/start/)
- **Jenkins**: [Download & Install](https://www.jenkins.io/download/)
- **A DockerHub account**: [Sign Up](https://hub.docker.com/)

---

## 2. Local Development
1. Clone the repository:
   ```powershell
   git clone <your-repo-url>
   cd <repo-folder>
   ```
2. (Optional) Create and activate a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the app locally:
   ```powershell
   python app.py
   ```
   Visit [http://localhost:5000](http://localhost:5000)

---

## 3. Dockerize the App
1. Build the Docker image:
   ```powershell
   docker build -t portfolio-app .
   ```
2. Test the image locally:
   ```powershell
   docker run -p 5000:5000 portfolio-app
   ```
   Visit [http://localhost:5000](http://localhost:5000)

---

## 4. Push Docker Image to DockerHub
1. Log in to DockerHub:
   ```powershell
   docker login
   ```
2. Tag your image:
   ```powershell
   docker tag portfolio-app <your-dockerhub-username>/portfolio-app:latest
   ```
3. Push the image:
   ```powershell
   docker push <your-dockerhub-username>/portfolio-app:latest
   ```

---

## 5. Set Up Minikube (Kubernetes Locally)
1. Start Minikube (choose a driver, e.g., virtualbox or hyperv):
   ```powershell
   minikube start --driver=virtualbox
   # or
   minikube start --driver=hyperv
   ```
2. Check status:
   ```powershell
   minikube status
   kubectl get nodes
   ```

---

## 6. Deploy to Kubernetes
1. Edit `k8s-deployment.yaml`:
   - Ensure the image field is:
     ```yaml
     image: <your-dockerhub-username>/portfolio-app:latest
     ```
2. Apply the deployment and service:
   ```powershell
   kubectl apply -f k8s-deployment.yaml
   ```
3. Check pod and service status:
   ```powershell
   kubectl get pods
   kubectl get svc
   ```
4. Get the Minikube IP:
   ```powershell
   minikube ip
   ```
5. Access your app:
   - If using NodePort (e.g., 30080):
     - Visit: `http://<minikube-ip>:30080`

---

## 7. Jenkins CI/CD Pipeline
1. Install Jenkins and required plugins (Docker, Kubernetes CLI, Git).
2. Add DockerHub credentials in Jenkins (e.g., ID: `dockerhub-creds`).
3. Create a new Pipeline job and use the provided `Jenkinsfile`.
4. The Jenkinsfile should:
   - Build the Docker image
   - Push to DockerHub
   - Deploy to Kubernetes using `kubectl apply -f k8s-deployment.yaml`
5. Trigger a build by pushing code or manually starting the job.

---

## 8. Troubleshooting
- **Pod stuck in ImagePullBackOff:**
  - Check image name in `k8s-deployment.yaml`.
  - Ensure image is public or configure imagePullSecrets for private repos.
- **App not accessible:**
  - Check pod and service status.
  - Ensure you are using the correct Minikube IP and NodePort.

---

## 9. Useful Commands
- View logs:
  ```powershell
  kubectl logs <pod-name>
  ```
- Delete a pod (it will restart):
  ```powershell
  kubectl delete pod <pod-name>
  ```
- Update deployment after changes:
  ```powershell
  kubectl apply -f k8s-deployment.yaml
  ```

---

## 10. Endpoints
- `/` - Portfolio form
- `/submit` - POST endpoint to save contact
- `/contacts` - See all contact submissions

---
