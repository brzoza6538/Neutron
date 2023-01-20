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

    def SetSpace(self, x, y, set):
        """puts set on field (x, y)"""
        self._board[x][y] = set

    def ClearSpace(self, x, y):
        """clears field (x,y), putting in None"""
        self._board[x][y] = None

    def IsFull(self, x, y):
        """is field (x,y) occupied"""
        if (self._board[x][y] is not None):
            return True
        return False

    def VisualRepr(self):
        """returns a string representation of the board. Used range() because
        'for row in board, for field in row' 
        would show the board rotated to the left"""
        str = ""
        for y in range(len(self._board)):
            for x in range(len(self._board[y])):
                if (not self.IsFull(x, y)):
                    str += ("\t" + "O")
                else:
                    str += ("\t" + self._board[x][y].value)

            str += "\n"

        return str
