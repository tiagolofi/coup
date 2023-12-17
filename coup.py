
import os

class Coup():

    def __init__(self) -> None:
        self.path_cards = 'cards/'
        self.deck = [self.path_cards + i for i in os.listdir(self.path_cards)]
    
    def __str__(self) -> str:
        return '\n'.join(self.deck)

    def __call__(self) -> list:
        return self.deck
    
if __name__ == '__main__':

    coup = Coup()

    print(coup)