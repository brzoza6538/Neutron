import tkinter
import time
from Variables import Colors


class Window:

    def __init__(self, rowlen) -> None:
        # constants
        self._numOfSpaces = rowlen
        self._frameWidth = 5
        self._fieldSize = 50
        self._windowWidth = (
            (self._numOfSpaces*self._fieldSize) +
            (self._frameWidth*(self._numOfSpaces+1))
            )
        self._windowHeight = (
            (self._numOfSpaces*self._fieldSize) +
            (self._frameWidth*(self._numOfSpaces+1))
            )

        self._ballRadius = int(self._fieldSize/2) - 6

        self._betweenStepsDelay = 0.01
        self._step = int(self._windowWidth / 50)

        self._font = 'Helvetica 25 bold'
        # Window
        self._window = tkinter.Tk()
        self._window.title("Neutron")
        self._window.geometry(f'{self._windowWidth}x{self._windowHeight}')
        # canvas
        self._canvas = tkinter.Canvas(self._window)
        self._canvas.configure(bg=Colors.BACKGROUND.value)
        self._canvas.pack(fill="both", expand=True)
        # mouse
        self._window.bind('<Motion>', self.MousePosition)
        self._window.bind("<1>", self.Clicked)
        self._mouseX = 0
        self._mouseY = 0
        self._clicked = False
        self._pawns = None
        self.SetFrame()

    @property
    def fieldSize(self):
        return self._fieldSize

    @property
    def canvas(self):
        return self._canvas

    @property
    def frameWidth(self):
        return self._frameWidth

    @property
    def numOfSpaces(self):
        return self._numOfSpaces

    @property
    def size(self):
        return self._windowWidth

    @property
    def mouseX(self):
        return self._mouseX

    @property
    def mouseY(self):
        return self._mouseY

    def MousePosition(self, e):
        self._mouseX = int(e.x / (self._frameWidth + self._fieldSize + 1))
        self._mouseY = int(e.y / (self._frameWidth + self._fieldSize + 1))

    def Clicked(self, e):
        self._clicked = True

    def CheckClicked(self):
        if self._clicked is True:
            self._clicked = False
            return True
        return False

    def SetFrame(self):
        """split board into fields"""
        width = self._frameWidth
        skip = self._fieldSize
        # X
        for line in range(self._numOfSpaces+1):
            self._canvas.create_rectangle(
                (width+skip)*line, 0,
                (width+skip)*line + width, self._windowHeight-1,
                fill=Colors.FRAME.value)
        # Y
        for line in range(self._numOfSpaces+1):
            self._canvas.create_rectangle(
                0, (width+skip)*line,
                self._windowWidth-1, (width+skip)*line + width,
                fill=Colors.FRAME.value)

    def SetPawns(self, topPawns, neutron, bottomPawns):
        """set pawns on the window"""
        self._pawns = {}
        for pawn in topPawns:
            self._pawns[pawn] = self.CreatePawn(pawn.color, pawn.x, pawn.y)

        for pawn in bottomPawns:
            self._pawns[pawn] = self.CreatePawn(pawn.color, pawn.x, pawn.y)

        self._pawns[neutron] = self.CreatePawn(
            neutron.color, neutron.x, neutron.y)

    def ChangePawnColor(self, pawn, color):
        """chenges a color of a pawn to color"""
        gPawn = self._pawns[pawn]
        self._canvas.itemconfig(gPawn, fill=color)
        self.Update()

    def CreatePawn(self, color, x, y):
        """creates visual representation of a pawn"""
        starter = self._frameWidth + int(self._fieldSize / 2)
        x = starter + x * (self._frameWidth + self._fieldSize)
        y = starter + y * (self._frameWidth + self._fieldSize)

        pawn = self._canvas.create_oval(
            x-self._ballRadius,
            y-self._ballRadius,
            x+self._ballRadius,
            y+self._ballRadius,
            fill=color
        )

        return pawn

    def FieldsIntoPix(self, num):
        """change pixels into fields on a board"""
        num = num * (self._frameWidth + self._fieldSize)
        return num

    def Move(self, pawn):
        """move pawn on the window according to last and current position.
        Animate it by moving a self._step of pixels at a time and then waiting
        self.betweenStepsDelay amount of time"""
        x = (pawn.x - pawn.lastX)
        y = (pawn.y - pawn.lastY)

        gPawn = self._pawns[pawn]
        x = self.FieldsIntoPix(x)
        y = self.FieldsIntoPix(y)

        x0 = 0
        y0 = 0

        dirX = 0
        dirY = 0

        if (x0 > x):
            dirX -= 1
        elif (x0 < x):
            dirX += 1

        if (y0 > y):
            dirY -= 1
        elif (y0 < y):
            dirY += 1

        while (
            abs(abs(x0) - abs(x)) > abs(self._step) or
            abs(abs(y0) - abs(y)) > abs(self._step)
                ):
            x0 += dirX * self._step
            y0 += dirY * self._step

            time.sleep(self._betweenStepsDelay)
            self._canvas.move(gPawn, dirX*self._step, dirY*self._step)
            self.Update()

        self._canvas.move(
            gPawn, dirX*(abs(abs(x0) - abs(x))),
            dirY*(abs(abs(y0) - abs(y)))
            )

    def PrintMiddleText(self, message):
        """print an announcement on board"""
        text = self._canvas.create_text(
            self.size/2, self.size/2, text=message,
            fill=Colors.TEXT.value, font=(self._font))
        self.Update()
        time.sleep(1)
        self._canvas.delete(text)

    def OnClosing(self):
        self._window.destroy()

    def Update(self):
        self._window.update()
