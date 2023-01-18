from Variables import Type, Set


class Player:
    def __init__(self, rowlen, neutron, pawns, board, set):
        self._set = set
        self._rowlen = rowlen
        self._board = board
        self._pawns = pawns
        self._neutron = neutron
        self._usedPawn = None

        self._pawnMoved = False
        self._neutronMoved = False

        self._immobileNeutron = False

        self._movedPawn = None
        if (self._set == Set.TOP):
            self._baseRow = 0
            self._enemyRow = rowlen - 1
        else:
            self._baseRow = rowlen - 1
            self._enemyRow = 0

    @property
    def usedPawn(self):
        return self._usedPawn

    @property
    def neutron(self):
        return self._neutron

    @property
    def immobileNeutron(self):
        return self._immobileNeutron

    @property
    def set(self):
        return self._set

    @property
    def pawns(self):
        return self._pawns

    def Render(self):
        for pawn in range(5):
            self._pawns[pawn].Update()

    def IsMoveInDirPossible(self, x0, y0, dirX, dirY):
        """sprawdza czy ruch możliwy, ruch o 0 pól oznacza że niemożliwy"""
        if (
            (x0 + dirX > (self._rowlen - 1)) or
            (y0 + dirY > (self._rowlen - 1)) or
            (x0 + dirX < 0) or (y0 + dirY < 0)
                ):
            return False
        elif (self._board.IsFull(x0 + dirX, y0 + dirY)):
            return False
        return True

    def IsNeutronMovable(self):
        x0 = self._neutron.x
        y0 = self._neutron.y
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                if (self.IsMoveInDirPossible(x0, y0, dirX, dirY)):
                    return True
        self._immobileNeutron = True
        return False

    def MoveToWhere(self, pawn, x, y):
        """sprawdza zasieg ruchu"""
        xCheck = pawn.x
        yCheck = pawn.y
        while True:
            if (not self.IsMoveInDirPossible(xCheck, yCheck, x, y)):
                break

            xCheck += x
            yCheck += y

        return xCheck, yCheck

    def Move(self, x, y):
        """x, y przyjmuja wartość -1, 0, 1"""
        pawn = self._usedPawn
        if (pawn.set == Type.NEUTRON):
            self._neutronMoved = True
        else:
            self._pawnMoved = True

        stepX, stepY = self.MoveToWhere(pawn, x, y)

        self._board.ClearSpace(pawn.x, pawn.y)
        self._board.SetSpace(stepX, stepY, pawn.set)

        pawn.Move(stepX, stepY)
        self._movedPawn = pawn

    def IsTurnFinished(self):
        if (self._neutronMoved and self._pawnMoved):
            self._neutronMoved = False
            self._pawnMoved = False
            return True
        return False

    def WhatMoved(self):
        pomoc = self._movedPawn
        self._movedPawn = None
        return pomoc

    def Update(self):
        pass
