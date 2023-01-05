import Window


class Player:
    def __init__(self, Window: Window, Neutron, Pawns, Board):
        self._Window = Window
        self._Board = Board
        self._Pawns = Pawns
        self._Neutron = Neutron

        self._usedPawn = None
        self._pawnMoved = False
        self._neutronMoved = False
        self._line = None

    def Render(self):
        for pawn in range(5):
            self._Pawns[pawn].Update()

    def IsMovePossible(self, pawn, x, y):
        """sprawdza czy ruch możliwy, ruch o 0 pól oznacza że niemożliwy"""
        XCheck = pawn._X
        YCheck = pawn._Y

        if ((XCheck + x > (self._Window.numOfSpaces - 1)) or (YCheck + y > (self._Window.numOfSpaces - 1)) or (XCheck + x < 0) or (YCheck + y < 0)):
            return False
        elif (self._Board.isFull(XCheck + x, YCheck + y)):
            return False
        return True

    def MoveToWhere(self, pawn, x, y):
        """sprawdza zasieg ruchu"""
        XCheck = pawn._X
        YCheck = pawn._Y
        while True:
            if ((XCheck + x > (self._Window.numOfSpaces - 1)) or (YCheck + y > (self._Window.numOfSpaces - 1)) or (XCheck + x < 0) or (YCheck + y < 0)):
                break
            elif (self._Board.isFull(XCheck + x, YCheck + y)):
                break
            # @TODO wstaw tam isMovePossible

            XCheck += x
            YCheck += y
        return XCheck, YCheck

    def move(self, pawn, x, y):
        """x, y przyjmuja wartość -1, 0, 1"""
        XCheck = pawn._X
        YCheck = pawn._Y
        while True:
            if ((XCheck + x > (self._Window.numOfSpaces - 1)) or (YCheck + y > (self._Window.numOfSpaces - 1)) or (XCheck + x < 0) or (YCheck + y < 0)):
                break
            elif (self._Board.isFull(XCheck + x, YCheck + y)):
                break
            # @TODO wstaw tam isMovePossible

            XCheck += x
            YCheck += y

        self._Board.clearSpace(pawn._X, pawn._Y)
        self._Board.setSpace(XCheck, YCheck, pawn.type)

        pawn.move(XCheck, YCheck)

    def Update(self):
        pass
        # self._Window.Update()
