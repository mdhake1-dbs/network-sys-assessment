#!/bin/bash

# Create folders
mkdir -p network-sys-assessment/{terraform,ansible,app,.github/workflows}

# Create files
touch network-sys-assessment/README.md
touch network-sys-assessment/report.pdf
touch network-sys-assessment/terraform/{main.tf,variables.tf,outputs.tf}
touch network-sys-assessment/ansible/{hosts.ini,playbook.yml}
touch network-sys-assessment/app/{app.py,requirements.txt,Dockerfile}
touch network-sys-assessment/.github/workflows/ci-cd.yml

echo "Folder structure created successfully!"

