import Pionki
import Window


class Game:
    def __init__(self, Window: Window, type):
        # "choose opponent: 1 = AI, 0 = random"
        if (type == 1):
            self._EnemyPawn1 = Pionki.AIPawn(0, 0)
            self._EnemyPawn2 = Pionki.AIPawn(1, 0)
            self._EnemyPawn3 = Pionki.AIPawn(2, 0)
            self._EnemyPawn4 = Pionki.AIPawn(3, 0)
            self._EnemyPawn5 = Pionki.AIPawn(4, 0)
        else:
            self._EnemyPawn1 = Pionki.RandomPawn(0, 0)
            self._EnemyPawn2 = Pionki.RandomPawn(1, 0)
            self._EnemyPawn3 = Pionki.RandomPawn(2, 0)
            self._EnemyPawn4 = Pionki.RandomPawn(3, 0)
            self._EnemyPawn5 = Pionki.RandomPawn(4, 0)

        self._PlayerPawn1 = Pionki.PlayerPawn(0, 4)
        self._PlayerPawn2 = Pionki.PlayerPawn(1, 4)
        self._PlayerPawn3 = Pionki.PlayerPawn(2, 4)
        self._PlayerPawn4 = Pionki.PlayerPawn(3, 4)
        self._PlayerPawn5 = Pionki.PlayerPawn(4, 4)

        self._Neutron = Pionki.NeutronPawn(2, 2)

        self._Window = Window

    def Render(self):
        col = self._EnemyPawn1._color
        self._Window.SetPawn(col, self._EnemyPawn1._X, self._EnemyPawn1._Y)
        self._Window.SetPawn(col, self._EnemyPawn2._X, self._EnemyPawn2._Y)
        self._Window.SetPawn(col, self._EnemyPawn3._X, self._EnemyPawn3._Y)
        self._Window.SetPawn(col, self._EnemyPawn4._X, self._EnemyPawn4._Y)
        self._Window.SetPawn(col, self._EnemyPawn5._X, self._EnemyPawn5._Y)

        col = self._PlayerPawn1._color
        self._Window.SetPawn(col, self._PlayerPawn1._X, self._PlayerPawn1._Y)
        self._Window.SetPawn(col, self._PlayerPawn2._X, self._PlayerPawn2._Y)
        self._Window.SetPawn(col, self._PlayerPawn3._X, self._PlayerPawn3._Y)
        self._Window.SetPawn(col, self._PlayerPawn4._X, self._PlayerPawn4._Y)
        self._Window.SetPawn(col, self._PlayerPawn5._X, self._PlayerPawn5._Y)

        col = self._Neutron._color
        self._Window.SetPawn(col, self._Neutron._X, self._Neutron._Y)
