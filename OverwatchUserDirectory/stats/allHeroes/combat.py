"""
:copyright: (c) 2020-present Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""


class Combat:
    def __init__(self, js: dict):
        self._barrierDamageDone = js["barrierDamageDone"] if "barrierDamageDone" in js else 0
        self._damageDone = js["damageDone"] if "damageDone" in js else 0
        self._deaths = js["deaths"] if "deaths" in js else 0
        self._eliminations = js["eliminations"] if "eliminations" in js else 0
        self._environmentalKills = js["environmentalKills"] if "environmentalKills" in js else 0
        self._finalBlows = js["finalBlows"] if "finalBlows" in js else 0
        self._heroDamageDone = js["heroDamageDone"] if "heroDamageDone" in js else 0
        self._meleeFinalBlows = js["meleeFinalBlows"] if "meleeFinalBlows" in js else 0
        self._multikills = js["multiKills"] if "multiKills" in js else 0
        self._objectiveKills = js["objectiveKills"] if "objectiveKills" in js else 0
        self._objectiveTime = js["objectiveTime"] if "objectiveTime" in js else 0
        self._soloKills = js["soloKills"] if "soloKills" in js else 0
        self._timeSpentOnFire = js["timeSpentOnFire"] if "timeSpentOnFire" in js else 0

    @property
    def barrierDamageDone(self):
        return self._barrierDamageDone

    @property
    def damageDone(self):
        return self._damageDone

    @property
    def deaths(self):
        return self._deaths

    @property
    def eliminations(self):
        return self._eliminations

    @property
    def environmentalKills(self):
        return self._environmentalKills

    @property
    def finalBlows(self):
        return self._finalBlows

    @property
    def heroDamageDone(self):
        return self._heroDamageDone

    @property
    def meleeFinalBlows(self):
        return self._meleeFinalBlows

    @property
    def multikills(self):
        return self._multikills

    @property
    def objectiveKills(self):
        return self._objectiveKills

    @property
    def objectiveTime(self):
        return self._objectiveTime

    @property
    def soloKills(self):
        return self._soloKills

    @property
    def timeSpentOnFire(self):
        return self._timeSpentOnFire
