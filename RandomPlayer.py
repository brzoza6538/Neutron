from Player import Player
import random


class RandomPlayer(Player):

    def __init__(self, Window, Neutron, Pawns, Board):
        super().__init__(Window, Neutron, Pawns, Board)

    def pawnTurn(self):

        while True:
            # print("pawn:")
            # data = int(input())
            # usedPawn = self._Pawns[data]
            # dirX = int(input())
            # dirY = int(input())
            usedPawn = self._Pawns[
                random.randint(0,  (self._Window.numOfSpaces - 1))
                ]
            dirX = random.randint(-1, 1)
            dirY = random.randint(-1, 1)

            if (self.IsMoveInDirPossible(usedPawn.X, usedPawn.Y, dirX, dirY)):
                self.move(usedPawn, dirX, dirY)
                break

    def neutronTurn(self):

        while True:
            dirX = random.randint(-1, 1)
            dirY = random.randint(-1, 1)
            # print("neutron:")
            # dirX = int(input())
            # dirY = int(input())

            if (self.IsMoveInDirPossible(
                self._Neutron.X, self._Neutron.Y, dirX, dirY
                    )):
                self.move(self._Neutron, dirX, dirY)
                break

    def Update(self):
        self._Window._Canvas.delete(self._line)

        self.pawnTurn()

        if (self.isNeutronMovable()):
            self.neutronTurn()
        else:
            self._immobileNeutron = False
