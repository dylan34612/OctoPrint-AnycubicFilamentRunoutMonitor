# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2024-12-23

### Added
- Initial release
- Detection of Anycubic filament runout message: `echo:Insert filament and send M108`
- Automatic pause of print job when filament runs out
- Notification popup when filament runout is detected
- Configurable detection message in settings
- Debug logging support

### Changed
- Adapted from Prusa Filament Runout Monitor for Anycubic printers
- Simplified configuration (removed X/Y position monitoring)
- Updated to use message-based detection instead of position-based

### Notes
- Tested on Anycubic Kobra series and Vyper
- Based on original work by jneilliii
