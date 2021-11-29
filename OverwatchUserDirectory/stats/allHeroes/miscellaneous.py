"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""


class Miscellaneous:
    def __init__(self, js: dict):
        try:
            self._teleporter_pads_destroyed = js["teleporterPadsDestroyed"]
        except KeyError:
            self._teleporter_pads_destroyed = 0
        try:
            self._turrets_destroyed = js["turretsDestroyed"]
        except KeyError:
            self._turrets_destroyed = 0

    @property
    def teleporter_pads_destroyed(self) -> int:
        return self._teleporter_pads_destroyed

    @property
    def turrets_destroyed(self) -> int:
        return self._turrets_destroyed
