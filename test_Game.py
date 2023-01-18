from Window import Window
from Game import Game
import Pawns
import RandomPlayer
import PlayablePlayer
import random
import math
from Variables import Type, Set


"""test ending game conditions"""


def SetPawnsSurroundingNeutron(self):
    for x in range(self._rowlen):
        self._topPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
        self._board.SetSpace(x, 0, self._topPawns[x].set)

    for x in range(self._rowlen-1):
        self._bottomPawns.append(
            Pawns.BottomPawn(self._bottomPlayerType, x, 2))
        self._board.SetSpace(
            x, 2, self._bottomPawns[x].set)

    self._bottomPawns.append(
        Pawns.BottomPawn(self._bottomPlayerType, 1, 1))
    self._board.SetSpace(
        1, 1, self._bottomPawns[self._rowlen-1].set)

    self._neutron = Pawns.NeutronPawn(Type.NEUTRON, 0, 1)
    self._board.SetSpace(0, 1,  self._neutron.set)


def testSurroundedNeutronBottomLoses(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)

    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.RANDOM)
    game._whoseTurn = Set.BOTTOM
    window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)


def testSurroundedNeutronBottomWins(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)
    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.PLAYER)
    game._whoseTurn = Set.TOP

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtEnemy(self):
    rowlen = self._rowlen
    for x in range(rowlen):
        self._topPawns.append(Pawns.TopPawn(self._topPlayerType, x, 1))
        self._board.SetSpace(x, 1, self._topPawns[x].set)

    for x in range(rowlen):
        self._bottomPawns.append(
            Pawns.BottomPawn(self._bottomPlayerType, x, (rowlen - 1))
            )
        self._board.SetSpace(
            x, (rowlen - 1), self._bottomPawns[x].set
            )
    middle = 0
    self._neutron = Pawns.NeutronPawn(Type.NEUTRON, middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testNeutronAtEnemyPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)
    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.AI, Type.PLAYER)
    game._whoseTurn = Set.BOTTOM

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)
# Game.CheckIfEnd()


def testNeutronAtEnemyEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)

    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.AI, Type.PLAYER)
    game._whoseTurn = Set.TOP

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtPlayer(self):
    rowlen = self._rowlen
    for x in range(rowlen):
        self._topPawns.append(Pawns.TopPawn(self._topPlayerType, x, 1))
        self._board.SetSpace(x, 1, self._topPawns[x].set)

    for x in range(rowlen):
        self._bottomPawns.append(
            Pawns.BottomPawn(self._bottomPlayerType, x, (rowlen - 1))
            )
        self._board.SetSpace(
            x, (rowlen - 1), self._bottomPawns[x].set
            )
    middle = rowlen - 1
    self._neutron = Pawns.NeutronPawn(Type.NEUTRON, middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testNeutronAtPlayerPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.PLAYER)
    game._whoseTurn = Set.BOTTOM

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)
# Game.CheckIfEnd()


def testNeutronAtPlayerEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.PLAYER)
    game._whoseTurn = Set.TOP

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)


"""board and pawn locations consistency"""


def usePawn(pawn, game):
    while True:
        if hasattr(pawn, "__len__"):
            usedPawn = pawn[random.randint(0,  (game.rowlen - 1))]
        else:
            usedPawn = pawn

        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (game.player1.IsMoveInDirPossible(
            usedPawn.x, usedPawn.y, dirX, dirY
                )):
            game._player1._usedPawn = usedPawn
            game.player1.Move(dirX, dirY)

            break


def testBoardPawnsConsistency():
    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.PLAYER)
    window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

    for i in range(25):
        usePawn(game.player1.pawns, game)
        usePawn(game.player1.neutron, game)

        usePawn(game.player2._pawns, game)
        usePawn(game.player2._neutron, game)

    playerPawnsCounter = 0
    randPawnsCounter = 0
    neutronCounter = 0
    EmptySpacesCounter = 0

    for row in game.board._board:
        for field in row:
            if (field == game.topPawns[0].set):
                randPawnsCounter += 1
            elif (field == game.bottomPawns[0].set):
                playerPawnsCounter += 1
            elif (field == game.neutron.set):
                neutronCounter += 1
            else:
                EmptySpacesCounter += 1

    var = (playerPawnsCounter == rowlen and
           randPawnsCounter == rowlen and
           neutronCounter == 1 and
           EmptySpacesCounter == ((rowlen - 2) * rowlen) - 1
           )
    assert var is True


def testPawnsBoardConsistency():
    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.PLAYER)
    window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

    for i in range(25):
        usePawn(game.player1.pawns, game)
        usePawn(game.player1.neutron, game)

        usePawn(game.player2.pawns, game)
        usePawn(game.player2.neutron, game)

    var = True
    board = game.board.board
    for pawn in game.topPawns:
        if board[pawn.x][pawn.y] != pawn.set:
            var = False

    for pawn in game.bottomPawns:
        if board[pawn.x][pawn.y] != pawn.set:
            var = False

    pawn = game.neutron
    if board[pawn.x][pawn.y] != pawn.set:
        var = False

    assert var is True


