class Pawn:

    def __init__(self, x, y):
        """x, y według pól na planszy, nie piexeli"""
        self._X = x
        self._Y = y
        self._type = "random"
        self._color = "Green"
        self._lastY = None
        self._lastX = None

    def Update(self):
        pass

    @property
    def type(self):
        return self._type

    @property
    def color(self):
        return self._color

    @property
    def X(self):
        return self._X

    @property
    def Y(self):
        return self._Y

    @property
    def lastX(self):
        return self._lastX

    @property
    def lastY(self):
        return self._lastY

    def move(self, x, y):
        """na jakie pole (x,y) poruszyć"""
        self._lastX = self.X
        self._lastY = self.Y
        self._X = x
        self._Y = y


class AIPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "AI"
        self._color = "Blue"


class RandomPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "Random"
        self._color = "Green"


class PlayerPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "Player"
        self._color = "Red"


class NeutronPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "Neutron"
        self._color = "Pink"


class TopPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "Top"
        self._color = "White"


class BottomPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "Bottom"
        self._color = "Black"
