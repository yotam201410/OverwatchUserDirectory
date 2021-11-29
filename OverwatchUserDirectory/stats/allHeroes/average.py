"""
:copyright: (c) 2020 Yotam Rechnitz
:license: MIT, see LICENSE for more details
"""


class Average:
    def __init__(self, js: dict):
        self._allDamageDoneAvgPer10Min = js["allDamageDoneAvgPer10Min"] if "allDamageDoneAvgPer10Min" in js else 0
        self._barrierDamageDoneAvgPer10Min = js[
            "barrierDamageDoneAvgPer10Min"] if "barrierDamageDoneAvgPer10Min" in js else 0
        self._deathsAvgPer10Min = js["deathsAvgPer10Min"] if "deathsAvgPer10Min" in js else 0
        self._eliminationsAvgPer10Min = js["eliminationsAvgPer10Min"] if "eliminationsAvgPer10Min" in js else 0
        self._finalBlowsAvgPer10Min = js["finalBlowsAvgPer10Min"] if "finalBlowsAvgPer10Min" in js else 0
        self._healingDoneAvgPer10Min = js["healingDoneAvgPer10Min"] if "healingDoneAvgPer10Min" in js else 0
        self._heroDamageDoneAvgPer10Min = js["heroDamageDoneAvgPer10Min"] if "heroDamageDoneAvgPer10Min" in js else 0
        self._objectiveKillsAvgPer10Min = js["objectiveKillsAvgPer10Min"] if "objectiveKillsAvgPer10Min" in js else 0
        self._objectiveTimeAvgPer10Min = js["objectiveTimeAvgPer10Min"] if "objectiveTimeAvgPer10Min" in js else 0
        self._soloKillsAvgPer10Min = js["_soloKillsAvgPer10Min"] if "_soloKillsAvgPer10Min" in js else 0
        self._timeSpentOnFireAvgPer10Min = js["timeSpentOnFireAvgPer10Min"] if "timeSpentOnFireAvgPer10Min" in js else 0

    @property
    def allDamageDoneAvgPer10Min(self) -> int:
        return self._allDamageDoneAvgPer10Min

    @property
    def barrierDamageDoneAvgPer10Min(self) -> int:
        return self._barrierDamageDoneAvgPer10Min

    @property
    def deathsAvgPer10Min(self) -> int:
        return self._deathsAvgPer10Min

    @property
    def eliminationsAvgPer10Min(self) -> int:
        return self._eliminationsAvgPer10Min

    @property
    def finalBlowsAvgPer10Min(self) -> int:
        return self._finalBlowsAvgPer10Min

    @property
    def healingDoneAvgPer10Min(self) -> int:
        return self._healingDoneAvgPer10Min

    @property
    def heroDamageDoneAvgPer10Min(self) -> int:
        return self._heroDamageDoneAvgPer10Min

    @property
    def objectiveKillsAvgPer10Min(self) -> int:
        return self._objectiveKillsAvgPer10Min

    @property
    def objectiveTimeAvgPer10Min(self) -> int:
        return self._objectiveTimeAvgPer10Min

    @property
    def soloKillsAvgPer10Min(self) -> int:
        return self._soloKillsAvgPer10Min

    @property
    def timeSpentOnFireAvgPer10Min(self) -> int:
        return self._timeSpentOnFireAvgPer10Min
