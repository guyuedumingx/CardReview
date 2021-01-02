# -*- coding: utf-8 -*-
import sys
import os
import datetime
from card import *
from pynput import keyboard

class Action():
    """
    动作类
    """

    def __init__(self, cards):
        self.cards = cards
        self.turn = True

    #退出
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
        self.next()

    def show_card_list(self):
        os.system("clear")
        for card in self.cards.cards:
            card.show()
            
    def previous(self):
        self.card.cur = self.card.cur - 1
        self.next()

    def add(self):
        os.system('clear')
        print("front: ")
        front = self.read_in()
        print("back: ")
        back = self.read_in()

        self.card = Card(self.cards.len, front, back, 0)
        self.cards.new_card(self.card) 

        print("添加成功!")

    def read_in(self):
        return "".join(sys.stdin.readlines()).strip('\n')



class Review_Action(Action):
    """
    复习动作类
    """
    def __init__(self, cards):
        self.cards = cards
        self.turn = True
        self.review = Cards(self.name_init(cards), self.path_init(cards.path))
        self.review.build()
    
    def path_init(self, path):
        path = path + "review/" 
        if not os.path.exists(path):
            os.makedirs(path)
        return path
    
    def name_init(self, cards):
        date = str(datetime.date.today().month) + "_" + str(datetime.date.today().day)
        name = cards.name + "_" + date
        return name 

    def next(self):
        self.card = self.cards.read_one()
        if self.card is not None:
            os.system('clear')
            self.card.show()
            print("--------------------------------------------------")
            self.now_answer()
    
    def now_answer(self):
        answer = self.read_in()
        recard = self.card.clone()
        recard.back = answer
        self.review.new_card(recard)
        print("--------------------------------------------------")
        self.card.overturn()

    def quit(self):
        self.cards.write()
        self.review.write()
        sys.exit(0)

