import Pawns
import Window


class Player:
    def __init__(self, Window: Window.Window, Neutron, Pawns, Board):
        """główna kalsa
        modyfikuje tablice, nie robi jej"""
        self._Window = Window
        self._Board = Board
        self._Pawns = Pawns
        self._Neutron = Neutron
        self._line = self._Window._Canvas.create_line(
            1, 1,
            1, 1,
            fill='Red',
            width=5
        )

    def Render(self):
        for pawn in range(5):
            self._Pawns[pawn].Update()

    def IsMovePossible(self, pawn: Pawns.Pawn, x, y):
        """sprawdza czy ruch możliwy"""
        XCheck = pawn._X
        YCheck = pawn._Y

        if ((XCheck + x > 4) or (YCheck + y > 4) or (XCheck + x < 0) or (YCheck + y < 0)):
            return False
        elif (self._Board[XCheck + x][YCheck + y] is not None):
            return False

        return True

    def MoveToWhere(self, pawn, x, y):
        """sprawdza zasieg ruchu"""
        XCheck = pawn._X
        YCheck = pawn._Y
        while True:
            if ((XCheck + x > 4) or (YCheck + y > 4) or (XCheck + x < 0) or (YCheck + y < 0)):
                break
            elif (self._Board[XCheck + x][YCheck + y] is not None):
                break

            XCheck += x
            YCheck += y
        return XCheck, YCheck

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
        self._Window._Canvas.delete(self._line)


        dirX = self._Window.MouseX - self._Neutron._X
        if dirX > 0:
            dirX = 1
        if dirX < 0:
            dirX = -1
        dirY = self._Window.MouseY - self._Neutron._Y
        if dirY > 0:
            dirY = 1
        if dirY < 0:
            dirY = -1
        # print(dirX, " ", dirY, "\n")
        x1 = self.MoveToWhere(self._Neutron, dirX, dirY)[0]
        y1 = self.MoveToWhere(self._Neutron, dirX, dirY)[1]

        self._line = self._Window._Canvas.create_line(
            self._Neutron.X * 55 + 27,
            self._Neutron.Y * 55 + 27,
            x1 * 55 + 27,
            y1 * 55 + 27,
            fill='Red',
            width=5
        )
        if (self._Window.CheckClicked() is True):
            if (self.IsMovePossible(self._Neutron, dirX, dirY)):
                self.move(self._Neutron, dirX, dirY)

            else:
                pass
            # zrób inny ruch
