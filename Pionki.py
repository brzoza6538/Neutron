class Pawn:

    def __init__(self, x, y):
        """x, y według pól na planszy, nie piexeli"""
        self._X = x
        self._Y = y
        self._type = "random"

    # def move(self):


class AIPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "AI"
        self._color = "Blue"


class RandomPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "random"
        self._color = "Green"


class PlayerPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "Player"
        self._color = "Red"


class NeutronPawn(Pawn):

    def __init__(self, x, y):
        super().__init__(x, y)
        self._type = "Player"
        self._color = "Pink"
