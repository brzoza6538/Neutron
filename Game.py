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
        if (self._topPlayerType == "AI"):
            for x in range(self._RowLen):
                self._TopPawns.append(Pawns.AIPawn(x, 0))
                self._Board.setSpace(x, 0, self._TopPawns[x].type)
        elif (self._topPlayerType == "player"):
            for x in range(self._RowLen):
                self._TopPawns.append(Pawns.PlayerPawn(x, 0))
                self._Board.setSpace(x, 0, self._TopPawns[x].type)
        else:
            for x in range(self._RowLen):
                self._TopPawns.append(Pawns.RandomPawn(x, 0))
                self._Board.setSpace(x, 0, self._TopPawns[x].type)

        if (self._bottomPlayerType == "AI"):
            for x in range(self._RowLen):
                self._BottomPawns.append(Pawns.AIPawn(x, self._RowLen - 1))
                self._Board.setSpace(x, self._RowLen - 1, self._TopPawns[x].type)
        elif (self._bottomPlayerType == "player"):
            for x in range(self._RowLen):
                self._BottomPawns.append(Pawns.PlayerPawn(x, self._RowLen - 1))
                self._Board.setSpace(x, self._RowLen - 1, self._TopPawns[x].type)
        else:
            for x in range(self._RowLen):
                self._BottomPawns.append(Pawns.RandomPawn(x, self._RowLen - 1))
                self._Board.setSpace(x, self._RowLen - 1, self._TopPawns[x].type)

        middle = math.floor(self._RowLen/2)
        self._Neutron = Pawns.NeutronPawn(middle, middle)
        self._Board.setSpace(middle, middle,  self._Neutron.type)

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

    def checkIfEnd(self):
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

    def whatMoved(self):
        player2Check = self._player2.whatMoved()
        player1check = self._player1.whatMoved()

        if (player2Check is not None):
            self._movedPawn = player2Check
        elif (player1check is not None):
            self._movedPawn = player1check
        else:
            self._movedPawn = None

    def Update(self):
        if not self.checkIfEnd() and self._whoseTurn == "bottom":
            self._player2.Update()
            if (self._player2.isTurnFinished()):
                self._whoseTurn = "top"

        elif not self.checkIfEnd() and self._whoseTurn == "top":
            self._player1.Update()
            if (self._player1.isTurnFinished()):
                self._whoseTurn = "bottom"

        self.whatMoved()
