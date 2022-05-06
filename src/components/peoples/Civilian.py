import src.components.People as People

class Civilian(People):

    def __init__(self, destination):
        super().__init__()
        self.__destination= destination
        self.led = False