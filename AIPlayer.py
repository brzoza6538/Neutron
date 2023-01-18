from Player import Player
import random


class AIPlayer(Player):
    def __init__(self, rowLen, neutron, pawns, board, set):
        super().__init__(rowLen, neutron, pawns, board, set)

    def IsTheOnlyNeutronMoveSuicidal(self):
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                if (self.IsMoveInDirPossible(
                        self._neutron.x, self._neutron.y, dirX, dirY)):
                    if (self.IsMoveSafe(dirX, dirY)):
                        return False
        return True

    def RandomMove(self):
        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (self.IsMoveInDirPossible(
            self._usedPawn.x, self._usedPawn.y, dirX, dirY
                )):
            self.Move(dirX, dirY)

    def Brain(self):
        dirX, dirY = self.LookForWinInOne()
        if (dirX is not None and dirY is not None):
            self.Move(dirX, dirY)

        else:
            dirX = random.randint(-1, 1)
            dirY = random.randint(-1, 1)

            if (self.IsMoveInDirPossible(
                    self._usedPawn.x, self._usedPawn.y, dirX, dirY)):
                var = self.IsTheOnlyNeutronMoveSuicidal()
                if (self.IsMoveSafe(dirX, dirY)
                        or var):
                    self.Move(dirX, dirY)

    def ChoosePawn(self):
        self._usedPawn = self._pawns[
            random.randint(0,  (self._rowlen - 1))]

    def IsMoveSafe(self, dirX, dirY):
        stepY = self.MoveToWhere(self._usedPawn, dirX, dirY)[1]
        if (self._neutron == self._usedPawn):
            if (self._baseRow == stepY):
                return False
        return True

    def LookForWinInOne(self):
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                stepY = self.MoveToWhere(self._usedPawn, dirX, dirY)[1]
                if (self._enemyRow == stepY):
                    return dirX, dirY
        return None, None

    def Update(self):
        neutronCheck = self.IsNeutronMovable()
        if (not self._pawnMoved):
            self.ChoosePawn()
            if (self._usedPawn is not None):
                self.RandomMove()

        elif (neutronCheck):
            if (not self._neutronMoved and self._pawnMoved):
                self._usedPawn = self._neutron
                self.Brain()
