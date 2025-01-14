import sys

class Player:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def create_player():
        name = input('What is your name?: ').strip().capitalize()
        print(f'Hello {name}\n')
        try:
            age = int(input(f'{name}, How old are you?: '))
            if age < 18:
                sys.exit('Come back when you are older.')
        except ValueError:
            sys.exit('Invalid age input. Please restart and enter a valid number.')
        return Player(name, age)