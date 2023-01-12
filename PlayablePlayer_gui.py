class PlayablePlayer_gui():
    def __init__(self, Window):
        self._Window = Window
        self._line = None

    @property
    def MouseX(self):
        return self._Window.MouseX

    @property
    def MouseY(self):
        return self._Window.MouseY

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

    def ShowLine(self, x0, y0, x1, y1):
        self._Window._Canvas.delete(self._line)

        fieldsize = self._Window._FrameWidth + self._Window._FieldSize

        self._line = self._Window._Canvas.create_line(
            x0 * fieldsize + fieldsize/2,
            y0 * fieldsize + fieldsize/2,
            x1 * fieldsize + fieldsize/2,
            y1 * fieldsize + fieldsize/2,
            fill="Red",
            width=5
        )

    def DelLine(self):
        self._Window._Canvas.delete(self._line)

    def PawnClickedOn(self, pawn):
        if (self.isMouseOnPawn(pawn) and self._Window.CheckClicked()):
            return True
        return False

    def CheckClicked(self):
        if (self._Window.CheckClicked()):
            return True
        return False
