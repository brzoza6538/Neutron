from Player import Player
import random


class RandomPlayer(Player):

    def __init__(self, Window, Neutron, Pawns, Board):
        super().__init__(Window, Neutron, Pawns, Board)
        self._neutronLine = None

    def turn(self, pawn, line):

        while True:
            dirX = random.randint(-1, 1)
            dirY = random.randint(-1, 1)

            if (self.IsMovePossible(pawn, dirX, dirY)):
                self.move(pawn, dirX, dirY)
                break

    def Update(self):
        self._Window._Canvas.delete(self._line)
        self._Window._Canvas.delete(self._neutronLine)

        self._usedPawn = self._Pawns[random.randint(0,  (self._Window.numOfSpaces - 1))]

        self.turn(self._usedPawn, self._line)

        self.turn(self._Neutron, self._neutronLine)

        self._Window.Update()
