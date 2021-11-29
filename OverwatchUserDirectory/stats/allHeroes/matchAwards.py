"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""


class MatchAwards:
    def __init__(self, js: dict):
        self._cards = js["cards"] if "cards" in js else 0
        self._medals = js["medals"] if "medals" in js else 0
        self._medalsBronze = js["medalsBronze"] if "medalsBronze" in js else 0
        self._medalsGold = js["medalsGold"] if "medalsGold" in js else 0
        self._medalsSilver = js["medalsSilver"] if "medalsSilver" in js else 0

    @property
    def cards(self) -> int:
        return self._cards

    @property
    def medals(self) -> int:
        return self._medals

    @property
    def medalsBronze(self) -> int:
        return self._medalsBronze

    @property
    def medalsGold(self) -> int:
        return self._medalsGold

    @property
    def medalsSilver(self) -> int:
        return self._medalsSilver
