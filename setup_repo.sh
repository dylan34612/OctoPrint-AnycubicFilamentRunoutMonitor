#!/bin/bash

# Setup script for Anycubic Filament Runout Monitor GitHub repository
# This script will help you set up the repository and push to GitHub

echo "=================================="
echo "Anycubic Filament Runout Monitor"
echo "GitHub Repository Setup"
echo "=================================="
echo ""

# Check if git is installed
if ! command -v git &> /dev/null; then
    echo "Error: git is not installed. Please install git first."
    exit 1
fi

# Get GitHub username
read -p "Enter your GitHub username: " GITHUB_USERNAME
if [ -z "$GITHUB_USERNAME" ]; then
    echo "Error: GitHub username cannot be empty"
    exit 1
fi

echo ""
echo "Updating files with your GitHub username..."

# Update README.md
sed -i "s/YOUR_GITHUB_USERNAME/$GITHUB_USERNAME/g" README.md
sed -i "s/YOUR_USERNAME/$GITHUB_USERNAME/g" README.md

# Update setup.py
sed -i "s/YOUR_GITHUB_USERNAME/$GITHUB_USERNAME/g" setup.py
read -p "Enter your email address: " EMAIL
sed -i "s/your-email@example.com/$EMAIL/g" setup.py

# Update __init__.py
sed -i "s/YOUR_GITHUB_USERNAME/$GITHUB_USERNAME/g" octoprint_anycubicfilamentrunout/__init__.py

# Update INSTALLATION.md
sed -i "s/YOUR_GITHUB_USERNAME/$GITHUB_USERNAME/g" INSTALLATION.md

echo "Files updated successfully!"
echo ""

# Initialize git repository
if [ ! -d ".git" ]; then
    echo "Initializing git repository..."
    git init
    git add .
    git commit -m "Initial commit - Anycubic Filament Runout Monitor"
    echo "Git repository initialized!"
else
    echo "Git repository already exists."
fi

echo ""
echo "=================================="
echo "Next Steps:"
echo "=================================="
echo ""
echo "1. Create a new repository on GitHub:"
echo "   - Go to: https://github.com/new"
echo "   - Repository name: OctoPrint-AnycubicFilamentRunoutMonitor"
echo "   - Make it public"
echo "   - Do NOT initialize with README, .gitignore, or license"
echo ""
echo "2. After creating the repository, run these commands:"
echo ""
echo "   git branch -M main"
echo "   git remote add origin https://github.com/$GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor.git"
echo "   git push -u origin main"
echo ""
echo "3. Your plugin will be available at:"
echo "   https://github.com/$GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor"
echo ""
echo "4. To install directly from GitHub:"
echo "   https://github.com/$GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/main.zip"
echo ""
