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
        self.miscellaneous = Miscellaneous(js["miscellaneous"]) if js["miscellaneous"] else None
        self.assists = Assists(js["assists"]) if js["assists"] else None
        self.average = Average(js["average"]) if js["average"] else None
        self.combat = Combat(js["combat"]) if js["combat"] else None
        self.game = Game(js["game"]) if js["game"] else None
        self.matchAwards = MatchAwards(js["matchAwards"]) if js["matchAwards"] else None
        self.best = Best(js["best"]) if js["best"] else None
