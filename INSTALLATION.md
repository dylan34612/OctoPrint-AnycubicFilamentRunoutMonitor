# Installation & Setup Guide

This guide will walk you through installing the Anycubic Filament Runout Monitor plugin for OctoPrint.

## Quick Install

### Method 1: Via Plugin Manager (When Published)

1. Open OctoPrint web interface
2. Click on the wrench icon (⚙️) to open Settings
3. Navigate to **Plugin Manager**
4. Click **"Get More..."**
5. Search for **"Anycubic Filament Runout"**
6. Click **"Install"**
7. Restart OctoPrint when prompted

### Method 2: Manual Install from GitHub

1. Open OctoPrint Settings
2. Go to **Plugin Manager**
3. Click **"Get More..."**
4. Paste this URL in the "... from URL" field:
   ```
   https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/main.zip
   ```
5. Click **"Install"**
6. Restart OctoPrint

### Method 3: Command Line Install

SSH into your OctoPrint server and run:

```bash
~/oprint/bin/pip install https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/main.zip
```

Then restart OctoPrint:
```bash
sudo service octoprint restart
```

## Initial Configuration

### Step 1: Access Plugin Settings

1. Open OctoPrint Settings (⚙️)
2. Scroll down to **Anycubic Filament Runout** in the left sidebar
3. You should see the plugin settings page

### Step 2: Verify Detection Message

The default detection message is:
```
echo:Insert filament and send M108
```

This works for most Anycubic printers. If your printer uses a different message, continue to Step 3.

### Step 3: Test Filament Runout Detection

1. Load a small test print
2. Open the **Terminal** tab in OctoPrint
3. Start the print
4. Manually trigger a filament runout (remove filament or cut it)
5. Watch the Terminal output for messages

You should see something like:
```
Recv: X:5.00 Y:88.41 Z:10.10 E:153.52
Recv: echo:Insert filament and send M108
Recv: T:210.36 /210.00 B:53.06 /53.00
```

6. If you see a **different message**, copy it exactly
7. Go back to plugin settings
8. Paste the message in the **Detection Message** field
9. Click **Save**

## Enable Debug Logging (Optional but Recommended)

For troubleshooting and to verify the plugin is working:

1. Go to Settings → **Logging**
2. Under **Logging Levels**, click **Add**
3. In the **Component** field, enter:
   ```
   octoprint.plugins.anycubicfilamentrunout
   ```
4. Set **Level** to **DEBUG**
5. Click **Save**
6. Restart OctoPrint

Now you'll see detailed plugin activity in `octoprint.log`

## Verify Installation

### Quick Test

1. Start a print
2. Trigger a filament runout
3. You should see:
   - Print pauses automatically
   - A blue notification popup appears
   - Terminal shows the detection message

### Check Logs

View the OctoPrint log file:
```bash
tail -f ~/.octoprint/logs/octoprint.log | grep anycubicfilamentrunout
```

You should see entries like:
```
INFO - Anycubic filament runout detected: echo:Insert filament and send M108
INFO - Firing pause on event bus for Anycubic filament runout.
```

## Troubleshooting

### Plugin Not Showing in Settings

- Restart OctoPrint completely
- Check if plugin is installed: Settings → Plugin Manager
- Look for errors in `octoprint.log`

### Plugin Not Detecting Runout

1. Verify the detection message matches exactly
2. Check debug logs are enabled
3. Confirm printer is actually sending the message
4. Make sure print is active (plugin only works during prints)

### Multiple Pause Events

- Check for other plugins that handle filament runout
- Disable conflicting plugins temporarily to test

## Integration with Other Plugins

### OctoText (SMS/Email Alerts)

This plugin works great with OctoText for remote notifications:

1. Install OctoText plugin
2. Configure your SMS/email settings
3. OctoText will automatically send alerts when this plugin pauses the print

### Other Event-Based Plugins

Any plugin that listens for `PRINT_PAUSED` events will work with this plugin.

## Uninstallation

1. Go to Settings → Plugin Manager
2. Find **Anycubic Filament Runout**
3. Click the **trash icon**
4. Restart OctoPrint

Or via command line:
```bash
~/oprint/bin/pip uninstall octoprint-anycubicfilamentrunout
```

## Need Help?

- [GitHub Issues](https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/issues)
- [OctoPrint Community Forum](https://community.octoprint.org)
