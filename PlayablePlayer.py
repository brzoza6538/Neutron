from Player import Player


class PlayablePlayer(Player):

    def __init__(self, Window, Neutron, Pawns, Board):
        super().__init__(Window, Neutron, Pawns, Board)

    def isMouseOnPawn(self, pawn):
        if (
            self._Window.MouseX == pawn._X and
            self._Window.MouseY == pawn._Y
        ):
            self._Window._Canvas.itemconfig(pawn._pawn, fill="Orange")
            return True
        else:
            self._Window._Canvas.itemconfig(pawn._pawn, fill=pawn._color)
            return False

    def move(self, pawn, x, y):
        Player.move(self, pawn, x, y)
        self._Window._Canvas.delete(self._line)

    def turn(self, pawn):
        """zwraca prawda/fałsz czy pionek sie poruszył"""

        dirX = self._Window.MouseX - pawn._X
        if dirX > 0:
            dirX = 1
        if dirX < 0:
            dirX = -1
        dirY = self._Window.MouseY - pawn._Y
        if dirY > 0:
            dirY = 1
        if dirY < 0:
            dirY = -1
        self.ShowLine(pawn, dirX, dirY)

        if (self._Window.CheckClicked() is True):
            if (self.IsMovePossible(pawn, dirX, dirY)):
                self.move(pawn, dirX, dirY)
                return True
        return False

    def isTurnFinished(self):
        if (self._neutronMoved and self._pawnMoved):
            self._neutronMoved = False
            self._pawnMoved = False
            self._usedPawn = None
            return True
        else:
            return False

    def Update(self):
        # self.turn(self._Neutron)
        if (not self._pawnMoved):
            for pawn in self._Pawns:
                if (self.isMouseOnPawn(pawn) and self._Window.CheckClicked()):
                    self._usedPawn = pawn

            if (self._usedPawn is not None):
                self._pawnMoved = self.turn(self._usedPawn)

        if (not self._neutronMoved and self._pawnMoved):
            self._neutronMoved = self.turn(self._Neutron)

        self._Window.Update()
