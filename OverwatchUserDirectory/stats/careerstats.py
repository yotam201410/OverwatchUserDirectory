"""
:copyright: (c) 2020-present Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.stats.allHeroes.AllHeroes import AllHeroes
from OverwatchUserDirectory.stats.Heroes.Hero.hero import Hero
from typing import TypedDict


class CareerStats:
    def __init__(self, js: dict):
        hero_name_list = ["ana", "ashe", "baptiste", "bastion", "brigitte", "dVa", "doomfist", "echo", "genji", "hanzo",
                          "junkrat", "lucio", "mccree", "mei", "mercy", "moira", "orisa", "pharah", "reaper",
                          "reinhardt", "roadhog", "sigma", "soldier76", "sombra", "symmetra", "torbjorn", "tracer",
                          "widowmaker", "winston", "wreckingBall", "zarya", "zenyatta"]
        self._all_Heroes = AllHeroes(js["allHeroes"])
        self._hero_dict = {}
        for only_hero in hero_name_list:
            try:
                self._hero_dict[only_hero] = Hero(js[only_hero], only_hero)
            except KeyError:
                pass

    @property
    def all_Heroes(self) -> AllHeroes:
        return self._all_Heroes

    @property
    def hero_dict(self) -> {str: Hero}:
        return self._hero_dict
