"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.allHeroes.assists import Assists
from OverwatchUserDirectory.stats.allHeroes.average import Average
from OverwatchUserDirectory.stats.allHeroes.best import Best
from OverwatchUserDirectory.stats.allHeroes.combat import Combat
from OverwatchUserDirectory.stats.allHeroes.game import Game
from OverwatchUserDirectory.stats.allHeroes.matchAwards import MatchAwards
from OverwatchUserDirectory.stats.allHeroes.miscellaneous import Miscellaneous

class AllHeroes:
    def __init__(self, js: dict):
        self._miscellaneous = Miscellaneous(js["miscellaneous"]) if js["miscellaneous"] else None
        self._assists = Assists(js["assists"]) if js["assists"] else None
        self._average = Average(js["average"]) if js["average"] else None
        self._combat = Combat(js["combat"]) if js["combat"] else None
        self._game = Game(js["game"]) if js["game"] else None
        self._match_awards = MatchAwards(js["matchAwards"]) if js["matchAwards"] else None
        self._best = Best(js["best"]) if js["best"] else None

    @property
    def miscellaneous(self) -> Miscellaneous:
        return self._miscellaneous

    @property
    def assists(self) -> Assists:
        return self._assists

    @property
    def average(self) -> Average:
        return self._average

    @property
    def combat(self) -> Combat:
        return self._combat

    @property
    def game(self) -> Game:
        return self._game

    @property
    def match_awards(self) -> MatchAwards:
        return self._match_awards

    @property
    def best(self) -> Best:
        return self._best
