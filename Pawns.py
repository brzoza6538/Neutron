
class Pawn:

    def __init__(self, Window, x, y):
        """x, y według pól na planszy, nie piexeli"""
        self._X = x
        self._Y = y
        self._type = "random"
        self._color = "Green"

        self._Window = Window

    def Update(self):
        pass

    @property
    def type(self):
        return self._type

    @property
    def X(self):
        return self._X

    @property
    def Y(self):
        return self._Y

    def move(self, x, y):
        """na jakie pole (x,y) poruszyć"""
        self._Window.move(self._pawn, x - self._X, y - self._Y)
        self._X = x
        self._Y = y
    # do użycia gdzieś indziej


class AIPawn(Pawn):

    def __init__(self, Window, x, y):
        super().__init__(Window, x, y)
        self._type = "AI"
        self._color = "Blue"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)


class RandomPawn(Pawn):

    def __init__(self, Window, x, y):
        super().__init__(Window, x, y)
        self._type = "Random"
        self._color = "Green"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)


class PlayerPawn(Pawn):

    def __init__(self, Window, x, y):
        super().__init__(Window, x, y)
        self._type = "Player"
        self._color = "Red"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)


class NeutronPawn(Pawn):

    def __init__(self, Window, x, y):
        super().__init__(Window, x, y)
        self._type = "Neutron"
        self._color = "Pink"
        self._pawn = Window.CreatePawn(self._color, self._X, self._Y)
