import tkinter


class Window:

    def __init__(self) -> None:
        # constants
        self._FrameWidth = 5
        self._FieldSize = 50
        self._WindowWidth = ((5*self._FieldSize) + (self._FrameWidth*6))
        self._WindowHeight = ((5*self._FieldSize) + (self._FrameWidth*6))

        self._BallRadius = int(self._FieldSize/2) - 6

        self._BallStartXPosition = self._BallRadius
        self._BallStartYPosition = self._BallRadius

        self._BallMinMovement = 5
        self._RefreshFreq = 0.01

        self._Speed = 3
        # Window
        self._Window = tkinter.Tk()
        self._Window.title("Python Guides")
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
    def MouseX(self):
        return self._MouseX

    @property
    def MouseY(self):
        return self._MouseY

    def MousePosition(self, e):
        self._MouseX = int(e.x / (self._FrameWidth + self._FieldSize + 1))
        self._MouseY = int(e.y / (self._FrameWidth + self._FieldSize + 1))
        # print("Pointer is currently at %d, %d" % (self._MouseX, self._MouseY))

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
        for line in range(6):
            self._Canvas.create_rectangle(
                (width+skip)*line, 0,
                (width+skip)*line + width, self._WindowHeight-1,
                fill='Black')
        # Y
        for line in range(6):
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
        self._Canvas.move(pawn, x, y)

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

    def Render(self):
        # tlo
        self.SetFrame()
        # jednostki

    def Update(self):
        self._Window.update()
        # self._Canvas.delete('all')

    # def callback(e):
    #     x = e.x
    #     y = e.y
    #     print("Pointer is currently at %d, %d" % (x, y))

    # def on_main_click(e):
    #     print("sfffffffff")
