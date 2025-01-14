from game import Game
class Day:
    def __init__(self, day, time):
        self.day = day
        self.time = time

    def describe_morning(self):
        print(f'Day {self.day}, {self.time}')
        print('The sun is shining through the blinds of your window, you hear birds chirping outside.')

    def morning_activity(self):
        activity = Game.ask_question(
            'You wake up to a beautiful morning, do you: '
            '\n1. Get up\n2. Go back to sleep\n',
            ['get up', 'go back to sleep'],
            {1: 'get up', 2: 'go back to sleep'}
        )
        if activity == 'get up':
            print('You get up excited to start your day.')
        else:
            print('You drift back to sleep for an extra few hours.')
            self.time = '12:00 PM'
        return activity

    def end_day(self):
        print(f"Day {self.day} ends. You reflect on the day's events and prepare for tomorrow.\n")

    def go_back(self):
        print(f"You decide to rewind the events of Day {self.day} and start over.\n")
