#!/bin/bash
# This script verifies GitHub token, remote URL, and push permissions

set -e

# Load credentials
if [ ! -f github_credentials.env ]; then
    echo "❌ github_credentials.env not found!"
    exit 1
fi
source github_credentials.env

# Navigate to project
cd network-sys-assessment || { echo "❌ Project folder not found"; exit 1; }

# 1️⃣ Check if Git repo exists
if [ ! -d .git ]; then
    echo "❌ Git is not initialized in this folder."
    exit 1
else
    echo "✅ Git repository detected."
fi

# 2️⃣ Check remote origin
REMOTE_URL=$(git remote get-url origin 2>/dev/null || echo "")
if [ -z "$REMOTE_URL" ]; then
    echo "❌ Git remote 'origin' is not set."
else
    echo "✅ Git remote URL found: $REMOTE_URL"
fi

# 3️⃣ Test GitHub token via API
echo "🔍 Testing GitHub token..."
TOKEN_TEST=$(curl -s -o /dev/null -w "%{http_code}" -u ${GITHUB_USERNAME}:${GITHUB_TOKEN} https://api.github.com/user)

if [ "$TOKEN_TEST" -eq 200 ]; then
    echo "✅ GitHub token is valid for user $GITHUB_USERNAME"
else
    echo "❌ GitHub token is invalid or expired (HTTP $TOKEN_TEST)"
    exit 1
fi

# 4️⃣ Test push permission (dry-run)
echo "🔍 Testing push permission..."
git fetch origin main >/dev/null 2>&1 || echo "⚠️ Could not fetch main branch; repo may be empty."

PUSH_TEST=$(git push --dry-run origin main 2>&1 || echo "")
if [[ "$PUSH_TEST" == *"permission"* || "$PUSH_TEST" == *"denied"* ]]; then
    echo "❌ You do NOT have write access to the repository."
else
    echo "✅ You have write access to the repository (dry-run successful)."
fi

echo "✅ Git setup verification complete!"

