
class Card():

    def __init__(self, front, back):
        self.front = front
        self.back = back

    def overturn(self):
        print(self.back)

    def show(self):
        print(self.front)
        print("--------------------------------------------------")