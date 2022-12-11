import Pionki
import Window


class Game:
    def __init__(self, type, Window: Window):
        # "choose opponent: 1 = AI, 0 = random"
        if (type == 1):
            self._enemyPawn1 = Pionki.AIPawn(0, 0)
            self._enemyPawn2 = Pionki.AIPawn(1, 0)
            self._enemyPawn3 = Pionki.AIPawn(2, 0)
            self._enemyPawn4 = Pionki.AIPawn(3, 0)
            self._enemyPawn5 = Pionki.AIPawn(4, 0)
        else:
            self._enemyPawn1 = Pionki.RandomPawn(0, 0)
            self._enemyPawn2 = Pionki.RandomPawn(1, 0)
            self._enemyPawn3 = Pionki.RandomPawn(2, 0)
            self._enemyPawn4 = Pionki.RandomPawn(3, 0)
            self._enemyPawn5 = Pionki.RandomPawn(4, 0)

        self._PlayerPawn1 = Pionki.PlayerPawn(0, 4)
        self._PlayerPawn2 = Pionki.PlayerPawn(1, 4)
        self._PlayerPawn3 = Pionki.PlayerPawn(2, 4)
        self._PlayerPawn4 = Pionki.PlayerPawn(3, 4)
        self._PlayerPawn5 = Pionki.PlayerPawn(4, 4)

        self._Neutron = Pionki.NeutronPawn(2, 2)

        self._Window = Window

    def render(self):
        self._Window.SetPawn()
        
