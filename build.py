from xml.dom.minidom import parse, Document
from card import Card
import os
import sys


class Cards():
    """
    实现卡片的添加和存储
    """
    
    def __init__(self, name):
        self.file = name + ".xml"
        self.cards = []
        self.cur = 0
        self.len = 0

    def read(self):
        self.domTree = parse(self.file)
        self.root = self.domTree.documentElement

        res = []
        nodes = self.domTree.getElementsByTagName("card")
        for node in nodes:
            try:
                front = node.getElementsByTagName("front")[0].childNodes[0].data
                back = node.getElementsByTagName("back")[0].childNodes[0].data
                card = Card(front, back)
                res.append(card)
            except:
                continue

        self.cards = res
        self.len = len(res)

    def read_one(self):

        if self.cur >= self.len:
            print("你已经复习完了!")
            self.write()
            self.cur = 0

        card = self.cards[self.cur]
        self.cur = self.cur + 1
        return card

    def write(self):
        with open(self.file, 'w') as f:
            self.domTree.writexml(f, encoding='utf-8')


    def add_card(self, card):
        node = self.domTree.createElement("card") 

        front_node = self.domTree.createElement("front")
        front_node_text = self.domTree.createTextNode(card.front)
        front_node.appendChild(front_node_text)

        back_node = self.domTree.createElement("back")
        back_node_text = self.domTree.createTextNode(card.back)
        back_node.appendChild(back_node_text)

        node.appendChild(front_node)
        node.appendChild(back_node)

        self.root.appendChild(node)
        self.len = self.len + 1
        self.cards.append(card)
        print("添加成功!")


    def build(self):
        doc = Document()  
        root = doc.createElement('DOCUMENT') 
        root.setAttribute('content_method',"full")
        doc.appendChild(root)

        self.domTree = doc
        self.root = root


class IO():
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

