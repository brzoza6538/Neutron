import Pawns
import Window


class Player:
    def __init__(self, Window: Window, Neutron, Pawns, Board):
        """główna kalsa 
        modyfikuje tablice, nie robi jej"""
        self._Window = Window
        self._Board = Board
        self._Pawns = Pawns
        self._Neutron = Neutron

    def Render(self):
        for pawn in range(5):
            self._Pawns[pawn].Update()

    def move(self, pawn: Pawns.Pawn, x, y):
        """x, y przyjmuja wartość -1, 0, 1"""
        XCheck = pawn._X
        YCheck = pawn._Y
        while True:
            if ((XCheck + x > 4) or (YCheck + y > 4) or (XCheck + x < 0) or (YCheck + y < 0)):
                break
            elif (self._Board[XCheck + x][YCheck + y] is not None):
                break

            XCheck += x
            YCheck += y

        self._Board[pawn._X][pawn._Y] = None
        self._Board[XCheck][YCheck] = pawn.type

        pawn.move(XCheck, YCheck)

    def Update(self):
        self.move(self._Neutron, -1, 0)
