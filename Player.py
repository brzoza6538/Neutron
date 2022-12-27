class Player:
    def __init__(self, Window, Neutron, Pawns, Board):
        self._Window = Window
        self._Board = Board
        self._Pawns = Pawns
        self._Neutron = Neutron

        self._usedPawn = None
        self._pawnMoved = False
        self._neutronMoved = False

    def Render(self):
        for pawn in range(5):
            self._Pawns[pawn].Update()

    def IsMovePossible(self, pawn, x, y):
        """sprawdza czy ruch możliwy"""
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
        self._Window._Canvas.delete(self._line)

    def ShowLine(self, pawn, dirX, dirY):
        self._Window._Canvas.delete(self._line)

        x = self.MoveToWhere(pawn, dirX, dirY)[0]
        y = self.MoveToWhere(pawn, dirX, dirY)[1]

        fieldsize = self._Window._FrameWidth + self._Window._FieldSize

        self._line = self._Window._Canvas.create_line(
            pawn.X * fieldsize + fieldsize/2,
            pawn.Y * fieldsize + fieldsize/2,
            x * fieldsize + fieldsize/2,
            y * fieldsize + fieldsize/2,
            fill="Red",
            width=5
        )

    def turn(self, pawn):
        """zwraca prawda/fałsz czy pionek sie poruszył"""
        dirX = self._Window.MouseX - pawn._X
        if dirX > 0:
            dirX = 1
        if dirX < 0:
            dirX = -1
        dirY = self._Window.MouseY - pawn._Y
        if dirY > 0:
            dirY = 1
        if dirY < 0:
            dirY = -1
        self.ShowLine(pawn, dirX, dirY)

        if (self._Window.CheckClicked() is True):
            if (self.IsMovePossible(pawn, dirX, dirY)):
                self.move(pawn, dirX, dirY)
                return True
        return False

    def Update(self):
        pass
