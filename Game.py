import Pawns
import PlayablePlayer
import RandomPlayer
import time


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

        self._player = PlayablePlayer.PlayablePlayer(self._Window, self._Neutron, self._PlayerPawns, self._Board)
        self._randEnemy = RandomPlayer.RandomPlayer(self._Window, self._Neutron, self._EnemyPawns, self._Board)

    def checkIfEnd(self):
        if (self._Neutron._Y == 4 or self._Neutron._Y == 0):
            return True
        return False

    def WhoWon(self):
        if (self._Neutron._Y == 4):
            self._Window._Canvas.create_text(self._Window.size/2, self._Window.size/2, text="PRZEGRAŁEŚ", fill="Yellow", font=('Helvetica 25 bold'))
        elif (self._Neutron._Y == 0):
            self._Window._Canvas.create_text(self._Window.size/2, self._Window.size/2, text="WYGRAŁEŚ", fill="Yellow", font=('Helvetica 25 bold'))
        self._Window.Update()

    def Update(self):
        if not self.checkIfEnd():
            self._player.Update()

        if not self.checkIfEnd():
            if (self._player.isTurnFinished()):
                time.sleep(1)
                self._randEnemy.Update()
