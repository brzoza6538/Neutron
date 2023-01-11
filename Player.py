class Player:
    def __init__(self, Window, Neutron, Pawns, Board):
        self._Window = Window
        self._Board = Board
        self._Pawns = Pawns
        self._Neutron = Neutron

        self._pawnMoved = False
        self._neutronMoved = False
        self._line = None

        self._immobileNeutron = False

    def Render(self):
        for pawn in range(5):
            self._Pawns[pawn].Update()

    def IsMoveInDirPossible(self, x0, y0, dirX, dirY):
        """sprawdza czy ruch możliwy, ruch o 0 pól oznacza że niemożliwy"""
        if (
            (x0 + dirX > (self._Window.numOfSpaces - 1)) or
            (y0 + dirY > (self._Window.numOfSpaces - 1)) or
            (x0 + dirX < 0) or (y0 + dirY < 0)
                ):
            return False
        elif (self._Board.isFull(x0 + dirX, y0 + dirY)):
            return False
        return True

    def isNeutronMovable(self):
        x0 = self._Neutron.X
        y0 = self._Neutron.Y
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                if (self.IsMoveInDirPossible(x0, y0, dirX, dirY)):
                    return True
        return False

    def MoveToWhere(self, pawn, x, y):
        """sprawdza zasieg ruchu"""
        xCheck = pawn.X
        yCheck = pawn.Y
        while True:
            if (not self.IsMoveInDirPossible(xCheck, yCheck, x, y)):
                break

            xCheck += x
            yCheck += y

        return xCheck, yCheck

    def move(self, pawn, x, y):
        """x, y przyjmuja wartość -1, 0, 1"""

        stepX, stepY = self.MoveToWhere(pawn, x, y)

        self._Board.clearSpace(pawn._X, pawn._Y)
        self._Board.setSpace(stepX, stepY, pawn.type)

        pawn.move(stepX, stepY)

    def Update(self):
        pass
