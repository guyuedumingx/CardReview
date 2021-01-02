import argparse  
import sys 
import os
from build import *
from pynput import keyboard
from key import Key

ap = argparse.ArgumentParser()
ap.add_argument("-n", "--name", help="choose which cards group to use")
ap.add_argument("-l", "--list", action="store_true", help="show cards group list")
ap.add_argument("-p", "--path", type=str, help="choose a file to load cards")
ap.add_argument("-b", "--build", action="store_true", help="cards a new groups")
ap.add_argument("-r", "--review", action="store_true", help="cards a new groups")
args = vars(ap.parse_args())


path = sys.path[0]+"/res/"
if args['path'] is not None:
    path = args['path']
else:
    if not os.path.exists(path):
        os.makedirs(path)

io = IO(path)

if args['list'] is True:
    for name in io.card_groups_name():
        print(name.split('.')[0])

    
if args['name'] is not None:
    if args['review'] is True:
        cards = Review(path + args['name'])
    else:
        cards = Cards(path + args['name'])

    if(io.has_groups(args['name'])):
        cards.read()

    elif args['build'] is True:
        cards.build()

    else:
        print("没有这个卡牌组! 请使用 -b 来新建卡组")
        sys.exit(0)




    key = Key(cards)
    print("总共有:\t"+str(cards.len)+" 张卡牌")

    with keyboard.GlobalHotKeys({
            '<ctrl>+a': key.add,
            '<ctrl>+j': key.add_times_next,
            '<ctrl>+h': key.sub_times_next,
            '<ctrl>+w' : key.quit,
            '<ctrl>+q' : key.quit,
            '<ctrl>+k' : key.previous,
            '<ctrl>+p' : key.pass_card,
            '<ctrl>+l' : key.show_card_list
            }) as h:
        h.join()

