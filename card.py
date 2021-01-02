import setting
from xml.dom.minidom import parse, Document

class Card():
    """
    一张卡牌
    """

    def __init__(self, no, front, back, times):
        self.no = no
        self.front = front
        self.back = back
        self.times = int(times)

    #翻转功能
    def overturn(self):
        print(self.back)

    #显示问题
    def show(self):
        print(self.front)
    
    #已复习次数增加
    def add_times(self):
        if self.times < setting.MAX_TIMES:
            self.times = self.times + 1

    #剩下的复习次数增加
    def sub_times(self):
        if self.times > 0:
            self.times = self.times - 1

    #忽略这个卡牌
    def pass_card(self):
        self.times = setting.MAX_TIMES

    def clone(self):
        card = Card(self.no, self.front, self.back, self.times)
        return card


class Cards():
    """
    卡牌组
    """
    
    def __init__(self, name, path):
        self.name = name
        self.path = path 
        self.file = self.path+self.name+".xml"
        self.cards = {}
        self.len = 0
        self.cur = 1 

    #读取卡组
    def read(self):
        try:
            self.domTree = parse(self.file)
        except:
            self.build()
        self.root = self.domTree.documentElement

        res = {}
        nodes = self.domTree.getElementsByTagName("card")
        for node in nodes:
            try:
                front = node.getElementsByTagName("front")[0].childNodes[0].data
                back = node.getElementsByTagName("back")[0].childNodes[0].data
                times = node.getAttribute("times")
                no = node.getAttribute("no")
                if int(times) >= setting.MAX_TIMES:
                    continue

                card = Card(no, front, back, times)
                res[int(no)] = card
            except:
                continue

        self.cards = res
        self.len = len(res)

    def read_one_by_no(self, no):
        try:
            card = self.cards[no]
            self.cur = no + 1
        except:
            card = None 
            self.cur = 1 
        return card
    
    def read_one(self):
        card = self.read_one_by_no(self.cur)
        return card

    def write(self):
        self.rebuild()
        with open(self.file, 'w') as f:
            self.domTree.writexml(f, encoding='utf-8')


    def add_card(self, card):

        node = self.domTree.createElement("card") 
        node.setAttribute("times", str(card.times))
        node.setAttribute("no", str(card.no))

        front_node = self.domTree.createElement("front")
        front_node_text = self.domTree.createTextNode(card.front)
        front_node.appendChild(front_node_text)

        back_node = self.domTree.createElement("back")
        back_node_text = self.domTree.createTextNode(card.back)
        back_node.appendChild(back_node_text)

        node.appendChild(front_node)
        node.appendChild(back_node)

        self.root.appendChild(node)

    def new_card(self, card):
        self.len = self.len + 1
        self.cards[card.no] = card

    def rebuild(self):
        self.build()
        for no in self.cards:
            self.add_card(self.cards[no])

    def build(self):
        doc = Document()  
        root = doc.createElement('DOCUMENT') 
        root.setAttribute('content_method',"full")
        doc.appendChild(root)

        self.domTree = doc
        self.root = root

    def load_cards_from_file(self, file):
        lines = []
        card_info = []
        buf = ""
        flag = False
        with open(file, 'r') as f:
            lines = f.readlines()
        for line in lines:
            if "$" != line.rstrip() and flag:
                buf = buf + line.rstrip()+"\n"
            else:
                if flag:
                    if(buf != ""):
                        card_info.append(buf)
                        flag = False
                else:
                    if "$" == line.rstrip():
                        flag = True
                buf = ""

        self.build_cards(card_info)


    def build_cards(self, lines):
        try:
            for i in range(0, len(lines), 2):
                card = Card(self.len+1, lines[i], lines[i+1], 0)
                self.new_card(card)
        except:
            print("卡片的前后数量不匹配")
       
        
    


                

