from Player import Player
import random


class AIPlayer(Player):
    def __init__(self, RowLen, Neutron, Pawns, Board, loc):
        super().__init__(RowLen, Neutron, Pawns, Board, loc)

    def IsTheOnlyNeutronMoveSuicidal(self):
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                if (self.IsMoveInDirPossible(
                        self._Neutron.X, self._Neutron.Y, dirX, dirY)):
                    if (self.isMoveSafe(dirX, dirY)):
                        return False
        return True

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
                var = self.IsTheOnlyNeutronMoveSuicidal()
                if (self.isMoveSafe(dirX, dirY)
                        or var):
                    self.move(dirX, dirY)

    def choosePawn(self):
        self._usedPawn = self._Pawns[
            random.randint(0,  (self._RowLen - 1))]

    def isMoveSafe(self, dirX, dirY):
        stepY = self.MoveToWhere(self._usedPawn, dirX, dirY)[1]
        if (self._Neutron == self._usedPawn):
            if (self._BaseRow == stepY):
                return False
        return True

    def lookForWinInOne(self):
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                stepY = self.MoveToWhere(self._usedPawn, dirX, dirY)[1]
                if (self._enemyRow == stepY):
                    return dirX, dirY
        return None, None

    def Update(self):
        neutronCheck = self.isNeutronMovable()
        if (not self._pawnMoved):
            self.choosePawn()
            if (self._usedPawn is not None):
                self.randomMove()

        elif (neutronCheck):
            if (not self._neutronMoved and self._pawnMoved):
                self._usedPawn = self._Neutron
                self.Brain()
