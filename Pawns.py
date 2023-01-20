from Variables import Type, Set, Colors


class Pawn:

    def __init__(self, x, y):
        """x, y according to board, not pixels"""
        self._x = x
        self._y = y
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

    def __init__(self, x, y):
        super().__init__(x, y)
        self._set = Set.NEUTRON
        self._color = Colors.NEUTRON.value


class TopPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(x, y)
        self._type = type
        self._set = Set.TOP
        self._color = self.SetColor()

    def SetColor(self):
        if (self.type == Type.AI):
            return Colors.TAI.value

        elif (self.type == Type.PLAYER):
            return Colors.TPLAYER.value

        return Colors.TRANDOM.value

    @property
    def type(self):
        return self._type


class BottomPawn(Pawn):

    def __init__(self, type, x, y):
        super().__init__(x, y)
        self._type = type
        self._set = Set.BOTTOM
        self._color = self.SetColor()

    def SetColor(self):
        if (self.type == Type.AI):
            return Colors.BAI.value

        elif (self.type == Type.PLAYER):
            return Colors.BPLAYER.value

        return Colors.BRANDOM.value

    @property
    def type(self):
        return self._type
