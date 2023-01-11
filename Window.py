import tkinter
import time


class Window:

    def __init__(self) -> None:
        # constants
        self._numOfSpaces = 7  # musi być nieparzyste
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
        self.betweenStepsDelay = 0.02
        self._speed = 9
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

    def SetPawn(self, type, x, y):
        """what kind of pawn and where 0=ai, 1=random, 2=player, 3=neutron
        and where (x,y) for x,y e[0,5]"""
        starter = self._FrameWidth + int(self._FieldSize / 2)
        x = starter + x * (self._FrameWidth + self._FieldSize)
        y = starter + y * (self._FrameWidth + self._FieldSize)

        self._Canvas.create_oval(
            x-self._BallRadius,
            y-self._BallRadius,
            x+self._BallRadius,
            y+self._BallRadius,
            fill=type
        )

    def FieldsIntoPix(self, num):
        num = num * (self._FrameWidth + self._FieldSize)
        return num

    def move(self, pawn, x, y):
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
            abs(abs(x0) - abs(x)) > abs(self._speed) or
            abs(abs(y0) - abs(y)) > abs(self._speed)
                ):
            x0 += dirX * self._speed
            y0 += dirY * self._speed

            time.sleep(self.betweenStepsDelay)
            self._Canvas.move(pawn._pawn, dirX*self._speed, dirY*self._speed)
            self.Update()

        self._Canvas.move(
            pawn._pawn, dirX*(abs(abs(x0) - abs(x))),
            dirY*(abs(abs(y0) - abs(y)))
            )
        self.Update()

    def CreateBoard(self):
        Board = [
            [None for x in range(self.numOfSpaces)]
            for y in range(self.numOfSpaces)
            ]

        return Board

    def PrintMiddleText(self, message):
        self._Canvas.create_text(
            self.size/2, self.size/2, text=message,
            fill="Yellow", font=('Helvetica 25 bold'))

    def CreatePawn(self, type, x, y):
        starter = self._FrameWidth + int(self._FieldSize / 2)
        x = starter + x * (self._FrameWidth + self._FieldSize)
        y = starter + y * (self._FrameWidth + self._FieldSize)

        pawn = self._Canvas.create_oval(
            x-self._BallRadius,
            y-self._BallRadius,
            x+self._BallRadius,
            y+self._BallRadius,
            fill=type
        )

        return pawn

    def on_closing(self):
        self._Window.destroy()

    def Update(self):

        self._Window.update()
