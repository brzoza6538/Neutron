from Window import Window
from Game import Game
import Pawns
import RandomPlayer
import PlayablePlayer
import random
import math


"""test ending game conditions"""


def SetPawnsSurroundingNeutron(self):
    for x in range(self._RowLen):
        self._TopPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
        self._Board.setSpace(x, 0, self._TopPawns[x].set)

    for x in range(self._RowLen-1):
        self._BottomPawns.append(
            Pawns.BottomPawn(self._bottomPlayerType, x, 2))
        self._Board.setSpace(
            x, 2, self._BottomPawns[x].set)

    self._BottomPawns.append(
        Pawns.BottomPawn(self._bottomPlayerType, 1, 1))
    self._Board.setSpace(
        1, 1, self._BottomPawns[self._RowLen-1].set)

    self._Neutron = Pawns.NeutronPawn("Neutron", 0, 1)
    self._Board.setSpace(0, 1,  self._Neutron.set)


def testSurroundedNeutronPlayerLoses(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand", "player")
    game._whoseTurn = "bottom"
    window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)


def testSurroundedNeutronPlayerWins(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand", "player")
    game._whoseTurn = "top"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtEnemy(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._TopPawns.append(Pawns.TopPawn(self._topPlayerType, x, 1))
        self._Board.setSpace(x, 1, self._TopPawns[x].set)

    for x in range(rowLen):
        self._BottomPawns.append(
            Pawns.BottomPawn(self._bottomPlayerType, x, (rowLen - 1))
            )
        self._Board.setSpace(
            x, (rowLen - 1), self._BottomPawns[x].set
            )
    middle = 0
    self._Neutron = Pawns.NeutronPawn("Neutron", middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.set)


def testNeutronAtEnemyPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "AI", "player")
    game._whoseTurn = "bottom"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)
# Game.checkIfEnd()


def testNeutronAtEnemyEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "AI", "player")
    game._whoseTurn = "top"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtPlayer(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._TopPawns.append(Pawns.TopPawn(self._topPlayerType, x, 1))
        self._Board.setSpace(x, 1, self._TopPawns[x].set)

    for x in range(rowLen):
        self._BottomPawns.append(
            Pawns.BottomPawn(self._bottomPlayerType, x, (rowLen - 1))
            )
        self._Board.setSpace(
            x, (rowLen - 1), self._BottomPawns[x].set
            )
    middle = rowLen - 1
    self._Neutron = Pawns.NeutronPawn("Neutron", middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.set)


def testNeutronAtPlayerPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand", "player")
    game._whoseTurn = "bottom"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)
# Game.checkIfEnd()


def testNeutronAtPlayerEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand", "player")
    game._whoseTurn = "top"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)


"""board and pawn locations consistency"""


def usePawn(pawn, game):
    while True:
        if hasattr(pawn, "__len__"):
            usedPawn = pawn[random.randint(0,  (game.RowLen - 1))]
        else:
            usedPawn = pawn

        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (game._player1.IsMoveInDirPossible(
            usedPawn.X, usedPawn.Y, dirX, dirY
                )):
            game._player1._usedPawn = usedPawn
            game._player1.move(dirX, dirY)

            break


def testBoardPawnsConsistency():
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand", "player")
    window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)

    for i in range(25):
        usePawn(game._player1._Pawns, game)
        usePawn(game._player1._Neutron, game)

        usePawn(game._player2._Pawns, game)
        usePawn(game._player2._Neutron, game)

    playerPawnsCounter = 0
    randPawnsCounter = 0
    neutronCounter = 0
    EmptySpacesCounter = 0

    for row in game._Board._Board:
        for field in row:
            if (field == game._TopPawns[0].set):
                randPawnsCounter += 1
            elif (field == game._BottomPawns[0].set):
                playerPawnsCounter += 1
            elif (field == game.Neutron.set):
                neutronCounter += 1
            else:
                EmptySpacesCounter += 1

    var = (playerPawnsCounter == RowLen and
           randPawnsCounter == RowLen and
           neutronCounter == 1 and
           EmptySpacesCounter == ((RowLen - 2) * RowLen) - 1
           )
    assert var is True


