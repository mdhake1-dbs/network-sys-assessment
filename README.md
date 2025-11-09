## 📘 Project Summary (Short Version)

**Automated Container Deployment and Administration in the Cloud** is a DevOps automation project that demonstrates the integration of **Terraform**, **Ansible**, **Docker**, and **GitHub Actions** for cloud-based application deployment on **AWS EC2**.  

The project provisions cloud infrastructure automatically, configures servers, and deploys a containerized **Flask web application** through a fully automated **CI/CD pipeline**.  
Each tool plays a specific role in the workflow:

- **Terraform** provisions AWS infrastructure using Infrastructure-as-Code (IaC).  
- **Ansible** manages configuration and installs Docker on the remote instance.  
- **Docker** encapsulates the Flask app for consistent, portable execution.  
- **GitHub Actions** automates build, test, and deployment workflows upon each code push.  

This architecture minimizes manual intervention, enhances reproducibility, and embodies key **DevOps principles**—automation, scalability, and reliability. The inclusion of shell scripting (`ec2_setup.sh`) bridges automation layers for a seamless one-command deployment.  

Security is enforced through encrypted GitHub secrets, SSH key management, and network access control, while cost optimization is achieved through automatic container shutdowns.  

The solution provides a **reusable blueprint** for academic, research, and industry environments aiming to implement modern DevOps pipelines using open-source technologies.  

---
# 🚀 Automated Container Deployment and Administration in the Cloud

This project automates the end-to-end deployment of a containerized web application on **AWS EC2** using a combination of **Terraform**, **Ansible**, **Docker**, and **GitHub Actions**.  
It demonstrates a modern **Infrastructure-as-Code (IaC)** and **DevOps** pipeline that provisions cloud infrastructure, configures the environment, deploys a containerized Flask app, and manages continuous integration and delivery (CI/CD).

---

## 🧩 Architecture Overview

The system consists of four automation layers:

1. **Infrastructure Layer (Terraform):** Provisions AWS EC2 instance, SSH key, and security groups.  
2. **Configuration Layer (Ansible):** Installs Docker, sets permissions, and deploys containers.  
3. **Application Layer (Docker):** Runs a Flask app container exposing port 80.  
4. **Pipeline Layer (GitHub Actions):** Automates build, push, and deploy on every code commit.  

**Figure 1 – Overall System Architecture Diagram**  
*(Refer to `/docs/architecture.png` or included project images.)*

---

## 🏗️ Tech Stack

- **Cloud:** AWS (EC2, Security Groups, Key Pairs)  
- **IaC:** Terraform  
- **Configuration Management:** Ansible  
- **Containerization:** Docker  
- **CI/CD:** GitHub Actions  
- **OS:** Ubuntu (LTS)  
- **Language:** Python (Flask web app)  

---

## 📁 Repository Structure

```
├── app/
│   ├── app.py               # Flask application source
│   ├── requirements.txt     # Python dependencies
│   └── Dockerfile           # Container image definition
│
├── terraform/
│   ├── main.tf              # Infrastructure provisioning (EC2, Security Groups)
│   ├── variables.tf         # Terraform input variables
│   └── outputs.tf           # Outputs (e.g., public IP)
│
├── ansible/
│   ├── playbook.yml         # Configuration playbook for Docker & app deployment
│   └── hosts.ini            # Dynamic inventory file
│
├── .github/workflows/
│   └── ci-cd.yml            # GitHub Actions workflow for CI/CD
│
├── ec2_setup.sh             # Shell script to run Terraform + Ansible sequentially
├── README.md                # Project documentation (this file)
└── docs/                    # Architecture diagrams (optional)
```

---

## ⚙️ Deployment Workflow

The project follows an automated workflow from provisioning to deployment:

1. **Terraform** provisions the EC2 instance and outputs its IP.  
2. **Shell Script (`ec2_setup.sh`)** retrieves the IP and updates Ansible’s inventory.  
3. **Ansible** installs Docker and runs the Flask container.  
4. **GitHub Actions** automates Docker image build, push to DockerHub, and redeployment.  

---

## 🚀 Setup and Usage

