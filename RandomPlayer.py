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
                self.ShowLine(pawn, dirX, dirY, line)
                self.move(pawn, dirX, dirY)
                break

    def ShowLine(self, pawn, dirX, dirY, line):
        """trajektoria pionka - mogę tylko przesunąć w całości - jakoś trzeba widzieć jak wygląda ruch"""
        x, y = self.MoveToWhere(pawn, dirX, dirY)
        fieldsize = self._Window._FrameWidth + self._Window._FieldSize

        if (line == self._line):
            self._Window._Canvas.delete(self._line)

            self._line = self._Window._Canvas.create_line(
                pawn.X * fieldsize + fieldsize/2,
                pawn.Y * fieldsize + fieldsize/2,
                x * fieldsize + fieldsize/2,
                y * fieldsize + fieldsize/2,
                fill="Blue",
                width=5
            )
        else:
            self._Window._Canvas.delete(self._neutronLine)

            self._neutronLine = self._Window._Canvas.create_line(
                pawn.X * fieldsize + fieldsize/2,
                pawn.Y * fieldsize + fieldsize/2,
                x * fieldsize + fieldsize/2,
                y * fieldsize + fieldsize/2,
                fill="Blue",
                width=5
            )

    def Update(self):
        self._Window._Canvas.delete(self._line)
        self._Window._Canvas.delete(self._neutronLine)

        self._usedPawn = self._Pawns[random.randint(0, 4)]

        self.turn(self._usedPawn, self._line)

        self.turn(self._Neutron, self._neutronLine)

        self._Window.Update()
