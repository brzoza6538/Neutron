import Window


class Player:
    def __init__(self, Window: Window, Neutron, Pawns, Board):
        self._Window = Window
        self._Board = Board
        self._Pawns = Pawns
        self._Neutron = Neutron

        self._usedPawn = None
        self._pawnMoved = False
        self._neutronMoved = False
        self._line = None

    def Render(self):
        for pawn in range(5):
            self._Pawns[pawn].Update()

    def IsMovePossible(self, pawn, x, y):
        """sprawdza czy ruch możliwy, ruch o 0 pól oznacza że niemożliwy"""
        XCheck = pawn._X
        YCheck = pawn._Y

        if ((XCheck + x > 4) or (YCheck + y > 4) or (XCheck + x < 0) or (YCheck + y < 0)):
            return False
        elif (self._Board[XCheck + x][YCheck + y] is not None):
            return False
        return True

    def MoveToWhere(self, pawn, x, y):
        """sprawdza zasieg ruchu"""
        XCheck = pawn._X
        YCheck = pawn._Y
        while True:
            if ((XCheck + x > 4) or (YCheck + y > 4) or (XCheck + x < 0) or (YCheck + y < 0)):
                break
            elif (self._Board[XCheck + x][YCheck + y] is not None):
                break

            XCheck += x
            YCheck += y
        return XCheck, YCheck

    def move(self, pawn, x, y):
        """x, y przyjmuja wartość -1, 0, 1"""
        XCheck = pawn._X
        YCheck = pawn._Y
        while True:
            if ((XCheck + x > 4) or (YCheck + y > 4) or (XCheck + x < 0) or (YCheck + y < 0)):
                break
            elif (self._Board[XCheck + x][YCheck + y] is not None):
                break

            XCheck += x
            YCheck += y

        self._Board[pawn._X][pawn._Y] = None
        self._Board[XCheck][YCheck] = pawn.type

        pawn.move(XCheck, YCheck)

    def ShowLine(self, pawn, dirX, dirY):
        self._Window._Canvas.delete(self._line)

        x, y = self.MoveToWhere(pawn, dirX, dirY)

        fieldsize = self._Window._FrameWidth + self._Window._FieldSize

        self._line = self._Window._Canvas.create_line(
            pawn.X * fieldsize + fieldsize/2,
            pawn.Y * fieldsize + fieldsize/2,
            x * fieldsize + fieldsize/2,
            y * fieldsize + fieldsize/2,
            fill="Red",
            width=5
        )

    def Update(self):
        pass
        # self._Window.Update()
