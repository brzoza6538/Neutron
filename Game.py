import Pawns
import PlayablePlayer
import RandomPlayer
import time
import math
import Board


class Game:
    def __init__(self, RowLen, Window, type):

        self._RowLen = RowLen
        self._Board = Board.Board(self._RowLen)
        self._Window = Window
        self._EnemyPawns = []
        self._PlayerPawns = []
        self._winner = None
        self._whoseTurn = "player"  # or enemy
        self.SetPawns()
        self.SetPlayers()
        self._movedPawn = None

        self._timer = 0

    @property
    def movedPawn(self):
        return self._movedPawn

    @property
    def EnemyPawns(self):
        return self._EnemyPawns

    @property
    def PlayerPawns(self):
        return self._PlayerPawns

    @property
    def Neutron(self):
        return self._Neutron

    def SetPawns(self):
        if (type == 1):
            for x in range(self._RowLen):
                self._EnemyPawns.append(Pawns.AIPawn(x, 0))
                self._Board.setSpace(x, 0, self._EnemyPawns[x].color)
        else:
            for x in range(self._RowLen):
                self._EnemyPawns.append(Pawns.RandomPawn(x, 0))
                self._Board.setSpace(x, 0, self._EnemyPawns[x].color)

        for x in range(self._RowLen):
            self._PlayerPawns.append(
                Pawns.PlayerPawn(x, (self._RowLen - 1))
                )
            self._Board.setSpace(
                x, (self._RowLen - 1), self._PlayerPawns[x].color
                )

        middle = math.floor(self._RowLen/2)
        self._Neutron = Pawns.NeutronPawn(middle, middle)
        self._Board.setSpace(middle, middle,  self._Neutron.color)

    def SetPlayers(self):
        self._player = PlayablePlayer.PlayablePlayer(
            self._RowLen, self._Window, self._Neutron, self._PlayerPawns, self._Board
            )
        self._enemy = RandomPlayer.RandomPlayer(
            self._RowLen, self._Neutron, self._EnemyPawns, self._Board
            )

    def checkIfEnd(self):
        if (
            self._Neutron._Y == (self._RowLen - 1)
            or self._Neutron._Y == 0
                ):
            return True
        elif (
            self._player._immobileNeutron or self._enemy._immobileNeutron
                ):
            return True
        return False

    def WhoWon(self):
        if (
            self._Neutron._Y == (self._RowLen - 1)
            or self._player._immobileNeutron
                ):
            return self._enemy
        elif (self._Neutron._Y == 0 or self._enemy._immobileNeutron):
            return self._player

    def whatMoved(self):
        playerCheck = self._player.whatMoved()
        enemycheck = self._enemy.whatMoved()

        if (playerCheck is not None):
            self._movedPawn = playerCheck
        elif (enemycheck is not None):
            self._movedPawn = enemycheck
        else:
            self._movedPawn = None

    def Update(self):
        if not self.checkIfEnd() and self._whoseTurn == "player":
            self._player.Update()
            if (self._player.isTurnFinished()):
                self._whoseTurn = "enemy"

        elif not self.checkIfEnd() and self._whoseTurn == "enemy":
            self._enemy.Update()
            if (self._enemy.isTurnFinished()):
                self._whoseTurn = "player"

        self.whatMoved()
