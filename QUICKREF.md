# Quick Reference Card

## Installation

**Direct URL for OctoPrint:**
```
https://github.com/YOUR_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/main.zip
```

## Default Settings

**Detection Message:**
```
echo:Insert filament and send M108
```

## Troubleshooting Commands

### Enable Debug Logging
1. Settings → Logging
2. Add component: `octoprint.plugins.anycubicfilamentrunout`
3. Level: DEBUG

### View Live Logs
```bash
tail -f ~/.octoprint/logs/octoprint.log | grep anycubicfilamentrunout
```

### Test Detection
1. Start a print
2. Open Terminal tab
3. Trigger filament runout
4. Look for: `echo:Insert filament and send M108`

## Git Commands

### Initial Setup
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor.git
git push -u origin main
```

### Making Updates
```bash
git add .
git commit -m "Description of changes"
git push
```

### Create Release
1. Update version in `setup.py`
2. Update `CHANGELOG.md`
3. Commit and push
4. Create release on GitHub with tag `vX.X.X`

## File Structure
```
OctoPrint-AnycubicFilamentRunoutMonitor/
├── octoprint_anycubicfilamentrunout/
│   ├── __init__.py                    # Main plugin code
│   ├── static/js/
│   │   └── anycubicfilamentrunout.js # Frontend code
│   └── templates/
│       └── anycubicfilamentrunout_settings.jinja2  # Settings UI
├── setup.py                           # Installation config
├── README.md                          # Main documentation
├── INSTALLATION.md                    # Setup guide
├── GITHUB_SETUP.md                    # GitHub publishing guide
├── CHANGELOG.md                       # Version history
└── LICENSE                            # AGPL v3 license
```

## Important Placeholders to Replace

Before publishing, replace these in all files:
- `YOUR_GITHUB_USERNAME` → Your GitHub username
- `your-email@example.com` → Your email address
- `YOUR_USERNAME` → Your GitHub username (in some files)

**Tip:** Use the `setup_repo.sh` script to do this automatically!

## Support Resources

- **GitHub Issues:** https://github.com/YOUR_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/issues
- **OctoPrint Forum:** https://community.octoprint.org
- **Original Plugin:** https://github.com/jneilliii/OctoPrint-PrusaFilamentRunoutMonitor

## Testing Checklist

- [ ] Plugin installs without errors
- [ ] Settings page appears correctly
- [ ] Terminal shows filament runout message
- [ ] Plugin detects runout and pauses print
- [ ] Notification popup appears
- [ ] Debug logs show detection
- [ ] Resume works correctly after filament change

## Common Terminal Messages

**Successful detection:**
```
Recv: echo:Insert filament and send M108
INFO - Anycubic filament runout detected
INFO - Firing pause on event bus
```

**Temperature monitoring (normal):**
```
Recv: T:210.03 /210.00 B:53.03 /53.00
```

**Position report (normal during runout):**
```
Recv: X:5.00 Y:88.41 Z:10.10 E:153.52
```
