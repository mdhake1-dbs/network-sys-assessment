#!/bin/bash

# This script sets up git, initializes repo, and connects it to GitHub

set -e  # exit if any command fails

# Load credentials
if [ ! -f github_credentials.env ]; then
  echo "❌ github_credentials.env not found! Create it first."
  exit 1
fi
source github_credentials.env

# Navigate to your project folder
cd $HOME/networks_ca_1/network-sys-assessment || exit 1

# Initialize Git
git init

# Set Git config (you can customize your name/email)
git config user.name "$GITHUB_USERNAME"
git config user.email "${GITHUB_USERNAME}@users.noreply.github.com"

# Add remote repository
REMOTE_URL="https://${GITHUB_USERNAME}:${GITHUB_TOKEN}@github.com/${GITHUB_USERNAME}/${REPO_NAME}.git"

if git remote | grep -q origin; then
  git remote set-url origin "$REMOTE_URL"
else
  git remote add origin "$REMOTE_URL"
fi

echo "✅ Git initialized and remote configured for $REPO_NAME"

