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
        self._whoseTurn = "player"  # or enemy
        self._Window.SetFrame()
        self.SetPawns()
        self.SetPlayers()

    def SetPawns(self):
        rowLen = self._Window.numOfSpaces
        if (type == 1):
            for x in range(rowLen):
                self._EnemyPawns.append(Pawns.AIPawn(self._Window, x, 0))
                self._Board.setSpace(x, 0, self._EnemyPawns[x].type)
        else:
            for x in range(rowLen):
                self._EnemyPawns.append(Pawns.RandomPawn(self._Window, x, 0))
                self._Board.setSpace(x, 0, self._EnemyPawns[x].type)

        for x in range(rowLen):
            self._PlayerPawns.append(
                Pawns.PlayerPawn(self._Window, x, (rowLen - 1))
                )
            self._Board.setSpace(
                x, (rowLen - 1), self._PlayerPawns[x].type
                )

        middle = math.floor(rowLen/2)
        self._Neutron = Pawns.NeutronPawn(self._Window, middle, middle)
        self._Board.setSpace(middle, middle,  self._Neutron.type)

    def SetPlayers(self):
        self._player = PlayablePlayer.PlayablePlayer(
            self._Window, self._Neutron, self._PlayerPawns, self._Board
            )
        self._randEnemy = RandomPlayer.RandomPlayer(
            self._Window, self._Neutron, self._EnemyPawns, self._Board
            )

    def checkIfEnd(self):
        if (
            self._Neutron._Y == (self._Window.numOfSpaces - 1)
            or self._Neutron._Y == 0
                ):
            return True
        elif (
            self._player._immobileNeutron or self._randEnemy._immobileNeutron
                ):
            return True
        return False

    def WhoWon(self):
        if (
            self._Neutron._Y == (self._Window.numOfSpaces - 1)
            or self._player._immobileNeutron
                ):
            return self._randEnemy
        elif (self._Neutron._Y == 0 or self._randEnemy._immobileNeutron):
            return self._player

        self._Window.Update()

    def ShowWhoWon(self):
        if (
            self._Neutron._Y == (self._Window.numOfSpaces - 1)
            or self._player._immobileNeutron
                ):
            self._Window.PrintMiddleText("PRZEGRAŁEŚ")
        elif (self._Neutron._Y == 0 or self._randEnemy._immobileNeutron):
            self._Window.PrintMiddleText("WYGRAŁEś")

        self._Window.Update()

    def Update(self):
        if not self.checkIfEnd() and self._whoseTurn == "player":
            self._player.Update()
            if (self._player.isTurnFinished()):
                time.sleep(0.5)
                self._whoseTurn = "enemy"

        if not self.checkIfEnd() and self._whoseTurn == "enemy":
            self._randEnemy.Update()
            if (self._randEnemy.isTurnFinished()):
                self._whoseTurn = "player"
