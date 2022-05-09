import src.components.People as People

class Civilian(People):

    def __init__(self, name, position, destionation):
        super().__init__(name, position)
        self.__position = position
        self.__destination = destionation