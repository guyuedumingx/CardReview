# -*- coding: utf-8 -*-

import argparse  
import sys 
import os
from pynput import keyboard
from action import *
from card import *

class InOut():
    """
    实现卡片的读入
    """

    def __init__(self, path):
        self.path = path
        self.groups = [] 

    def card_groups_name(self):
        for file in os.listdir(self.path):
            if(file.endswith(".xml")):
                self.groups.append(file) 
        return self.groups

    def has_groups(self, name):
        file = name+".xml"
        self.card_groups_name()
        return file in self.groups


ap = argparse.ArgumentParser()
ap.add_argument("-r", "--review", action="store_true", help="review mode")
ap.add_argument("-b", "--build", action="store_true", help="add a new groups")
ap.add_argument("-l", "--list", action="store_true", help="show cards group list")
ap.add_argument("-n", "--name", help="choose which cards group to use")
ap.add_argument("-p", "--path", type=str, help="choose a path to load cards")
ap.add_argument("-f", "--file", type=str, help="choose a file to load cards")
args = vars(ap.parse_args())


path = sys.path[0]+"/res/"
if args['path'] is not None:
    path = args['path']+"/"
else:
    if not os.path.exists(path):
        os.makedirs(path)
in_out = InOut(path)

if args['list'] is True:
    for name in in_out.card_groups_name():
        print(name.split('.')[0])

    
if args['name'] is not None:
    cards = Cards(args['name'], path)

    if(in_out.has_groups(args['name'])):
        cards.read()

    elif args['build'] is True:
        if args['file'] is not None:
            cards.load_cards_from_file(args['file'])


    else:
        print("没有这个卡牌组! 请使用 -b 来新建卡组")
        sys.exit(0)

    print("总共有:\t"+str(cards.len)+" 张卡牌")

    if args['review'] is True:
        action = Review_Action(cards)
    else:
        action = Action(cards)

    with keyboard.GlobalHotKeys({
            '<ctrl>+a': action.add,
            '<ctrl>+j': action.add_times_next,
            '<ctrl>+n': action.add_times_next,
            '<ctrl>+h': action.sub_times_next,
            '<ctrl>+q' : action.quit,
            '<ctrl>+w' : action.quit,
            '<ctrl>+k' : action.previous,
            '<ctrl>+p' : action.pass_card,
            '<ctrl>+l' : action.show_card_list
            }) as h:
        h.join()


