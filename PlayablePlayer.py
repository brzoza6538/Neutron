from Player import Player


class PlayablePlayer(Player):

    def __init__(self, Window, Neutron, Pawns, Board):
        super().__init__(Window, Neutron, Pawns, Board)

        self._line = self._Window._Canvas.create_line(
            1, 1,
            1, 1,
            fill='Red',
            width=5
        )

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
