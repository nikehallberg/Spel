import sys
import random
from player import Player
from game import Game
from adventure import Adventure
from day import Day

if __name__ == "__main__":
    player = Player.create_player()
    game = Game(player)
    game.start()

    day1 = Day(day=1, time='Monday, 8:00 AM')
    day1.describe_morning()
    day1.morning_activity()

    adventure1 = Adventure()
    adventure1.describe_weather()
    adventure1.choose_activity()
    adventure1.mailbox_event()

    print("\nDay 2 begins...\n")

    day2 = Day(day=2, time='Tuesday, 8:00 AM')
    day2.describe_morning()
    day2.morning_activity()

    adventure2 = Adventure()
    adventure2.describe_weather()
    adventure2.choose_activity()
    adventure2.mailbox_event()
    day2.end_day()

