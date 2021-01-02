import sys
import os
from build import Cards
from card import Card
from pynput import keyboard

class Key():

    def __init__(self, data):
        self.cards = data
        self.turn = True

    def quit(self):
        self.cards.write()
        sys.exit(0)

    def next(self):
        if(self.turn):
            self.card = self.cards.read_one()
            self.turn = False
            os.system('clear')
            self.card.show()
        else:
            self.turn = True
            self.card.overturn()

    def show_card_list(self):
        for card in self.cards.cards:
            card.front()
            
    def previous(self):
        self.cards.cur = self.cards.cur - 1
        self.next()

    def add(self):
        os.system('clear')
        front = input("front: ")
        back = input("back: ")
        self.card = Card(front, back)
        self.cards.add_card(self.card)



