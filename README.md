# Double Press Power for Flashlight

A Magisk module that allows you to turn on/off the flashlight by double-pressing the power button on Meizu devices running Flyme 9.

## Description

This module listens for double-taps on the power button and toggles the flashlight using the Meizu Toolbox app. It's specifically designed for Meizu 17 Pro devices running Flyme 9, but may work on other Meizu devices with similar system configurations.

## Features

- Turn flashlight on/off by double-pressing the power button
- No additional app required (uses built-in Meizu Toolbox)
- Lightweight implementation using Python and system commands
- Runs in the background as a Magisk service

## Requirements

- Root access (Magisk)
- Meizu device running Flyme 9 (tested on Meizu 17 Pro)
- Python environment on the device (usually provided by Magisk)

## Installation

1. Flash the module zip file in Magisk Manager
2. Reboot your device
3. Double press the power button to toggle flashlight

## How It Works

The module uses a Python script that:
1. Monitors `/dev/input/event0` for power button events
2. Detects double-taps based on a configurable time interval (default 500ms)
3. Toggles the flashlight by starting or force-stopping the Meizu Toolbox app

## Files

- `module.prop` - Module information for Magisk
- `flashlight_toggle.py` - Main Python script that monitors events and toggles flashlight
- `service.sh` - Starts the Python script as a background service
- `customize.sh` - Installation script (empty for this module)
- `system.prop` - System properties (empty for this module)

## Configuration

You can modify the double-click interval by editing the `flashlight_toggle.py` file:
```python
# Change this value to adjust double-click sensitivity (in milliseconds)
DOUBLE_CLICK_INTERVAL_MS = 500
```

## Notes

- This module is specifically designed for Meizu devices with Flyme 9
- The implementation relies on the Meizu Toolbox app (`com.meizu.flyme.toolbox`)
- May not work on other Android devices or custom ROMs
- Requires root access to read input events

## Troubleshooting

If the module doesn't work:
1. Check if the module is properly installed and enabled in Magisk
2. Verify that Python is available on your device
3. Check the Magisk log for any error messages
4. Ensure your device is a Meizu with Flyme 9

## Disclaimer

This module modifies system behavior and requires root access. Use at your own risk. The authors are not responsible for any damage to your device.

## Author

Ash

> May the Holy Light protect you.# DoublePressPowerButtonToggleFlashlight
