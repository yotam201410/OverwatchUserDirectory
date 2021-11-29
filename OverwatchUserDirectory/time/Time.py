class TimeError(Exception):
    pass


class Time(object):
    def __init__(self, hour: int = 0, minute: int = 0, second: int = 0):
        if 0 <= minute < 60 and 0 <= second < 60:
            self._hour = hour
            self._minute = minute
            self._second = second
        else:
            raise TimeError("seconds/minutes have to be between 0 to 59")

    @property
    def hour(self) -> int:
        return self._hour

    @property
    def second(self) -> int:
        return self._second

    @property
    def minute(self) -> int:
        return self._minute

    def __str__(self):
        return f"{self.hour}:{self.minute}:{self.second}"

    def __eq__(self, other) -> bool:
        return self.second == other.second and self.minute == other.minute and self.hour == other.hour and self.__hash__() == hash(
            other)

    def __lt__(self, other) -> bool:
        if self.hour == other.hour:
            if self.minute == other.minute:
                return self.second < other.second
            return self.minute < other.minute
        return self.hour < other.hour

    def __le__(self, other):
        return self.__eq__(other) or self.__lt__(other)

    def __ne__(self, other):
        return not self.__eq__(other)

    def __gt__(self, other):
        return not self.__le__(other)

    def __ge__(self, other):
        return self.__eq__(other) or self.__gt__(self)

    def __hash__(self):
        return hash((self.second, self.minute, self.hour))
