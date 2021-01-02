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
    
    def add_times_next(self):
        if not self.turn:
            self.card.add_times()
        self.next()

    def sub_times_next(self):
        if not self.turn:
            self.card.sub_times()
        self.next()

    def next(self):
        if(self.turn):
            self.card = self.cards.read_one()
            if self.card is not None:
                self.turn = False
                os.system('clear')
                self.card.show()
                print("--------------------------------------------------")
        else:
            self.turn = True
            self.card.overturn()

    def pass_card(self):
        self.card.pass_card()

    def show_card_list(self):
        os.system("clear")
        for card in self.cards.cards:
            card.show()
            
    def previous(self):
        self.cards.cur = self.cards.cur - 1
        self.next()

    def add(self):
        os.system('clear')
        print("front: ")
        front = self.read_in()
        print("back: ")
        back = self.read_in()

        self.card = Card(front, back, 0)
        self.cards.add_card(self.card)
        self.cards.cards.append(self.card)
        print("添加成功!")

    def read_in(self):
        return "".join(sys.stdin.readlines()).strip('\n')



