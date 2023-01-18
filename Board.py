class Board:
    def __init__(self, rowlen):
        self._rowlen = rowlen
        self._board = self.CreateBoard()

    @property
    def board(self):
        return self._board

    def CreateBoard(self):
        Board = [
            [None for x in range(self._rowlen)]
            for y in range(self._rowlen)
            ]

        return Board

    def OnField(self, x, y):
        return self._board[x][y]

    def SetSpace(self, x, y, set):
        self._board[x][y] = set

    def ClearSpace(self, x, y):
        self._board[x][y] = None

    def ShowSpace(self, x, y):
        return self._board[x][y]

    def IsFull(self, x, y):
        if (self._board[x][y] is not None):
            return True
        return False

    def VisualRepr(self):
        str = ""
        for row in self._board:
            for field in row:
                if (field is None):
                    str += ("\t" + "O")
                else:
                    str += ("\t" + field)

            str += "\n"

        return str

    def VisualRepr_90Deg(self):
        str = ""
        for y in range(len(self._board)):
            for x in range(len(self._board[y])):
                if (not self.IsFull(x, y)):
                    str += ("\t" + "O")
                else:
                    str += ("\t" + self._board[x][y])

            str += "\n"

        return str
