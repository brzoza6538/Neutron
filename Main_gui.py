import tkinter as tk


class Main_gui():
    def __init__(self):
        self._root = tk.Tk()
        self._canvas = tk.Canvas(self._root, width=350, height=200)
        self._rowEntry = tk.Entry(self._root)
        self._topEntry = tk.Entry(self._root)
        self._bottomEntry = tk.Entry(self._root)

        self._RowLen = None
        self._TopPlayerType = None
        self._BottomPlayerType = None

        self._canvas.pack()
        self._canvas.create_window(175, 50, window=self._rowEntry)
        self._canvas.create_window(175, 100, window=self._topEntry)
        self._canvas.create_window(175, 150, window=self._bottomEntry)

        self.getData()
        self._root.mainloop()

    def checkData(self):
        # while True:
        RowLen = self._rowEntry.get()
        try:
            RowLen = int(RowLen)
            if (int(RowLen) < 20 and int(RowLen) > 2 and int(RowLen) % 2 == 1):
                self._RowLen = RowLen
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

        TopPlayerType = self._topEntry.get()
        if (
                isinstance(TopPlayerType, str) and
                (
                    TopPlayerType == "AI" or
                    TopPlayerType == "rand" or
                    TopPlayerType == "player"
                    )
                ):
            self._topMessage.destroy()
            self._TopPlayerType = TopPlayerType
            self._topMessage = tk.Label(text="thank you")
            self._topEntry.config(state="disabled")
            self._topLabel = self._canvas.create_window(
                175, 75, window=self._topMessage)
        else:
            self._topEntry.delete(0, 'end')
            self._topMessage.destroy()
            self._topMessage = tk.Label(
                text="please write 'AI', 'rand', or 'player'")

            self._topLabel = self._canvas.create_window(
                175, 75, window=self._topMessage)

        BottomPlayerType = self._bottomEntry.get()
        if (
                isinstance(BottomPlayerType, str) and
                (
                    BottomPlayerType == "AI" or
                    BottomPlayerType == "rand" or
                    BottomPlayerType == "player"
                    )
                ):
            self._BottomPlayerType = BottomPlayerType
            self._bottomMessage.destroy()
            self._bottomMessage = tk.Label(text="thank you")
            self._bottomEntry.config(state="disabled")
            self._bottomLabel = self._canvas.create_window(
                175, 125, window=self._bottomMessage)
        else:
            self._bottomEntry.delete(0, 'end')
            self._bottomMessage.destroy()
            self._bottomMessage = tk.Label(
                text="please write 'AI', 'rand', or 'player'")
            self._bottomLabel = self._canvas.create_window(
                175, 125, window=self._bottomMessage)

        if (
                self._RowLen is not None and
                self._BottomPlayerType is not None and
                self._TopPlayerType is not None
                ):
            self.on_closing()

    def getData(self):
        self._rowMessage = tk.Label(
            text="choose the size of the board (how many fields in a row):")
        self._rowLabel = self._canvas.create_window(
            175, 25, window=self._rowMessage)

        self._topMessage = tk.Label(
            text="choose top player type(write 'AI', 'rand', or 'player'):")
        self._topLabel = self._canvas.create_window(
            175, 75, window=self._topMessage)

        self._bottomMessage = tk.Label(
            text="choose bottom player type(write 'AI', 'rand', or 'player'):")
        self._bottomLabel = self._canvas.create_window(
            175, 125, window=self._bottomMessage)

        rowButton = tk.Button(text='Ok', command=self.checkData)
        self._canvas.create_window(175, 180, window=rowButton)

    def on_closing(self):
        self._root.destroy()

    def value(self):
        return (self._RowLen, self._TopPlayerType, self._BottomPlayerType)

    @property
    def RowLen(self):
        return self._RowLen

    @property
    def TopPlayerType(self):
        return self._TopPlayerType

    @property
    def BottomPlayerType(self):
        return self._BottomPlayerType
