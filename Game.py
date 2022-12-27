import Pawns
import PlayablePlayer


class Game:
    def __init__(self, Window, type):
        "choose opponent: 1 = AI, 0 = random"

        self._Board = [[None for x in range(5)] for y in range(5)]
        self._EnemyPawns = []
        self._PlayerPawns = []

        if (type == 1):
            for x in range(5):
                self._EnemyPawns.append(Pawns.AIPawn(Window, x, 0))
                self._Board[x][0] = self._EnemyPawns[x].type
        else:
            for x in range(5):
                self._EnemyPawns.append(Pawns.RandomPawn(Window, x, 0))
                self._Board[x][0] = self._EnemyPawns[x].type

        for x in range(5):
            self._PlayerPawns.append(Pawns.PlayerPawn(Window, x, 4))
            self._Board[x][4] = self._PlayerPawns[x].type

        self._Neutron = Pawns.NeutronPawn(Window, 2, 2)
        self._Board[2][2] = self._Neutron.type

        self._Window = Window

        self._player1 = PlayablePlayer.PlayablePlayer(self._Window, self._Neutron, self._PlayerPawns, self._Board)

    def Update(self):
        self._player1.Update()
