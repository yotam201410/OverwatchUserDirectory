"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.ratings.rate import Rate


class Ratings:
    def __init__(self, js: list):
        self._tank = None
        self._support = None
        self._damage = None
        if js:
            for role in js:
                if role["role"] == "tank":
                    self._tank = Rate(role)
                elif role["role"] == "damage":
                    self._damage = Rate(role)
                elif role["role"] == "support":
                    self._support = Rate(role)
        if self.tank is not None and self.damage is not None and self.support is not None:
            self._average_level = round(float(self.tank.level + self.damage.level + self.support.level) / 3)
        else:
            self._average_level = None

    @property
    def average_level(self) -> int:
        return self._average_level

    @property
    def tank(self) -> Rate:
        return self._tank

    @property
    def support(self) -> Rate:
        return self._support

    @property
    def damage(self) -> Rate:
        return self._damage
