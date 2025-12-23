# Anycubic Filament Runout Monitor

OctoPrint plugin that monitors Anycubic printer serial communications for filament runout events and automatically pauses the print job.

![License](https://img.shields.io/github/license/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor)
![Release](https://img.shields.io/github/v/release/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor)

## Overview

This plugin detects when your Anycubic printer runs out of filament by monitoring for the specific message `echo:Insert filament and send M108` in the serial communication. When detected, it automatically:

- Pauses the print job in OctoPrint
- Displays a notification popup
- Triggers the pause event for other plugins (like OctoText for SMS/email alerts)

## Compatibility

**Tested on:**
- Anycubic Kobra series
- Anycubic Vyper
- Other Anycubic printers that send the standard filament runout message

**Requirements:**
- OctoPrint 1.4.0 or higher
- Python 3.7 or higher

## Installation

### Via Plugin Manager (Recommended)

1. Open OctoPrint Settings
2. Go to Plugin Manager
3. Click "Get More..."
4. Search for "Anycubic Filament Runout"
5. Click "Install"

### Manual Installation

Install via the bundled Plugin Manager or manually using this URL:

```
https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/main.zip
```

Or via command line:

```bash
pip install https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/main.zip
```

## Configuration

### Default Settings

The plugin comes pre-configured with the default Anycubic filament runout message:
```
echo:Insert filament and send M108
```

### Custom Detection Message

If your printer uses a different message:

1. Go to OctoPrint Settings → Anycubic Filament Runout
2. Start a print and trigger a filament runout
3. Watch the Terminal tab in OctoPrint for the exact message
4. Copy and paste that message into the "Detection Message" field
5. Save settings

Example terminal output during filament runout:
```
Recv: T:210.03 /210.00 B:53.03 /53.00
Recv: X:5.00 Y:88.41 Z:10.10 E:153.52
Recv: echo:Insert filament and send M108
Recv: T:210.36 /210.00 B:53.06 /53.00
```

## Usage

1. Start a print as normal
2. When filament runs out, the plugin automatically:
   - Detects the runout message
   - Pauses the print
   - Shows a notification popup
3. Replace the filament
4. Resume the print from OctoPrint interface

## Troubleshooting

### Plugin not detecting runout

1. **Enable Debug Logging:**
   - Go to Settings → Logging
   - Add `octoprint.plugins.anycubicfilamentrunout` with level `DEBUG`
   - Save and restart OctoPrint

2. **Check Terminal Output:**
   - Trigger a filament runout
   - Watch the Terminal tab
   - Copy the exact message your printer sends

3. **Update Detection Message:**
   - Go to plugin settings
   - Update with the exact message from your printer
   - Save and test again

### Common Issues

**Issue:** Popup doesn't appear
- **Solution:** Check browser console for JavaScript errors

**Issue:** Print doesn't pause
- **Solution:** Verify the detection message matches exactly (including spaces and capitalization)

**Issue:** Multiple pause events
- **Solution:** Check for conflicting plugins that also monitor for pauses

## Development

### Building from Source

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor.git
cd OctoPrint-AnycubicFilamentRunoutMonitor
pip install -e .
```

### Testing

Create a test file with your printer's output:
```bash
echo "!!DEBUG:send echo:Insert filament and send M108" > test.gcode
```

## Credits

- Modified for Anycubic printers from the original [Prusa Filament Runout Monitor](https://github.com/jneilliii/OctoPrint-PrusaFilamentRunoutMonitor) by jneilliii
- Original plugin funded by [Kaizen Smart Data Ltd.](https://kaizensmartdata.com/)

## Support

If you find this plugin helpful:

[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/YOUR_USERNAME)

Or support the original author jneilliii:
- [Patreon](https://www.patreon.com/jneilliii)
- [PayPal](https://paypal.me/jneilliii)

## Get Help

- [Issue Tracker](https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/issues)
- [OctoPrint Community Forums](https://community.octoprint.org)

## License

Licensed under the [GNU Affero General Public License v3.0](LICENSE)
