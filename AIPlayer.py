from Player import Player
import random


class AIPlayer(Player):
    def __init__(self, rowLen, neutron, pawns, board, set):
        super().__init__(rowLen, neutron, pawns, board, set)

    def IsTheOnlyNeutronMoveSuicidal(self):
        """are there any moves that won't result in defeat"""
        for dirX in [-1, 0, 1]:
            for dirY in [-1, 0, 1]:
                if (self.IsMoveInDirPossible(
                        self._neutron.x, self._neutron.y, dirX, dirY)):
                    if (self.IsMoveSafe(dirX, dirY)):
                        return False
        return True

    def RandomMove(self):
        """moves pawn in a random direction if possible"""
        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (self.IsMoveInDirPossible(
            self._usedPawn.x, self._usedPawn.y, dirX, dirY
                )):
            self.Move(dirX, dirY)

    def Brain(self):
        """chooses what kind of move to make with neutron"""
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
        """choose pawn to move"""
        self._usedPawn = self._pawns[
            random.randint(0,  (self._rowlen - 1))]

    def IsMoveSafe(self, dirX, dirY):
        """will move result in defeat"""
        stepY = self.MoveToWhere(self._usedPawn, dirX, dirY)[1]
        if (self._neutron == self._usedPawn):
            if (self._baseRow == stepY):
                return False
        return True

    def LookForWinInOne(self):
        """can you win with one move of neutron"""
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
