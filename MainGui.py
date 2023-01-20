import tkinter as tk
from Variables import Type


class MainGui():
    def __init__(self):
        self._window = tk.Tk()
        self._width = 380
        self._height = 200
        self._canvas = tk.Canvas(
            self._window, width=self._width, height=self._height)
        self._rowEntry = tk.Entry(self._window)
        self._topEntry = tk.Entry(self._window)
        self._bottomEntry = tk.Entry(self._window)

        self._window.resizable(False, False)
        self._rowlen = None
        self._topPlayerType = None
        self._bottomPlayerType = None

        self._canvas.pack()
        self._canvas.create_window(
            self._width/2, self._height/4, window=self._rowEntry)
        self._canvas.create_window(
            self._width/2, self._height/4*2, window=self._topEntry)
        self._canvas.create_window(
            self._width/2, self._height/4*3, window=self._bottomEntry)

        self.GetData()
        self._window.mainloop()
        self.PrepareData()

    def PrepareData(self):
        """change data from strings to Type's attributes"""
        if (self._bottomPlayerType == Type.AI.value):
            self._bottomPlayerType = Type.AI
        elif (self._bottomPlayerType == Type.PLAYER.value):
            self._bottomPlayerType = Type.PLAYER
        else:
            self._bottomPlayerType = Type.RANDOM

        if (self._topPlayerType == Type.AI.value):
            self._topPlayerType = Type.AI
        elif (self._topPlayerType == Type.PLAYER.value):
            self._topPlayerType = Type.PLAYER
        else:
            self._topPlayerType = Type.RANDOM

    def CheckData(self):
        """method activated when button pressed
        check if input data is correct"""
        self.CheckRowLen()
        self.CheckTopType()
        self.CheckBottomType()

        if (
                self._rowlen is not None and
                self._bottomPlayerType is not None and
                self._topPlayerType is not None
                ):
            self.OnClosing()

    def CheckRowLen(self):
        """check if given rowlen is correct and acts accordingly"""
        rowlen = self._rowEntry.get()
        try:
            rowlen = int(rowlen)
            if (int(rowlen) < 20 and int(rowlen) > 2 and int(rowlen) % 2 == 1):
                self._rowlen = rowlen
                self._rowMessage.destroy()
                self._rowMessage = tk.Label(text="thank you")
                self._rowEntry.config(state="disabled")
                self._rowLabel = self._canvas.create_window(
                    self._width/2, self._height/8, window=self._rowMessage)
            else:
                self._rowEntry.delete(0, 'end')
                self._rowMessage.destroy()
                self._rowMessage = tk.Label(
                    text="""size must be an odd number, \
smaller than 20 and bigger than 2""")

                self._rowLabel = self._canvas.create_window(
                    self._width/2, self._height/8, window=self._rowMessage)

        except ValueError:
            self._rowEntry.delete(0, 'end')
            self._rowMessage.destroy()
            self._rowMessage = tk.Label(
                text="""size must be an odd number, \
smaller than 20 and bigger than 2""")

            self._rowLabel = self._canvas.create_window(
                self._width/2, self._height/8, window=self._rowMessage)

    def CheckTopType(self):
        """checks if given top player type is correct and acts accordingly"""
        topPlayerType = self._topEntry.get()
        if (
                isinstance(topPlayerType, str) and
                (
                    topPlayerType == Type.AI.value or
                    topPlayerType == Type.RANDOM.value or
                    topPlayerType == Type.PLAYER.value
                    )
                ):
            self._topMessage.destroy()
            self._topPlayerType = topPlayerType
            self._topMessage = tk.Label(text="thank you")
            self._topEntry.config(state="disabled")
            self._topLabel = self._canvas.create_window(
                self._width/2, self._height/8*3, window=self._topMessage)
        else:
            self._topEntry.delete(0, 'end')
            self._topMessage.destroy()
            self._topMessage = tk.Label(
                text="please write 'AI', 'random', or 'player'")

            self._topLabel = self._canvas.create_window(
                self._width/2, self._height/8*3, window=self._topMessage)

    def CheckBottomType(self):
        """check if given bottom playerType is correct and acts accordingly"""
        bottomPlayerType = self._bottomEntry.get()
        if (
                isinstance(bottomPlayerType, str) and
                (
                    bottomPlayerType == Type.AI.value or
                    bottomPlayerType == Type.RANDOM.value or
                    bottomPlayerType == Type.PLAYER.value
                    )
                ):
            self._bottomPlayerType = bottomPlayerType
            self._bottomMessage.destroy()
            self._bottomMessage = tk.Label(text="thank you")
            self._bottomEntry.config(state="disabled")
            self._bottomLabel = self._canvas.create_window(
                self._width/2, self._height/8*5, window=self._bottomMessage)
        else:
            self._bottomEntry.delete(0, 'end')
            self._bottomMessage.destroy()
            self._bottomMessage = tk.Label(
                text="please write 'AI', 'random', or 'player'")
            self._bottomLabel = self._canvas.create_window(
                self._width/2, self._height/8*5, window=self._bottomMessage)

    def GetData(self):
        """prepare the window asking for data"""
        self._rowMessage = tk.Label(
            text="choose the size of the board (how many fields in a row):")
        self._rowLabel = self._canvas.create_window(
            self._width/2, self._height/8, window=self._rowMessage)

        self._topMessage = tk.Label(
            text="""choose player starting at the top type\
('AI', 'random', or 'player'):""")
        self._topLabel = self._canvas.create_window(
            self._width/2, self._height/8*3, window=self._topMessage)

        self._bottomMessage = tk.Label(
            text="choose player starting at the bottom type\
('AI', 'random', or 'player'):")
        self._bottomLabel = self._canvas.create_window(
            self._width/2, self._height/8*5, window=self._bottomMessage)

        rowButton = tk.Button(text='Ok', command=self.CheckData)
        self._canvas.create_window(
            self._width/2, self._height/8*7, window=rowButton)

    def OnClosing(self):
        self._window.destroy()

    def Value(self):
        """returns values gotten from the window"""
        return (self._rowlen, self._topPlayerType, self._bottomPlayerType)

    @property
    def rowlen(self):
        return self._rowlen

    @property
    def topPlayerType(self):
        return self._topPlayerType

    @property
    def bottomPlayerType(self):
        return self._bottomPlayerType
