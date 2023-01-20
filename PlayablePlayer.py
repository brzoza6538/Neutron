from Player import Player
from PlayablePlayerGui import PlayablePlayerGui


class PlayablePlayer(Player):
    def __init__(self, rowlen, window, neutron, pawns, board, set):
        super().__init__(rowlen, neutron, pawns, board, set)
        self._window = window
        self._gui = PlayablePlayerGui(self._window)

    def Turn(self):
        """lets player make a move"""
        pawn = self._usedPawn
        dirX = self._gui.mouseX - pawn.x
        if dirX > 0:
            dirX = 1
        if dirX < 0:
            dirX = -1
        dirY = self._gui.mouseY - pawn.y
        if dirY > 0:
            dirY = 1
        if dirY < 0:
            dirY = -1

        x1, y1 = self.MoveToWhere(pawn, dirX, dirY)
        self._gui.ShowLine(pawn.x, pawn.y, x1, y1)

        if (self._gui.CheckClicked()):
            if (self.IsMoveInDirPossible(pawn.x, pawn.y, dirX, dirY)):
                if (not self.ChangePawnMidMove()):
                    self._gui.DelLine()
                    self.Move(dirX, dirY)
                    self._usedPawn = None
            else:
                self.ChangePawnMidMove()

    def ChangePawnMidMove(self):
        """changes pawns when player clicks on a pawn,
        while he's pointing a currently used pawn to move at it"""
        for pawn in self._pawns:
            if (pawn.x == self._gui.mouseX and
                    pawn.y == self._gui.mouseY):
                self._usedPawn = pawn
                return True
        return False

    def ChoosePawn(self):
        for pawn in self._pawns:
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
                self._usedPawn = self._neutron
                self.Turn()
