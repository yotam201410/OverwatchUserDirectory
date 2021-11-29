"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""
from OverwatchUserDirectory.time import Time


class Lhero:
    def __init__(self, js: dict, hero: str):
        self._hero_name = hero
        self._time_played = js["timePlayed"] if "timePlayed" in js else 0
        if self._time_played == 0:
            self._time_played = Time.Time()
        else:
            self._time_played = self._time_played.split(":")
            ln = len(self._time_played)
            if ln == 1:
                self._time_played = Time.Time(second=int(self._time_played[0]))
            elif ln == 2:
                self._time_played = Time.Time(second=int(self._time_played[1]), minute=int(self._time_played[0]))
            elif ln == 3:
                self._time_played = Time.Time(second=int(self._time_played[2]), minute=int(self._time_played[1]),
                                              hour=int(self._time_played[0]))
        self._games_won = js["gamesWon"] if "gamesWon" in js else 0
        self._weapon_accuracy = js["weaponAccuracy"] if "weaponAccuracy" in js else 0
        self._eliminations_per_life = js["eliminationPerLife"] if "eliminationPerLife" in js else 0
        self._multi_kill_best = js["multiKillBest"] if "multiKillBest" in js else 0
        self._objective_kills = js["objectiveKills"] if "objectiveKills" in js else 0

    @property
    def hero_name(self) -> str:
        return self._hero_name

    @property
    def time_played(self) -> Time:
        return self._time_played

    @property
    def games_won(self) -> int:
        return self._games_won

    @property
    def weapon_accuracy(self) -> int:
        return self._weapon_accuracy

    @property
    def eliminations_per_life(self) -> int:
        return self._eliminations_per_life

    @property
    def multi_kill_best(self) -> int:
        return self._multi_kill_best

    @property
    def objective_kills(self) -> int:
        return self._objective_kills