"""AI looking for win in one """


def SetPawnsWithOneWinOption_01(self):
    rowlen = self._rowlen
    for x in range(rowlen):
        self._topPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
        self._board.SetSpace(x, 0, self._topPawns[x].set)

    for x in range(rowlen):
        if (x != math.floor(self._rowlen/2)):
            self._bottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, x, (rowlen - 1))
                )
            self._board.SetSpace(
                x, (rowlen - 1), self._bottomPawns[x].set
                )
        else:
            self._bottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, 1, 1)
                )
            self._board.SetSpace(
                1, 1, self._bottomPawns[x].set
                )
    middle = math.floor(self._rowlen/2)
    self._neutron = Pawns.NeutronPawn(Type.NEUTRON, middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testAIFindingWin_01(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption_01)
    var = True
    for i in range(20):
        rowlen = 7
        window = Window(rowlen)

        game = Game(rowlen, window, Type.AI, Type.PLAYER)
        window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

        game.player1.Update()

        game._player1._usedPawn = game.neutron
        game.player1.Brain()

        if (game.neutron.y != rowlen-1):
            var = False
            break

    assert var is True


def SetPawnsWithOneWinOption_11(self):
    rowlen = self._rowlen
    for x in range(rowlen):
        self._topPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
        self._board.SetSpace(x, 0, self._topPawns[x].set)

    for x in range(rowlen):
        if (x != rowlen - 1):  #
            self._bottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, x, (rowlen - 1))
                )
            self._board.SetSpace(
                x, (rowlen - 1), self._bottomPawns[x].set
                )
        else:
            self._bottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, 1, 1)
                )
            self._board.SetSpace(
                1, 1, self._bottomPawns[x].set
                )
    middle = math.floor(self._rowlen/2)
    self._neutron = Pawns.NeutronPawn(Type.NEUTRON, middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testAIFindingWin_11(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption_01)
    var = True
    for i in range(20):
        rowlen = 7
        window = Window(rowlen)

        game = Game(rowlen, window, Type.AI, Type.PLAYER)
        window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

        game.player1.Update()

        game._player1._usedPawn = game.neutron
        game.player1.Brain()

        if (game.neutron.y != rowlen-1):
            var = False
            break

    assert var is True


"""AI choosin not fatal Move"""


def SetPawnsWithEnemyDefenseless(self):
    rowlen = self._rowlen
    for x in range(rowlen):
        self._topPawns.append(Pawns.TopPawn(
            self._topPlayerType, x, rowlen - 2))
        self._board.SetSpace(x, rowlen - 2, self._topPawns[x].set)

    for x in range(rowlen):
        self._bottomPawns.append(Pawns.BottomPawn(
            self._bottomPlayerType, x, rowlen - 1))
        self._board.SetSpace(x, rowlen - 1, self._bottomPawns[x].set)

    middle = math.floor(self._rowlen/2)
    self._neutron = Pawns.NeutronPawn(Type.NEUTRON, middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testNotLoosingAbility(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithEnemyDefenseless)
    var = True
    for i in range(20):
        rowlen = 7
        window = Window(rowlen)

        game = Game(rowlen, window, Type.AI, Type.PLAYER)
        window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

        game.player1.Update()

        game._player1._usedPawn = game.neutron
        game.player1.Brain()

        if (game.neutron.y == 0):
            var = False
            break

    assert var is True


"""AI have only an option that would make them lose"""


def SetPawnsAlmostSurroundingNeutron(self):
    for x in range(self._rowlen):
        self._topPawns.append(Pawns.TopPawn(self._topPlayerType, x, 0))
        self._board.SetSpace(x, 0, self._topPawns[x].set)

    for x in range(self._rowlen-1):
        if (x == 1):
            self._bottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, 5, 5))
            self._board.SetSpace(
                5, 5, self._bottomPawns[x].set)
        else:
            self._bottomPawns.append(
                Pawns.BottomPawn(self._bottomPlayerType, x, 2))
            self._board.SetSpace(
                x, 2, self._bottomPawns[x].set)

    self._bottomPawns.append(
        Pawns.BottomPawn(self._bottomPlayerType, 1, 1))
    self._board.SetSpace(
        1, 1, self._bottomPawns[self._rowlen-1].set)

    self._neutron = Pawns.NeutronPawn(Type.NEUTRON, 0, 1)
    self._board.SetSpace(0, 1,  self._neutron.set)


def testAIsuicide(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsAlmostSurroundingNeutron)

    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.AI, Type.AI)
    game._whoseTurn = Set.BOTTOM
    game._player2._pawnMoved = True
    window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

    while True:
        game.Update()

        if game.CheckIfEnd():
            winner = (game.WhoWon().set)
            window.OnClosing()
            break

    assert winner == Set.TOP
