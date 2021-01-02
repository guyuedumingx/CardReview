import setting

class Card():

    def __init__(self, front, back, times):
        self.front = front
        self.back = back
        self.times = int(times)


    def overturn(self):
        print(self.back)

    def show(self):
        print(self.front)
    
    def add_times(self):
        if self.times < setting.MAX_TIMES:
            self.times = self.times + 1

    def sub_times(self):
        if self.times > 0:
            self.times = self.times - 1

    def pass_card(self):
        self.times = setting.MAX_TIMES
