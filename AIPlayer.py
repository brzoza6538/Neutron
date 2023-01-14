from Player import Player
import random


class AIPlayer(Player):
    def __init__(self, RowLen, Neutron, Pawns, Board, loc):
        super().__init__(RowLen, Neutron, Pawns, Board, loc)
        self._timer = 0

    def randomMove(self):
        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (self.IsMoveInDirPossible(
            self._usedPawn.X, self._usedPawn.Y, dirX, dirY
                )):
            self.move(dirX, dirY)

    def Brain(self):
        dirX, dirY = self.lookForWinInOne()
        if (dirX is not None and dirY is not None):
            self.move(dirX, dirY)

        else:
            dirX = random.randint(-1, 1)
            dirY = random.randint(-1, 1)

            if (self.IsMoveInDirPossible(
                    self._usedPawn.X, self._usedPawn.Y, dirX, dirY)):

                if (self.isMoveSafe(dirX, dirY)):
                    self.move(dirX, dirY)

    def choosePawn(self):
        self._usedPawn = self._Pawns[
            random.randint(0,  (self._RowLen - 1))]

    def isMoveSafe(self, dirX, dirY):
        stepY = self.MoveToWhere(self._usedPawn, dirX, dirY)[1]
        if (self._Neutron == self._usedPawn):
            if (
             (self._loc == "bottom" and stepY == self._RowLen - 1) or
             (self._loc == "top" and stepY == 0)
            ):
                return False
        return True

    def lookForWinInOne(self):
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                stepY = self.MoveToWhere(self._usedPawn, dirX, dirY)[1]
                if ((self._loc == "bottom" and stepY == 0)
                        or (self._loc == "top" and stepY == self._RowLen - 1)):
                    return dirX, dirY
        return None, None

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
                self.Brain()