def testPawnsBoardConsistency():
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand", "player")
    window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)

    for i in range(25):
        usePawn(game._player1._Pawns, game)
        usePawn(game._player1._Neutron, game)

        usePawn(game._player2._Pawns, game)
        usePawn(game._player2._Neutron, game)

    var = True
    board = game._Board._Board
    for pawn in game.TopPawns:
        if board[pawn.X][pawn.Y] != pawn.set:
            var = False

    for pawn in game.BottomPawns:
        if board[pawn.X][pawn.Y] != pawn.set:
            var = False

    pawn = game.Neutron
    if board[pawn.X][pawn.Y] != pawn.set:
        var = False

    assert var is True


"""AI looking for win in one """


def SetPawnsWithOneWinOption_01(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._TopPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
        self._Board.setSpace(x, 0, self._TopPawns[x].set)

    for x in range(rowLen):
        if (x != math.floor(self._RowLen/2)):
            self._BottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, x, (rowLen - 1))
                )
            self._Board.setSpace(
                x, (rowLen - 1), self._BottomPawns[x].set
                )
        else:
            self._BottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, 1, 1)
                )
            self._Board.setSpace(
                1, 1, self._BottomPawns[x].set
                )
    middle = math.floor(self._RowLen/2)
    self._Neutron = Pawns.NeutronPawn("Neutron", middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.set)


def testAIFindingWin_01(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption_01)
    var = True
    for i in range(20):
        RowLen = 7
        window = Window(RowLen)

        game = Game(RowLen, window, "AI", "player")
        window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)

        game._player1.Update()

        game._player1._usedPawn = game._Neutron
        game._player1.Brain()

        if (game._Neutron.Y != RowLen-1):
            var = False
            break

    assert var is True


def SetPawnsWithOneWinOption_11(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._TopPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
        self._Board.setSpace(x, 0, self._TopPawns[x].set)

    for x in range(rowLen):
        if (x != rowLen - 1):  #
            self._BottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, x, (rowLen - 1))
                )
            self._Board.setSpace(
                x, (rowLen - 1), self._BottomPawns[x].set
                )
        else:
            self._BottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, 1, 1)
                )
            self._Board.setSpace(
                1, 1, self._BottomPawns[x].set
                )
    middle = math.floor(self._RowLen/2)
    self._Neutron = Pawns.NeutronPawn("Neutron", middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.set)


def testAIFindingWin_11(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption_01)
    var = True
    for i in range(20):
        RowLen = 7
        window = Window(RowLen)

        game = Game(RowLen, window, "AI", "player")
        window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)

        game._player1.Update()

        game._player1._usedPawn = game._Neutron
        game._player1.Brain()

        if (game._Neutron.Y != RowLen-1):
            var = False
            break

    assert var is True


"""AI choosin not fatal move"""


def SetPawnsWithEnemyDefenseless(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._TopPawns.append(Pawns.TopPawn(
            self._topPlayerType, x, rowLen - 2))
        self._Board.setSpace(x, rowLen - 2, self._TopPawns[x].set)

    for x in range(rowLen):
        self._BottomPawns.append(Pawns.BottomPawn(
            self._bottomPlayerType, x, rowLen - 1))
        self._Board.setSpace(x, rowLen - 1, self._BottomPawns[x].set)

    middle = math.floor(self._RowLen/2)
    self._Neutron = Pawns.NeutronPawn("Neutron", middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.set)


def testNotLoosingAbility(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithEnemyDefenseless)
    var = True
    for i in range(20):
        RowLen = 7
        window = Window(RowLen)

        game = Game(RowLen, window, "AI", "player")
        window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)

        game._player1.Update()

        game._player1._usedPawn = game._Neutron
        game._player1.Brain()

        if (game._Neutron.Y == 0):
            var = False
            break

    assert var is True
