

class Board:
    def __init__(self, Window):
        self._Window = Window
        self._Board = [[None for x in range(self._Window.numOfSpaces)] for y in range(self._Window.numOfSpaces)]

    def setSpace(self, x, y, type):
        self._Board[x][y] = type

    def clearSpace(self, x, y):
        self._Board[x][y] = None

    def showSpace(self, x, y):
        return self._Board[x][y]

    def isFull(self, x, y):
        if (self._Board[x][y] is not None):
            return True
        else:
            return False

    def __str__(self):
        str = ""
        for y in range(len(self._Board)):
            for x in range(len(self._Board[y])):
                if (not self.isFull(x, y)):
                    str += ("\t" + "O")
                else:
                    str += ("\t" + self._Board[x][y])

            str += "\n"

        return str
