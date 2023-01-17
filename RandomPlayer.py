from Player import Player
import random


class RandomPlayer(Player):
    def __init__(self, RowLen, Neutron, Pawns, Board, loc):
        super().__init__(RowLen, Neutron, Pawns, Board, loc)

    def RandomMove(self):
        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (self.IsMoveInDirPossible(
            self._usedPawn.X, self._usedPawn.Y, dirX, dirY
                )):
            self.Move(dirX, dirY)

    def ChoosePawn(self):
        self._usedPawn = self._Pawns[
            random.randint(0,  (self._RowLen - 1))]

    def Update(self):
        neutronCheck = self.IsNeutronMovable()
        if (not self._pawnMoved):
            self.ChoosePawn()
            if (self._usedPawn is not None):
                self.RandomMove()

        elif (neutronCheck):
            if (not self._neutronMoved and self._pawnMoved):
                self._usedPawn = self._Neutron
                self.RandomMove()
