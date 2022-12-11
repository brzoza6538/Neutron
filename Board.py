import tkinter
import time


class Board:

    def __init__(self) -> None:
        # constants
        self._FrameWidth = 10
        self._FieldSize = 50
        self._WindowWidth = ((5*self._FieldSize) + (self._FrameWidth*6))
        self._WindowHeight = ((5*self._FieldSize) + (self._FrameWidth*6))

        self._BallRadius = 15

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
        self._canvas = tkinter.Canvas(self._Window)
        self._canvas.configure(bg="Blue")
        self._canvas.pack(fill="both", expand=True)

    # def SetFrame(self):
    #     width = self._FrameWidth
    #     skip = self._FieldSize
    #     # X
    #     # for line in range(1):
    #     #     self._canvas.create_rectangle(0, 0, width, self._WindowHeight, fill='Black')

    def Animation(self):
        xInc = self._Speed
        yInc = self._Speed
        ball = self._canvas.create_oval(
            self._BallStartXPosition-self._BallRadius,
            self._BallStartYPosition-self._BallRadius,
            self._BallStartXPosition+self._BallRadius,
            self._BallStartYPosition+self._BallRadius,
            fill="Red", outline="", width=4)

        # while True:
        #     self._Window.update()


# warstwa 1
        while True:
            # self.SetFrame()
            self._canvas.move(
                ball, xInc, yInc
                )
            self._Window.update()
            time.sleep(self._RefreshFreq)
            ball_pos = self._canvas.coords(ball)
            # unpack array to variables
            al, bl, ar, br = ball_pos
            if al < abs(xInc) or ar > self._WindowWidth-abs(xInc):
                xInc = -xInc
            if bl < abs(yInc) or br > self._WindowHeight-abs(yInc):
                yInc = -yInc



    # def callback(e):
    #     x = e.x
    #     y = e.y
    #     print("Pointer is currently at %d, %d" % (x, y))

    # def on_main_click(e):
    #     print("sfffffffff")
