import Pawns
import PlayablePlayer
import RandomPlayer
import time
import math
import Board


class Game:
    def __init__(self, Window, type):
        "choose opponent: 1 = AI, 0 = random"

        self._Window = Window
        self._Board = Board.Board(Window)
        self._EnemyPawns = []
        self._PlayerPawns = []
        self._winner = None

        self._Window.SetFrame()

        if (type == 1):
            for x in range(self._Window.numOfSpaces):
                self._EnemyPawns.append(Pawns.AIPawn(Window, x, 0))
                self._Board.setSpace(x, 0, self._EnemyPawns[x].type)
        else:
            for x in range(self._Window.numOfSpaces):
                self._EnemyPawns.append(Pawns.RandomPawn(Window, x, 0))
                self._Board.setSpace(x, 0, self._EnemyPawns[x].type)

        for x in range(self._Window.numOfSpaces):
            # self._PlayerPawns.append(Pawns.PlayerPawn(Window, x, (2)))
            # self._Board.setSpace(x, 2, self._PlayerPawns[x].type)

            self._PlayerPawns.append(Pawns.PlayerPawn(Window, x, (self._Window.numOfSpaces - 1)))
            self._Board.setSpace(x, (self._Window.numOfSpaces - 1), self._PlayerPawns[x].type)

        middle = math.floor(self._Window.numOfSpaces/2)
        # self._Neutron = Pawns.NeutronPawn(Window, middle, 1)
        # self._Board.setSpace(middle, 1,  self._Neutron.type)
        self._Neutron = Pawns.NeutronPawn(Window, middle, middle)
        self._Board.setSpace(middle, middle,  self._Neutron.type)

        self._player = PlayablePlayer.PlayablePlayer(self._Window, self._Neutron, self._PlayerPawns, self._Board)
        self._randEnemy = RandomPlayer.RandomPlayer(self._Window, self._Neutron, self._EnemyPawns, self._Board)

    def checkIfEnd(self):
        if (self._Neutron._Y == (self._Window.numOfSpaces - 1) or self._Neutron._Y == 0):
            return True
        elif (self._player._immobileNeutron or self._randEnemy._immobileNeutron):
            return True
        return False

    def WhoWon(self):
        if (self._Neutron._Y == (self._Window.numOfSpaces - 1) or self._player._immobileNeutron):
            self._Window._Canvas.create_text(self._Window.size/2, self._Window.size/2, text="PRZEGRAŁEŚ", fill="Yellow", font=('Helvetica 25 bold'))
        elif (self._Neutron._Y == 0 or self._randEnemy._immobileNeutron):
            self._Window._Canvas.create_text(self._Window.size/2, self._Window.size/2, text="WYGRAŁEŚ", fill="Yellow", font=('Helvetica 25 bold'))

        self._Window.Update()

    def Update(self):
        if not self.checkIfEnd():
            self._player.Update()

        if not self.checkIfEnd():
            if (self._player.isTurnFinished()):
                time.sleep(0.5)
                self._randEnemy.Update()

        self._Window.Update()
