"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""


class Assists:
    def __init__(self, js: dict):
        self._defensive_assists = js["defensiveAssists"] if "defensiveAssists" in js else 0
        self._healing_done = js["healing_done"] if "healing_done" in js else 0
        self._offensive_assists = js["offensive_assists"] if "offensive_assists" in js else 0
        self._recon_assists = js["recon_assists"] if "recon_assists" in js else 0

    @property
    def defensive_assists(self) -> int:
        return self._defensive_assists

    @property
    def healing_done(self) -> int:
        return self._healing_done

    @property
    def offensive_assists(self) -> int:
        return self._offensive_assists

    @property
    def recon_assists(self) -> int:
        return self._recon_assists
