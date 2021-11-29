"""
MIT License
Copyright (c) 2020-present Yotam Rechnitz

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
import datetime

from OverwatchUserDirectory.ratings.Ratings import Ratings
import requests
import logging
from OverwatchUserDirectory.stats.stats import Stats


class UserNotFound(Exception):
    pass


class User:
    def __init__(self, user: str):
        user = user.split("#")
        user = "-".join(user)
        logging.basicConfig(level=logging.DEBUG)

        logging.error(f"{datetime.datetime.now()}: trying to get user")
        website = requests.get(f"https://ovrstat.com/stats/pc/{user}")
        if website.status_code == 404:
            raise UserNotFound(f"there is no such user as {user}")
        logging.info(f"{datetime.datetime.now()}: got user successfully")
        js = website.json()
        self._name = js["name"]
        self._icon = js["icon"]
        self._level_icon = js["levelIcon"]
        self._endorsement = js["endorsement"]
        self._endorsementIcon = js["endorsementIcon"]
        self._prestige_icon = js['prestigeIcon']
        self._private = js["private"]
        if self.private:
            self._ratings = None
            self._games_won = None
            self._quick_play_stats = None
            self._competitive_stats = None
        else:
            self._ratings = Ratings(js["ratings"])
            self._games_won = js["gamesWon"]
            self._quick_play_stats = Stats(js["quickPlayStats"])
            self._competitive_stats = Stats(js["competitiveStats"])
        logging.info(f"{datetime.datetime.now()}: user object is ready")

    @property
    def name(self) -> str:
        return self._name

    @property
    def private(self) -> bool:
        return self._private

    @property
    def icon(self) -> str:
        return self._icon

    @property
    def level_icon(self) -> str:
        return self._level_icon

    @property
    def endorsement(self) -> int:
        return self._endorsement

    @property
    def prestige_icon(self) -> str:
        return self._prestige_icon

    @property
    def ratings(self) -> Ratings:
        return self._ratings

    @property
    def games_won(self) -> int:
        return self._games_won

    @property
    def quick_play_stats(self) -> Stats:
        return self._quick_play_stats

    @property
    def competitive_stats(self) -> Stats:
        return self._competitive_stats

