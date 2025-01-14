import random
from game import Game

class Adventure:
    def __init__(self):
        self.feeling = random.choice(['invigorated', 'refreshed', 'rejuvenated', 'energized', 'restored', 'renewed'])
        self.weather = random.choice(['raining', 'sunny', 'snowing', 'windy', 'cloudy', 'hailing'])

    def describe_weather(self):
        print(f'You take a look outside the window, it’s {self.weather} outside today.')

    def choose_activity(self):
        activity = Game.ask_question(
            'What do you do first?: '
            '\n1. Eat breakfast\n2. Go outside\n3. Turn on the TV\n',
            ['eat breakfast', 'go outside', 'turn on the tv'],
            {1: 'eat breakfast', 2: 'go outside', 3: 'turn on the tv'}
        )
        if activity == 'eat breakfast':
            print(f'You enjoy a hearty breakfast and then head outside feeling {self.feeling} and ready to take on the day in the {self.weather} weather!')
        elif activity == 'go outside':
            print(f'You step outside into the {self.weather} weather, feeling {self.feeling}.')
        elif activity == 'turn on the tv':
            print(f'You turn on the TV and catch up on the latest news and shows before heading outside into the {self.weather} weather.')
        return activity

    def mailbox_event(self):
        print('While outside, you notice an envelope hanging out of your mailbox.')
        envelope_action = Game.ask_question(
            'Do you: '
            '\n1. Open the envelope\n2. Inspect the envelope\n',
            ['open the envelope', 'inspect the envelope'],
            {1: 'open the envelope', 2: 'inspect the envelope'}
        )
        if envelope_action == 'open the envelope':
            print('Inside the envelope is a mysterious message inviting you to a secret meeting.')
        elif envelope_action == 'inspect the envelope':
            print('The envelope only has your name written on it with a black pen in cursive.')
