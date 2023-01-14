from Player import Player
import random


class RandomPlayer(Player):
    def __init__(self, RowLen, Neutron, Pawns, Board):
        super().__init__(RowLen, Neutron, Pawns, Board)
        self._timer = 0

    def randomMove(self):
        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (self.IsMoveInDirPossible(
            self._usedPawn.X, self._usedPawn.Y, dirX, dirY
                )):
            self.move(self._usedPawn, dirX, dirY)

    def choosePawn(self):
        self._usedPawn = self._Pawns[
            random.randint(0,  (self._RowLen - 1))]

    def Update(self):
        self._timer += 1
        neutronCheck = self.isNeutronMovable()
        if (not self._pawnMoved):
            self.choosePawn()
            if (self._usedPawn is not None):
                self.randomMove()

        elif (neutronCheck):
            if (not self._neutronMoved and self._pawnMoved):
                self._usedPawn = self._Neutron
                self.randomMove()
