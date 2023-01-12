from Player import Player
import random


class RandomPlayer(Player):
    def ruch(self):
        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (self.IsMoveInDirPossible(
            self._usedPawn.X, self._usedPawn.Y, dirX, dirY
                )):
            self.move(self._usedPawn, dirX, dirY)

    def choosePawn(self):
        self._usedPawn = self._Pawns[
            random.randint(0,  (self._Window.numOfSpaces - 1))]

    def Update(self):

        if (not self._pawnMoved):
            self.choosePawn()
            if (self._usedPawn is not None):
                self.ruch()

        if (self.isNeutronMovable()):
            if (not self._neutronMoved and self._pawnMoved):
                self._usedPawn = self._Neutron
                self.ruch()
