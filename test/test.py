import OverwatchUserDirectory
import datetime

user = OverwatchUserDirectory.User("yotam201410#2946")
print(user.quick_play_stats.get_top_heroes_list_sorted("time_played")[0].__dict__["_time_played"])