### **1. Clone the Repository**
```bash
git clone https://github.com/<your-username>/network-sys-assessment.git
cd network-sys-assessment
```

### **2. Configure AWS Credentials**
Ensure your AWS CLI or Terraform environment has valid credentials:
```bash
aws configure
```

### **3. Deploy Infrastructure**
```bash
cd terraform
terraform init
terraform apply -auto-approve
```

### **4. Configure and Deploy the Application**
After Terraform finishes, run:
```bash
cd ..
bash ec2_setup.sh
```

This will:
- Extract the EC2 public IP  
- Update the Ansible inventory  
- Run the Ansible playbook  
- Install Docker and deploy the container automatically  

### **5. Access the Web Application**
Visit your EC2 instance’s public IP on port **80**:  
`http://<EC2-PUBLIC-IP>`

---

## 🔄 CI/CD Pipeline

GitHub Actions automates build and deployment with every code commit.

### Workflow Highlights (`.github/workflows/ci-cd.yml`):
- Triggers on every push to the `main` branch.  
- Builds Docker image from `/app` and pushes it to DockerHub.  
- SSHs into the EC2 instance to pull the latest image and restart the container.

```yaml
on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: docker/login-action@v3
      - uses: docker/build-push-action@v5
      - name: Deploy to EC2
        uses: appleboy/ssh-action@v1.0.0
```

### Required GitHub Secrets:
| Key | Description |
|------|-------------|
| `AWS_ACCESS_KEY_ID` | AWS Access Key |
| `AWS_SECRET_ACCESS_KEY` | AWS Secret Key |
| `EC2_HOST` | Public IP or DNS of EC2 |
| `EC2_PRIVATE_KEY` | SSH private key for access |
| `DOCKERHUB_USERNAME` | DockerHub username |
| `DOCKERHUB_TOKEN` | DockerHub access token |

---

## 🧰 Shell Script: `ec2_setup.sh`

This script connects Terraform and Ansible for seamless orchestration:
```bash
#!/bin/bash
cd terraform
terraform init && terraform apply -auto-approve
IP=$(terraform output -raw instance_public_ip)
cd ../ansible
sed -i "s/your_instance_ip/$IP/g" hosts.ini
ansible-playbook -i hosts.ini playbook.yml
```
It ensures Ansible always targets the correct EC2 instance without manual updates.

---

## 🛡️ Security and Cost Management

- **SSH Keys:** Managed via AWS Key Pairs and GitHub Secrets.  
- **Security Groups:** Allow inbound SSH (22) and HTTP (80) only.  
- **Instance Shutdown:** Container auto-stops after 4 hours (via Ansible `at` scheduling).  
- **Secrets:** Stored securely in GitHub Actions secrets manager.  

---

## 📈 Performance Metrics

| Metric | Average Value | Description |
|--------|----------------|-------------|
| Infrastructure Provisioning | 2–3 min | Terraform EC2 instance creation |
| Configuration | 1–2 min | Ansible Docker installation & setup |
| CI/CD Deployment | ~2 min | GitHub Actions build & deploy |
| Total Automation Time | < 7 min | Full end-to-end process |

**Figure 4 – Performance Metrics Overview**

---

## 🧩 Future Improvements

- Add **AWS ECS** or **Kubernetes** for container orchestration.  
- Implement **Prometheus & Grafana** for monitoring and alerting.  
- Add **automated testing** stages in the CI/CD pipeline.  
- Store secrets using **AWS Systems Manager Parameter Store**.  
- Integrate **auto-scaling groups** for production-grade workloads.  

---

## 👨‍💻 Author

**Developed by:** [Your Name]  
**Module:** B9IS121 – Network Systems and Administration CA 2025  
**Instructor:** Kingsley Ibomo  

---

## 📚 References
- [Terraform Documentation](https://developer.hashicorp.com/terraform)  
- [Ansible Documentation](https://docs.ansible.com/)  
- [Docker Documentation](https://docs.docker.com/)  
- [GitHub Actions Docs](https://docs.github.com/en/actions)  
- [AWS EC2 Guide](https://docs.aws.amazon.com/ec2/)
