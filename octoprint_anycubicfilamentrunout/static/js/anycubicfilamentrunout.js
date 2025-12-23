/*
 * View model for Anycubic Filament Runout Monitor
 *
 * Author: Modified for Anycubic
 * License: AGPLv3
 */
$(function () {
    function AnycubicfilamentrunoutViewModel(parameters) {
        var self = this;
        self.settingsViewModel = parameters[0];
        self.popup = undefined;

        self.onDataUpdaterPluginMessage = function (plugin, data) {
            if (plugin !== "anycubicfilamentrunout") {
                return;
            }

            if (data.filamentrunout) {
                self.popup = new PNotify({
                    title: 'Anycubic Filament Runout',
                    text: gettext('Filament runout has occurred, please replace filament and resume printing when ready.'),
                    type: 'info',
                    hide: false
                });
            } else {
                if (typeof self.popup !== "undefined") {
                    self.popup.remove();
                    self.popup = undefined;
                }
            }
        };
    }

    OCTOPRINT_VIEWMODELS.push({
        construct: AnycubicfilamentrunoutViewModel,
        dependencies: ["settingsViewModel"],
        elements: ["#settings_plugin_anycubicfilamentrunout"]
    });
});
