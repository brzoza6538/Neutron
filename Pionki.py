from Window import Window


class Pawn:

    def __init__(self, Window: Window, x, y):
        """x, y według pól na planszy, nie piexeli"""
        self._X = x
        self._Y = y
        self._type = "random"
        self._color = "Green"

        self._Window = Window

    def update(self):
        self.move()

    def move(self):
        self._Window.move(self._pawn, 0, -1)
    # do rozłożenia później na oddzielne pliki


class AIPawn(Pawn):

    def __init__(self, Window: Window, x, y):
        super().__init__(Window, x, y)
        self._type = "AI"
        self._color = "Blue"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)


class RandomPawn(Pawn):

    def __init__(self, Window: Window, x, y):
        super().__init__(Window, x, y)
        self._type = "random"
        self._color = "Green"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)


class PlayerPawn(Pawn):

    def __init__(self, Window: Window, x, y):
        super().__init__(Window, x, y)
        self._type = "Player"
        self._color = "Red"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)


class NeutronPawn(Pawn):

    def __init__(self, Window: Window, x, y):
        super().__init__(Window, x, y)
        self._type = "Player"
        self._color = "Pink"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)
