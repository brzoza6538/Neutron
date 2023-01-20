import Pawns
from PlayablePlayer import PlayablePlayer
from RandomPlayer import RandomPlayer
from AIPlayer import AIPlayer
import math
from Board import Board
from Variables import Type, Set


class Game:
    def __init__(self, rowlen, window, topPlayerType, bottomPlayerType):
        self._topPlayerType = topPlayerType
        self._bottomPlayerType = bottomPlayerType
        self._rowlen = rowlen
        self._board = Board(self._rowlen)
        self._window = window
        self._topPawns = []
        self._bottomPawns = []
        self._winner = None
        self._whoseTurn = Set.BOTTOM  # or top
        self.SetPawns()
        self.SetPlayers()

        self._movedPawn = None

        self._timer = 0

    @property
    def board(self):
        return self._board

    @property
    def whoseTurn(self):
        return self._whoseTurn

    @property
    def rowlen(self):
        return self._rowlen

    @property
    def movedPawn(self):
        return self._movedPawn

    @property
    def topPawns(self):
        return self._topPawns

    @property
    def bottomPawns(self):
        return self._bottomPawns

    @property
    def neutron(self):
        return self._neutron

    @property
    def player1(self):
        return self._player1

    @property
    def player2(self):
        return self._player2

    def SetPawns(self):
        for x in range(self._rowlen):
            self._topPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
            self._board.SetSpace(x, 0, self._topPawns[x].set)

        for x in range(self._rowlen):
            self._bottomPawns.append(Pawns.BottomPawn(
                self._bottomPlayerType, x, self._rowlen - 1))
            self._board.SetSpace(x, self._rowlen - 1, self._bottomPawns[x].set)

        middle = math.floor(self._rowlen/2)
        self._neutron = Pawns.NeutronPawn(middle, middle)
        self._board.SetSpace(middle, middle,  self._neutron.set)

    def SetPlayers(self):

        if (self._topPlayerType == Type.PLAYER):
            self._player1 = PlayablePlayer(
                self._rowlen, self._window, self._neutron,
                self._topPawns, self._board, Set.TOP
                )
        elif (self._topPlayerType == Type.AI):
            self._player1 = AIPlayer(
                self._rowlen, self._neutron, self._topPawns,
                self._board, Set.TOP
                )
        else:
            self._player1 = RandomPlayer(
                self._rowlen, self._neutron, self._topPawns,
                self._board, Set.TOP
                )

        if (self._bottomPlayerType == Type.PLAYER):
            self._player2 = PlayablePlayer(
                self._rowlen, self._window, self._neutron,
                self._bottomPawns, self._board, Set.BOTTOM
                )
        elif (self._bottomPlayerType == Type.AI):
            self._player2 = AIPlayer(
                self._rowlen, self._neutron, self._bottomPawns,
                self._board, Set.BOTTOM
                )
        else:
            self._player2 = RandomPlayer(
                self._rowlen, self._neutron, self._bottomPawns,
                self._board, Set.BOTTOM
                )

    def CheckIfEnd(self):
        if (
            self._neutron.y == (self._rowlen - 1)
            or self._neutron.y == 0
                ):
            return True
        elif (
            self._player2.immobileNeutron or self._player1.immobileNeutron
                ):
            return True
        return False

    def WhoWon(self):
        if (
            self._neutron.y == (self._rowlen - 1)
            or self._player2.immobileNeutron
                ):
            return self._player1
        elif (self._neutron.y == 0 or self._player1.immobileNeutron):
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
        if not self.CheckIfEnd() and self._whoseTurn == Set.BOTTOM:
            self._player2.Update()
            if (self._player2.IsTurnFinished()):
                self._whoseTurn = Set.TOP

        elif not self.CheckIfEnd() and self._whoseTurn == Set.TOP:
            self._player1.Update()
            if (self._player1.IsTurnFinished()):
                self._whoseTurn = Set.BOTTOM

        self.WhatMoved()
