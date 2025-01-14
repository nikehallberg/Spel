import sys

class Game:
    def __init__(self, player):
        self.player = player

    def start(self):
        while True:
            answer = input("Are you ready? (Yes or No): ").strip().lower()
            if answer == 'yes':
                print('Let us start your adventure!\n')
                break
            elif answer == 'no':
                sys.exit('Come back when you are ready.')
            else:
                print('Invalid answer, please input Yes or No.')

    @staticmethod
    def ask_question(prompt, options, numeric_map):
        while True:
            choice = input(prompt).strip().lower()
            if choice.isdigit() and int(choice) in numeric_map:
                return numeric_map[int(choice)]
            elif choice in options:
                return choice
            print(f"Invalid choice. Please choose from: {', '.join([f'{k}. {v}' for k, v in numeric_map.items()])}")