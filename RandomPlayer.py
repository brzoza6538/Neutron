from Player import Player
import random


class RandomPlayer(Player):
    def __init__(self, rowlen, neutron, pawns, board, set):
        super().__init__(rowlen, neutron, pawns, board, set)

    def RandomMove(self):
        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (self.IsMoveInDirPossible(
            self._usedPawn.x, self._usedPawn.y, dirX, dirY
                )):
            self.Move(dirX, dirY)

    def ChoosePawn(self):
        self._usedPawn = self._pawns[
            random.randint(0,  (self._rowlen - 1))]

    def Update(self):
        neutronCheck = self.IsNeutronMovable()
        if (not self._pawnMoved):
            self.ChoosePawn()
            if (self._usedPawn is not None):
                self.RandomMove()

        elif (neutronCheck):
            if (not self._neutronMoved and self._pawnMoved):
                self._usedPawn = self._neutron
                self.RandomMove()
