# coding=utf-8
import octoprint.plugin
from octoprint.events import Events

class AnycubicfilamentrunoutPlugin(octoprint.plugin.SettingsPlugin,
    octoprint.plugin.AssetPlugin,
    octoprint.plugin.TemplatePlugin,
    octoprint.plugin.EventHandlerPlugin
):
    def __init__(self):
        super().__init__()
        self._processing = False

    # ~~ SettingsPlugin mixin

    def get_settings_version(self):
        return 1

    def get_settings_defaults(self):
        return {
            "detection_message": "echo:Insert filament and send M108"
        }

    # ~~ AssetPlugin mixin

    def get_assets(self):
        return {
            "js": ["js/anycubicfilamentrunout.js"]
        }

    # ~~ TemplatePlugin mixin

    def get_template_vars(self):
        return {"plugin_version": self._plugin_version}

    # ~~ Event Handler Plugin

    def on_event(self, event, payload):
        if event in [Events.PRINT_STARTED, Events.PRINT_DONE, Events.PRINT_CANCELLED, Events.PRINT_RESUMED]:
            self._plugin_manager.send_plugin_message(self._identifier, {'filamentrunout': False})
            self._processing = False

    # ~~ GCode received hook
    def process_gcode(self, comm, line, *args, **kwargs):
        # Check for Anycubic filament runout message
        detection_message = self._settings.get(["detection_message"])
        
        if detection_message in line and self._printer.is_printing() and not self._processing:
            self._logger.info("Anycubic filament runout detected: %s" % line.strip())
            self._processing = True

            fileposition = comm.getFilePosition() if comm else None
            progress = comm.getPrintProgress() if comm else None
            job_data = self._printer.get_current_job()

            payload = job_data.get("file")
            payload["owner"] = ""
            payload["user"] = job_data.get("user")
            payload["fileposition"] = fileposition
            payload["progress"] = progress
            self._logger.info("Firing pause on event bus for Anycubic filament runout.")
            self._event_bus.fire(Events.PRINT_PAUSED, payload)

            self._plugin_manager.send_plugin_message(self._identifier, {'filamentrunout': True})

        return line

    # ~~ Softwareupdate hook

    def get_update_information(self):
        return {
            "anycubicfilamentrunout": {
                "displayName": "Anycubic Filament Runout",
                "displayVersion": self._plugin_version,

                # version check: github repository
                "type": "github_release",
                "user": "YOUR_GITHUB_USERNAME",
                "repo": "OctoPrint-AnycubicFilamentRunoutMonitor",
                "current": self._plugin_version,

                # update method: pip
                "pip": "https://github.com/YOUR_GITHUB_USERNAME/OctoPrint-AnycubicFilamentRunoutMonitor/archive/{target_version}.zip",
            }
        }


__plugin_name__ = "Anycubic Filament Runout"
__plugin_pythoncompat__ = ">=3,<4"  # Only Python 3

def __plugin_load__():
    global __plugin_implementation__
    __plugin_implementation__ = AnycubicfilamentrunoutPlugin()

    global __plugin_hooks__
    __plugin_hooks__ = {
        "octoprint.comm.protocol.gcode.received": (__plugin_implementation__.process_gcode, 1),
        "octoprint.plugin.softwareupdate.check_config": __plugin_implementation__.get_update_information
    }
