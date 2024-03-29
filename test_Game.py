from Window import Window
from Game import Game
import Pawns
import RandomPlayer
import PlayablePlayer
import math
from Variables import Type, Set


def SetPawnsSurroundingNeutron(self):
    """sets pawns surrounding the neutron"""
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

    self._neutron = Pawns.NeutronPawn(0, 1)
    self._board.SetSpace(0, 1,  self._neutron.set)


def testSurroundedNeutronBottomLoses(monkeypatch):
    """what happens when neutron can't move during bottom player's turn"""
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
    """what happens when neutron can't move during top player's turn"""
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)
    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.PLAYER)
    game._whoseTurn = Set.TOP

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtEnemy(self):
    """spawns netron in top player's row"""
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
    self._neutron = Pawns.NeutronPawn(middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testNeutronAtEnemyPlayerTurn(monkeypatch):
    """check how game goes when neutron is in top player's row
    during bottom player's turn """
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
    """check how game goes when neutron is in top player's row
    during top player's turn """
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)

    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.AI, Type.PLAYER)
    game._whoseTurn = Set.TOP

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtPlayer(self):
    """spawns netron in bottom player's row"""
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
    self._neutron = Pawns.NeutronPawn(middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testNeutronAtPlayerPlayerTurn(monkeypatch):
    """check how game goes when neutron is in bottom player's row
    during bottom player's turn """
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
    """check how game goes when neutron is in bottom player's row
    during top player's turn """
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.PLAYER)
    game._whoseTurn = Set.TOP

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)


def testBoardPawnsConsistency():
    """checks board after many moves if any pawn wasn't lost"""
    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.RANDOM)
    window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

    for i in range(25):
        game.player1.ChoosePawn()
        game.player1.RandomMove()
        game.player1._usedPawn = game.player1._neutron
        game.player1.RandomMove()

        game.player2.ChoosePawn()
        game.player2.RandomMove()
        game.player2._usedPawn = game.player2._neutron
        game.player2.RandomMove()

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
    """checks if location in pawns matches what is stored in board
    after many moves"""
    rowlen = 7
    window = Window(rowlen)

    game = Game(rowlen, window, Type.RANDOM, Type.RANDOM)
    window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

    for i in range(25):
        game.player1.ChoosePawn()
        game.player1.RandomMove()
        game.player1._usedPawn = game.player1._neutron
        game.player1.RandomMove()

        game.player2.ChoosePawn()
        game.player2.RandomMove()
        game.player2._usedPawn = game.player2._neutron
        game.player2.RandomMove()

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


def SetPawnsWithOneWinOption01(self):
    """set pawns where neutron can win in one move, moving downward"""
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
    self._neutron = Pawns.NeutronPawn(middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testAIFindingWin01(monkeypatch):
    """check if AI will win in one when neutron can move downward to win"""
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption01)
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


def SetPawnsWithOneWinOption11(self):
    """set pawns where neutron can win in one move, moving downward right"""
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
    self._neutron = Pawns.NeutronPawn(middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testAIFindingWin11(monkeypatch):
    """check if AI will win in one move when neutron
    can move downward right to win"""
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption01)
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


def SetPawnsWithEnemyDefenseless(self):
    """set pawns where top row is defenseless"""
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
    self._neutron = Pawns.NeutronPawn(middle, middle)
    self._board.SetSpace(middle, middle,  self._neutron.set)


def testNotLoosingAbility(monkeypatch):
    """will AI make moves that wouldn't make it lose"""
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


def SetPawnsAlmostSurroundingNeutron(self):
    """set pawns where the only move bottom player can make
     with neutron will make it lose"""
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

    self._neutron = Pawns.NeutronPawn(0, 1)
    self._board.SetSpace(0, 1,  self._neutron.set)


def testAIsuicide(monkeypatch):
    """AI have only an option that would make them lose.
    check if they choose it"""
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


"""play the game multiple times and check if everything works fine"""


def testStressTest():
    topCounter = 0
    bottomCounter = 0
    numOfGames = 100

    for i in range(numOfGames):
        rowlen = 7

        window = Window(rowlen)

        game = Game(rowlen, window, Type.AI, Type.AI)
        window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)

        while True:
            game.Update()

            if game.CheckIfEnd():
                winner = (game.WhoWon().set)
                if (winner == Set.TOP):
                    topCounter += 1
                elif (winner == Set.BOTTOM):
                    bottomCounter += 1

                break

    assert topCounter + bottomCounter == numOfGames
