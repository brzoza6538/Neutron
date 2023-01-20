class PlayablePlayerGui():
    def __init__(self, Window):
        self._window = Window
        self._line = None

    @property
    def mouseX(self):
        return self._window.mouseX

    @property
    def mouseY(self):
        return self._window.mouseY

    def IsMouseOnPawn(self, pawn):
        if (
            self._window.mouseX == pawn.x and
            self._window.mouseY == pawn.y
        ):
            self._window.ChangePawnColor(pawn, "Orange")
            return True
        else:
            self._window.ChangePawnColor(pawn, pawn.color)
            return False

    def ShowLine(self, x0, y0, x1, y1):
        self._window.canvas.delete(self._line)

        fieldsize = self._window.frameWidth + self._window.fieldSize

        self._line = self._window.canvas.create_line(
            x0 * fieldsize + fieldsize/2,
            y0 * fieldsize + fieldsize/2,
            x1 * fieldsize + fieldsize/2,
            y1 * fieldsize + fieldsize/2,
            fill="Red",
            width=5
        )

    def DelLine(self):
        self._window.canvas.delete(self._line)

    def PawnClickedOn(self, pawn):
        if (self.IsMouseOnPawn(pawn) and self._window.CheckClicked()):
            return True
        return False

    def CheckClicked(self):
        if (self._window.CheckClicked()):
            return True
        return False