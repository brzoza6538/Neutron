class Player:
    def __init__(self, RowLen, Neutron, Pawns, Board, loc):
        self._loc = loc
        self._RowLen = RowLen
        self._Board = Board
        self._Pawns = Pawns
        self._Neutron = Neutron
        self._usedPawn = None

        self._pawnMoved = False
        self._neutronMoved = False

        self._immobileNeutron = False

        self._movedPawn = None
        if (self._loc == "top"):
            self._BaseRow = 0
            self._enemyRow = RowLen - 1
        else:
            self._BaseRow = RowLen - 1
            self._enemyRow = 0

    @property
    def loc(self):
        return self._loc

    def Render(self):
        for pawn in range(5):
            self._Pawns[pawn].Update()

    def IsMoveInDirPossible(self, x0, y0, dirX, dirY):
        """sprawdza czy ruch możliwy, ruch o 0 pól oznacza że niemożliwy"""
        if (
            (x0 + dirX > (self._RowLen - 1)) or
            (y0 + dirY > (self._RowLen - 1)) or
            (x0 + dirX < 0) or (y0 + dirY < 0)
                ):
            return False
        elif (self._Board.IsFull(x0 + dirX, y0 + dirY)):
            return False
        return True

    def IsNeutronMovable(self):
        x0 = self._Neutron.X
        y0 = self._Neutron.Y
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                if (self.IsMoveInDirPossible(x0, y0, dirX, dirY)):
                    return True
        self._immobileNeutron = True
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

    def Move(self, x, y):
        """x, y przyjmuja wartość -1, 0, 1"""
        pawn = self._usedPawn
        if (pawn.set == "Neutron"):
            self._neutronMoved = True
        else:
            self._pawnMoved = True

        stepX, stepY = self.MoveToWhere(pawn, x, y)

        self._Board.ClearSpace(pawn._X, pawn._Y)
        self._Board.SetSpace(stepX, stepY, pawn.set)

        pawn.Move(stepX, stepY)
        self._movedPawn = pawn

    def IsTurnFinished(self):
        if (self._neutronMoved and self._pawnMoved):
            self._neutronMoved = False
            self._pawnMoved = False
            return True
        else:
            return False

    def WhatMoved(self):
        pomoc = self._movedPawn
        self._movedPawn = None
        return pomoc

    def Update(self):
        pass
