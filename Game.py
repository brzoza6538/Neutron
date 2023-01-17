import Pawns
import PlayablePlayer
import RandomPlayer
import AIPlayer
import math
import Board


class Game:
    def __init__(self, RowLen, Window, topPlayerType, bottomPlayerType):
        """type - "AI" or "rand" or "player" """
        self._topPlayerType = topPlayerType
        self._bottomPlayerType = bottomPlayerType
        self._RowLen = RowLen
        self._Board = Board.Board(self._RowLen)
        self._Window = Window
        self._TopPawns = []
        self._BottomPawns = []
        self._winner = None
        self._whoseTurn = "bottom"  # or top
        self.SetPawns()
        self.SetPlayers()

        self._movedPawn = None

        self._timer = 0

    @property
    def RowLen(self):
        return self._RowLen

    @property
    def movedPawn(self):
        return self._movedPawn

    @property
    def TopPawns(self):
        return self._TopPawns

    @property
    def BottomPawns(self):
        return self._BottomPawns

    @property
    def Neutron(self):
        return self._Neutron

    def SetPawns(self):
        for x in range(self._RowLen):
            self._TopPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
            self._Board.SetSpace(x, 0, self._TopPawns[x].set)

        for x in range(self._RowLen):
            self._BottomPawns.append(Pawns.BottomPawn(
                self._bottomPlayerType, x, self._RowLen - 1))
            self._Board.SetSpace(x, self._RowLen - 1, self._BottomPawns[x].set)

        middle = math.floor(self._RowLen/2)
        self._Neutron = Pawns.NeutronPawn("Neutron", middle, middle)
        self._Board.SetSpace(middle, middle,  self._Neutron.set)

    def SetPlayers(self):

        if (self._topPlayerType == "player"):
            self._player1 = PlayablePlayer.PlayablePlayer(
                self._RowLen, self._Window, self._Neutron,
                self._TopPawns, self._Board, "top"
                )
        elif (self._topPlayerType == "AI"):
            self._player1 = AIPlayer.AIPlayer(
                self._RowLen, self._Neutron, self._TopPawns,
                self._Board, "top"
                )
        else:
            self._player1 = RandomPlayer.RandomPlayer(
                self._RowLen, self._Neutron, self._TopPawns,
                self._Board, "top"
                )

        if (self._bottomPlayerType == "player"):
            self._player2 = PlayablePlayer.PlayablePlayer(
                self._RowLen, self._Window, self._Neutron,
                self._BottomPawns, self._Board, "bottom"
                )
        elif (self._bottomPlayerType == "AI"):
            self._player2 = AIPlayer.AIPlayer(
                self._RowLen, self._Neutron, self._BottomPawns,
                self._Board, "bottom"
                )
        else:
            self._player2 = RandomPlayer.RandomPlayer(
                self._RowLen, self._Neutron, self._BottomPawns,
                self._Board, "bottom"
                )

    def CheckIfEnd(self):
        if (
            self._Neutron._Y == (self._RowLen - 1)
            or self._Neutron._Y == 0
                ):
            return True
        elif (
            self._player2._immobileNeutron or self._player1._immobileNeutron
                ):
            return True
        return False

    def WhoWon(self):
        if (
            self._Neutron._Y == (self._RowLen - 1)
            or self._player2._immobileNeutron
                ):
            return self._player1
        elif (self._Neutron._Y == 0 or self._player1._immobileNeutron):
            return self._player2

    def WhatMoved(self):
        player2Check = self._player2.WhatMoved()
        player1check = self._player1.WhatMoved()

        if (player2Check is not None):
            self._movedPawn = player2Check
        elif (player1check is not None):
            self._movedPawn = player1check
        else:
            self._movedPawn = None

    def Update(self):
        if not self.CheckIfEnd() and self._whoseTurn == "bottom":
            self._player2.Update()
            if (self._player2.IsTurnFinished()):
                self._whoseTurn = "top"

        elif not self.CheckIfEnd() and self._whoseTurn == "top":
            self._player1.Update()
            if (self._player1.IsTurnFinished()):
                self._whoseTurn = "bottom"

        self.WhatMoved()
