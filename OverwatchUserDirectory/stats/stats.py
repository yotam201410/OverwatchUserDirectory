"""
:copyright: (c) 2020-present Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.Lhero import Lhero
from OverwatchUserDirectory.stats.careerstats import CareerStats
from typing import List
from OverwatchUserDirectory.time.Time import Time


def _sort_algorithm(lhero: Lhero, sort_by: str):
    return lhero.__dict__[sort_by]


class Stats:
    def __init__(self, js: dict):
        self._top_heroes_list = []
        for lhero in js["topHeroes"].items():
            self.top_heroes_list.append(Lhero(lhero[1], lhero[0]))
        if self._top_heroes_list:
            self._top_heroes_list = self.get_top_heroes_list_sorted("time_played")
        self._career_stats = CareerStats(js["careerStats"])

    @property
    def top_heroes_list(self) -> List[Lhero]:
        return self._top_heroes_list

    @property
    def career_stats(self) -> CareerStats:
        return self._career_stats

    def get_top_heroes_list_sorted(self, sort_value: str) -> List[Lhero]:
        sort_value = "_" + sort_value
        if self.top_heroes_list:
            if type(self.top_heroes_list[0].__dict__[sort_value]) in [int, Time]:
                return sorted(self.top_heroes_list, key=lambda x: _sort_algorithm(x, sort_value), reverse=True)
            else:
                return sorted(self.top_heroes_list, key=lambda x: _sort_algorithm(x, sort_value))
