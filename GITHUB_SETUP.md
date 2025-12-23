# GitHub Setup Guide

This guide will help you publish this plugin to your GitHub account.

## Prerequisites

- A GitHub account ([Sign up here](https://github.com/join))
- Git installed on your computer
- This plugin folder downloaded

## Step-by-Step Setup

### 1. Customize the Plugin Files

Before pushing to GitHub, you need to update files with your information:

#### Option A: Use the Setup Script (Easiest)

```bash
cd OctoPrint-AnycubicFilamentRunoutMonitor
./setup_repo.sh
```

The script will ask for your GitHub username and email, then automatically update all files.

#### Option B: Manual Updates

Edit these files and replace the placeholders:

1. **README.md** - Replace `YOUR_GITHUB_USERNAME` with your GitHub username
2. **setup.py** - Replace:
   - `YOUR_GITHUB_USERNAME` with your GitHub username
   - `your-email@example.com` with your email
3. **octoprint_anycubicfilamentrunout/__init__.py** - Replace `YOUR_GITHUB_USERNAME`
4. **INSTALLATION.md** - Replace `YOUR_GITHUB_USERNAME`

### 2. Create GitHub Repository

1. Go to [GitHub](https://github.com)
2. Click the **"+"** icon in the top right
3. Select **"New repository"**
4. Set repository name to: `OctoPrint-AnycubicFilamentRunoutMonitor`
5. Add description: `OctoPrint plugin for monitoring Anycubic printer filament runouts`
6. Make it **Public**
7. **DO NOT** check "Initialize with README" (we already have one)
8. Click **"Create repository"**

### 3. Push Your Code to GitHub

Open terminal in the plugin folder and run:

```bash
# Initialize git repository (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit - Anycubic Filament Runout Monitor"

# Rename branch to main
git branch -M main

# Add remote repository (replace YOUR_USERNAME with your GitHub username)
git remote add origin https://github.com/YOUR_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor.git

# Push to GitHub
git push -u origin main
```

### 4. Verify Upload

1. Go to your repository: `https://github.com/YOUR_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor`
2. You should see all the plugin files
3. The README.md will display on the main page

## Using Your Plugin

### Installation URL

Share this URL for direct installation:
```
https://github.com/YOUR_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/main.zip
```

Users can install it in OctoPrint:
1. Settings → Plugin Manager
2. "Get More..." → "... from URL"
3. Paste your URL
4. Click "Install"

### Clone URL

For development:
```bash
git clone https://github.com/YOUR_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor.git
```

## Making Updates

After making changes to the plugin:

```bash
# Stage changes
git add .

# Commit with a message
git commit -m "Description of your changes"

# Push to GitHub
git push
```

## Creating Releases

### 1. Update Version

Edit `setup.py` and change the version number:
```python
plugin_version = "1.0.1"  # Increment this
```

### 2. Update CHANGELOG.md

Add your changes to `CHANGELOG.md`:
```markdown
## [1.0.1] - 2024-12-24
### Fixed
- Fixed bug with detection message
```

### 3. Commit and Push

```bash
git add setup.py CHANGELOG.md
git commit -m "Release v1.0.1"
git push
```

### 4. Create GitHub Release

1. Go to your repository on GitHub
2. Click **"Releases"** on the right side
3. Click **"Create a new release"**
4. Click **"Choose a tag"** and type: `v1.0.1`
5. Click **"Create new tag: v1.0.1 on publish"**
6. Release title: `v1.0.1`
7. Description: Copy the changes from CHANGELOG.md
8. Click **"Publish release"**

The release will create a downloadable `.zip` file automatically.

## Submitting to OctoPrint Plugin Repository

To make your plugin searchable in OctoPrint's Plugin Manager:

1. Fork the plugin repository: https://github.com/OctoPrint/plugins.octoprint.org
2. Add a file: `_plugins/anycubicfilamentrunout.md`
3. Create a pull request

See: https://plugins.octoprint.org/help/registering/

## Repository Settings

### Enable Issues

1. Go to your repository settings
2. Under "Features", enable **Issues**
3. Users can now report bugs and request features

### Add Topics

Add these topics to help others find your plugin:
- `octoprint-plugin`
- `anycubic`
- `filament-runout`
- `3d-printing`

To add topics:
1. Click the gear icon next to "About" on your repo page
2. Add topics in the "Topics" field

## Getting Help

- [GitHub Docs](https://docs.github.com)
- [Git Basics](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics)
- [Creating Releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository)

## Quick Reference

```bash
# Check status
git status

# View commit history
git log

# Create new branch
git checkout -b feature-name

# Switch branches
git checkout main

# Pull latest changes
git pull

# View remote URL
git remote -v
```
