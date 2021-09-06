"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.Heroes.Hero.assists import Assists
from OverwatchUserDirectory.stats.Heroes.Hero.average import Average
from OverwatchUserDirectory.stats.Heroes.Hero.best import Best
from OverwatchUserDirectory.stats.Heroes.Hero.combat import Combat
from OverwatchUserDirectory.stats.Heroes.Hero.game import Game
from OverwatchUserDirectory.stats.Heroes.Hero.heroSpecific import HeroSpecific
from OverwatchUserDirectory.stats.Heroes.Hero.matchAwards import MatchAwards
from OverwatchUserDirectory.stats.Heroes.Hero.miscellaneous import Miscellaneous


class Hero:
    def __init__(self, js: dict, hero: str):
        self._hero = hero
        self._assists = Assists(js["assists"]) if js["assists"] else None
        self._average = Average(js["average"]) if js["average"] else None
        self._best = Best(js["best"]) if js["best"] else None
        self._combat = Combat(js["combat"]) if js["combat"] else None
        self._game = Game(js["game"]) if js["game"] else None
        self._heroSpecific = HeroSpecific(js["heroSpecific"], self.hero) if js["heroSpecific"] else None
        self._matchAwards = MatchAwards(js["matchAwards"]) if js["matchAwards"] else None
        self._miscellaneous = Miscellaneous(js["miscellaneous"]) if js["miscellaneous"] else None

    @property
    def hero(self) -> str:
        return self._hero

    @property
    def assists(self) -> Assists:
        return self._assists

    @property
    def average(self) -> Average:
        return self._average

    @property
    def best(self) -> Best:
        return self._best

    @property
    def combat(self) -> Combat:
        return self._combat

    @property
    def game(self) -> Game:
        return self._game

    @property
    def matchAwards(self) -> MatchAwards:
        return self._matchAwards

    @property
    def miscellaneous(self) -> Miscellaneous:
        return self._miscellaneous

    @property
    def heroSpecific(self) -> HeroSpecific:
        return self._heroSpecific
