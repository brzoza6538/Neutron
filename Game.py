import Pawns
import Window
import Player


class Game:
    def __init__(self, Window: Window, type):

        # self._Board = [5][5]
        # for x in range(5):
        #     for y in range(5):
        #         self._Board[x][y] = None

        "choose opponent: 1 = AI, 0 = random"
        self._EnemyPawns = []
        self._PlayerPawns = []
        
        if (type == 1):
            for X in range(5):
                self._EnemyPawns.append(Pawns.AIPawn(Window, X, 0))
        else:
            for X in range(5):
                self._EnemyPawns.append(Pawns.RandomPawn(Window, X, 0))

        for X in range(5):
            self._PlayerPawns.append(Pawns.PlayerPawn(Window, X, 0))

        self._Neutron = Pawns.NeutronPawn(Window, 2, 2)

        self._Window = Window

    def Update(self):
        pass
