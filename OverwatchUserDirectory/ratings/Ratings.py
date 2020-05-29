"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.ratings.rate import Rate


class Ratings:
    def __init__(self, js: list):
        try:
            self.tank = Rate(js[js.index("tank")])
        except:
            self.tank = None
        try:
            self.damage = Rate(js[js.index("damage")])
        except:
            self.damage = None
        try:
            self.support = Rate(js[js.index("support")])
        except:
            self.support = None
        if self.tank is not None and self.damage is not None and self.support is not None:
            self._average_level = round(float(self.tank.level + self.damage.level + self.support.level) / 3)
        else:
            self._average_level = None

    @property
    def average_level(self):
        return self._average_level
