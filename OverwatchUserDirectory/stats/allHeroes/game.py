"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.time.Time import Time


class Game:
    def __init__(self, js: dict):
        self._gamesWon = js["gamesWon"] if "gamesWon" in js else 0
        self._timePlayed = Time(js["timePlayed"]) if "timePlayed" in js else Time()

    @property
    def gamesWon(self) -> int:
        return self._gamesWon

    @property
    def timePlayed(self) -> Time:
        return self._timePlayed
