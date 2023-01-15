class Pawn:

    def __init__(self, type, x, y):
        """x, y według pól na planszy, nie piexeli"""
        self._X = x
        self._Y = y
        self._type = type
        self._set = "Top"
        self._color = "Green"
        self._lastY = None
        self._lastX = None

    def Update(self):
        pass

    @property
    def set(self):
        return self._set

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


# class AIPawn(Pawn):

#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self._set = "AI"
#         self._color = "Blue"


# class RandomPawn(Pawn):

#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self._type = "Random"
#         self._color = "Green"


# class PlayerPawn(Pawn):

#     def __init__(self, x, y):
#         super().__init__(x, y)
#         self._type = "Player"
#         self._color = "Red"


class NeutronPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self._set = "Neutron"
        self._color = "#F7CFF6"


class TopPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self._set = "Top"
        self._color = self.SetpColor()

    def SetpColor(self):
        if (self.type == "AI"):
            return "#85C1E9"
        elif (self.type == "player"):
            return "#F1948A"
        else:
            return "#82E0AA"


class BottomPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self._set = "Bottom"
        self._color = self.SetpColor()

    def SetpColor(self):
        if (self.type == "AI"):
            return "#21618C"
        elif (self.type == "player"):
            return "#943126"
        else:
            return "#1D8348"
