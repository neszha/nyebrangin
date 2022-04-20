import src.People as People

class NPC(People):

    def __init__(self, move):
        super().__init__()
        self.move = move

    def movement(self):
        pass