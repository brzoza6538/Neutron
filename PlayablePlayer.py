from Player import Player
from PlayablePlayer_gui import PlayablePlayer_gui


class PlayablePlayer(Player):
    def __init__(self, RowLen, Window, Neutron, Pawns, Board, loc):
        super().__init__(RowLen, Neutron, Pawns, Board, loc)
        self._Window = Window
        self._gui = PlayablePlayer_gui(self._Window)

    def Turn(self):
        pawn = self._usedPawn
        dirX = self._gui.MouseX - pawn._X
        if dirX > 0:
            dirX = 1
        if dirX < 0:
            dirX = -1
        dirY = self._gui.MouseY - pawn._Y
        if dirY > 0:
            dirY = 1
        if dirY < 0:
            dirY = -1

        x1, y1 = self.MoveToWhere(pawn, dirX, dirY)
        self._gui.ShowLine(pawn.X, pawn.Y, x1, y1)

        if (self._gui.CheckClicked()):
            if (self.IsMoveInDirPossible(pawn.X, pawn.Y, dirX, dirY)):
                var = self._Board.onField(self._gui.MouseX, self._gui.MouseY)
                if (var != self._loc):
                    self._gui.DelLine()
                    self.Move(dirX, dirY)
                    self._usedPawn = None

    def ChoosePawn(self):
        for pawn in self._Pawns:
            if (self._gui.PawnClickedOn(pawn)):
                self._usedPawn = pawn

    def Update(self):
        neutronCheck = self.IsNeutronMovable()
        if (not self._pawnMoved):
            self.ChoosePawn()
            if (self._usedPawn is not None):
                self.Turn()

        if (neutronCheck):
            if (not self._neutronMoved and self._pawnMoved):
                self._usedPawn = self._Neutron
                self.Turn()
