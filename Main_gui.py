import tkinter as tk
from Variables import Type


class Main_gui():
    def __init__(self):
        self._window = tk.Tk()
        self._canvas = tk.Canvas(self._window, width=350, height=200)
        self._rowEntry = tk.Entry(self._window)
        self._topEntry = tk.Entry(self._window)
        self._bottomEntry = tk.Entry(self._window)

        self._window.resizable(False, False)
        self._rowlen = None
        self._topPlayerType = None
        self._bottomPlayerType = None

        self._canvas.pack()
        self._canvas.create_window(175, 50, window=self._rowEntry)
        self._canvas.create_window(175, 100, window=self._topEntry)
        self._canvas.create_window(175, 150, window=self._bottomEntry)

        self.GetData()
        self._window.mainloop()
        self.PrepareData()

    def PrepareData(self):
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
        # while True:
        rowlen = self._rowEntry.get()
        try:
            rowlen = int(rowlen)
            if (int(rowlen) < 20 and int(rowlen) > 2 and int(rowlen) % 2 == 1):
                self._rowlen = rowlen
                self._rowMessage.destroy()
                self._rowMessage = tk.Label(text="thank you")
                self._rowEntry.config(state="disabled")
                self._rowLabel = self._canvas.create_window(
                    175, 25, window=self._rowMessage)
            else:
                self._rowEntry.delete(0, 'end')
                self._rowMessage.destroy()
                self._rowMessage = tk.Label(
                    text="""size must be an odd number, \
smaller than 20 and bigger than 2""")

                self._rowLabel = self._canvas.create_window(
                    175, 25, window=self._rowMessage)

        except ValueError:
            self._rowEntry.delete(0, 'end')
            self._rowMessage.destroy()
            self._rowMessage = tk.Label(
                text="""size must be an odd number, \
smaller than 20 and bigger than 2""")

            self._rowLabel = self._canvas.create_window(
                175, 25, window=self._rowMessage)

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
                175, 75, window=self._topMessage)
        else:
            self._topEntry.delete(0, 'end')
            self._topMessage.destroy()
            self._topMessage = tk.Label(
                text="please write 'AI', 'random', or 'player'")

            self._topLabel = self._canvas.create_window(
                175, 75, window=self._topMessage)

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
                175, 125, window=self._bottomMessage)
        else:
            self._bottomEntry.delete(0, 'end')
            self._bottomMessage.destroy()
            self._bottomMessage = tk.Label(
                text="please write 'AI', 'random', or 'player'")
            self._bottomLabel = self._canvas.create_window(
                175, 125, window=self._bottomMessage)

        if (
                self._rowlen is not None and
                self._bottomPlayerType is not None and
                self._topPlayerType is not None
                ):
            self.OnClosing()

    def GetData(self):
        self._rowMessage = tk.Label(
            text="choose the size of the board (how many fields in a row):")
        self._rowLabel = self._canvas.create_window(
            175, 25, window=self._rowMessage)

        self._topMessage = tk.Label(
            text="choose top player type(write 'AI', 'random', or 'player'):")
        self._topLabel = self._canvas.create_window(
            175, 75, window=self._topMessage)

        self._bottomMessage = tk.Label(
            text="choose bottom player type(write 'AI', 'random', or 'player'):")
        self._bottomLabel = self._canvas.create_window(
            175, 125, window=self._bottomMessage)

        rowButton = tk.Button(text='Ok', command=self.CheckData)
        self._canvas.create_window(175, 180, window=rowButton)

    def OnClosing(self):
        self._window.destroy()

    def Value(self):
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
