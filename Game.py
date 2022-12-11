import Pionki
import Window


class Game:
    def __init__(self, Window: Window, type):
        # "choose opponent: 1 = AI, 0 = random"
        if (type == 1):
            self._EnemyPawn1 = Pionki.AIPawn(Window, 0, 0)
            self._EnemyPawn2 = Pionki.AIPawn(Window, 1, 0)
            self._EnemyPawn3 = Pionki.AIPawn(Window, 2, 0)
            self._EnemyPawn4 = Pionki.AIPawn(Window, 3, 0)
            self._EnemyPawn5 = Pionki.AIPawn(Window, 4, 0)
        else:
            self._EnemyPawn1 = Pionki.RandomPawn(Window, 0, 0)
            self._EnemyPawn2 = Pionki.RandomPawn(Window, 1, 0)
            self._EnemyPawn3 = Pionki.RandomPawn(Window, 2, 0)
            self._EnemyPawn4 = Pionki.RandomPawn(Window, 3, 0)
            self._EnemyPawn5 = Pionki.RandomPawn(Window, 4, 0)

        self._PlayerPawn1 = Pionki.PlayerPawn(Window, 0, 4)
        self._PlayerPawn2 = Pionki.PlayerPawn(Window, 1, 4)
        self._PlayerPawn3 = Pionki.PlayerPawn(Window, 2, 4)
        self._PlayerPawn4 = Pionki.PlayerPawn(Window, 3, 4)
        self._PlayerPawn5 = Pionki.PlayerPawn(Window, 4, 4)

        self._Neutron = Pionki.NeutronPawn(Window, 2, 2)

        self._Window = Window

    # def Update(self):
        # self._PlayerPawn1.move()
        # self._PlayerPawn2.move()
        # self._PlayerPawn3.move()
        # self._PlayerPawn4.move()
        # self._PlayerPawn5.move()

    def Update(self):
        self._EnemyPawn1.update()
        self._EnemyPawn2.update()
        self._EnemyPawn3.update()
        self._EnemyPawn4.update()
        self._EnemyPawn5.update()

        self._PlayerPawn1.update()
        self._PlayerPawn2.update()
        self._PlayerPawn3.update()
        self._PlayerPawn4.update()
        self._PlayerPawn5.update()

        self._Neutron.update()
