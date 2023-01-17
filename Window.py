import tkinter
import time


class Window:

    def __init__(self, RowLen) -> None:
        # constants
        self._numOfSpaces = RowLen
        self._FrameWidth = 5
        self._FieldSize = 50
        self._WindowWidth = (
            (self._numOfSpaces*self._FieldSize) +
            (self._FrameWidth*(self._numOfSpaces+1))
            )
        self._WindowHeight = (
            (self._numOfSpaces*self._FieldSize) +
            (self._FrameWidth*(self._numOfSpaces+1))
            )

        self._BallRadius = int(self._FieldSize/2) - 6

        self.betweenStepsDelay = 0.01
        self._step = int(self._WindowWidth / 50)
        # Window
        self._Window = tkinter.Tk()
        self._Window.title("Neutron")
        self._Window.geometry(f'{self._WindowWidth}x{self._WindowHeight}')
        # canvas
        self._Canvas = tkinter.Canvas(self._Window)
        self._Canvas.configure(bg="Gray")
        self._Canvas.pack(fill="both", expand=True)
        # mouse
        self._Window.bind('<Motion>', self.MousePosition)
        self._Window.bind("<1>", self.Clicked)
        self._MouseX = 0
        self._MouseY = 0
        self._Clicked = False
        self._pawns = None
        self.SetFrame()

    @property
    def numOfSpaces(self):
        return self._numOfSpaces

    @property
    def size(self):
        return self._WindowWidth

    @property
    def MouseX(self):
        return self._MouseX

    @property
    def MouseY(self):
        return self._MouseY

    def MousePosition(self, e):
        self._MouseX = int(e.x / (self._FrameWidth + self._FieldSize + 1))
        self._MouseY = int(e.y / (self._FrameWidth + self._FieldSize + 1))

    def Clicked(self, e):
        self._Clicked = True

    def CheckClicked(self):
        if self._Clicked is True:
            self._Clicked = False
            return True
        else:
            return False

    def SetFrame(self):
        """split board into fields"""
        width = self._FrameWidth
        skip = self._FieldSize
        # X
        for line in range(self._numOfSpaces+1):
            self._Canvas.create_rectangle(
                (width+skip)*line, 0,
                (width+skip)*line + width, self._WindowHeight-1,
                fill='Black')
        # Y
        for line in range(self._numOfSpaces+1):
            self._Canvas.create_rectangle(
                0, (width+skip)*line,
                self._WindowWidth-1, (width+skip)*line + width,
                fill='Black')

    def SetPawns(self, TopPawns, neutron, BottomPawns):
        self._pawns = {}
        for pawn in TopPawns:
            self._pawns[pawn] = self.CreatePawn(pawn.color, pawn.X, pawn.Y)

        for pawn in BottomPawns:
            self._pawns[pawn] = self.CreatePawn(pawn.color, pawn.X, pawn.Y)

        self._pawns[neutron] = self.CreatePawn(
            neutron.color, neutron.X, neutron.Y)

    def ChangePawnColor(self, pawn, color):
        gPawn = self._pawns[pawn]
        self._Canvas.itemconfig(gPawn, fill=color)
        self.Update()

    def CreatePawn(self, color, x, y):
        starter = self._FrameWidth + int(self._FieldSize / 2)
        x = starter + x * (self._FrameWidth + self._FieldSize)
        y = starter + y * (self._FrameWidth + self._FieldSize)

        pawn = self._Canvas.create_oval(
            x-self._BallRadius,
            y-self._BallRadius,
            x+self._BallRadius,
            y+self._BallRadius,
            fill=color
        )

        return pawn

    def FieldsIntoPix(self, num):
        num = num * (self._FrameWidth + self._FieldSize)
        return num

    def Move(self, pawn):

        x = (pawn.X - pawn.lastX)
        y = (pawn.Y - pawn.lastY)

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

            time.sleep(self.betweenStepsDelay)
            self._Canvas.move(gPawn, dirX*self._step, dirY*self._step)
            self.Update()

        self._Canvas.move(
            gPawn, dirX*(abs(abs(x0) - abs(x))),
            dirY*(abs(abs(y0) - abs(y)))
            )

    def PrintMiddleText(self, message):
        text = self._Canvas.create_text(
            self.size/2, self.size/2, text=message,
            fill="Yellow", font=('Helvetica 25 bold'))
        self.Update()
        time.sleep(1)
        self._Canvas.delete(text)

    def OnClosing(self):
        self._Window.destroy()

    def Update(self):
        self._Window.update()
