from Variables import Type, Set


class Pawn:

    def __init__(self, type, x, y):
        """x, y according to board, not pixels"""
        self._x = x
        self._y = y
        self._type = type
        self._set = None
        self._color = None
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
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def lastX(self):
        return self._lastX

    @property
    def lastY(self):
        return self._lastY

    def Move(self, x, y):
        """what field (x, y) move to"""
        self._lastX = self.x
        self._lastY = self.y
        self._x = x
        self._y = y


class NeutronPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self._set = Type.NEUTRON
        self._color = "#F7CFF6"


class TopPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self._set = Set.TOP
        self._color = self.SetpColor()

    def SetpColor(self):
        if (self.type == Type.AI):
            return "#85C1E9"
        elif (self.type == Type.PLAYER):
            return "#F1948A"
        else:
            return "#82E0AA"


class BottomPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(type, x, y)
        self._set = Set.BOTTOM
        self._color = self.SetpColor()

    def SetpColor(self):
        if (self.type == Type.AI):
            return "#21618C"
        elif (self.type == Type.PLAYER):
            return "#943126"
        else:
            return "#1D8348"
