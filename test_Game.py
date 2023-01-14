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
        self._EnemyPawns.append(Pawns.RandomPawn(x, 0))
        self._Board.setSpace(x, 0, self._EnemyPawns[x].type)

    for x in range(self._RowLen-1):
        self._PlayerPawns.append(
            Pawns.PlayerPawn(x, 2))
        self._Board.setSpace(
            x, 2, self._PlayerPawns[x].type)

    self._PlayerPawns.append(
        Pawns.PlayerPawn(1, 1))
    self._Board.setSpace(
        1, 1, self._PlayerPawns[self._RowLen-1].type)

    self._Neutron = Pawns.NeutronPawn(0, 1)
    self._Board.setSpace(0, 1,  self._Neutron.type)


def testSurroundedNeutronPlayerLoses(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand")
    game._whoseTurn = "bottom"
    window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)


def testSurroundedNeutronPlayerWins(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window,  "rand")
    game._whoseTurn = "top"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtEnemy(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(x, 1))
        self._Board.setSpace(x, 1, self._EnemyPawns[x].type)

    for x in range(rowLen):
        self._PlayerPawns.append(
            Pawns.PlayerPawn(x, (rowLen - 1))
            )
        self._Board.setSpace(
            x, (rowLen - 1), self._PlayerPawns[x].type
            )
    middle = 0
    self._Neutron = Pawns.NeutronPawn(middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.type)


def testNeutronAtEnemyPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand")
    game._whoseTurn = "player"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)
# Game.checkIfEnd()


def testNeutronAtEnemyEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand")
    game._whoseTurn = "enemy"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtPlayer(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(x, 1))
        self._Board.setSpace(x, 1, self._EnemyPawns[x].type)

    for x in range(rowLen):
        self._PlayerPawns.append(
            Pawns.PlayerPawn(x, (rowLen - 1))
            )
        self._Board.setSpace(
            x, (rowLen - 1), self._PlayerPawns[x].type
            )
    middle = rowLen - 1
    self._Neutron = Pawns.NeutronPawn(middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.type)


def testNeutronAtPlayerPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand")
    game._whoseTurn = "player"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)
# Game.checkIfEnd()


def testNeutronAtPlayerEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand")
    game._whoseTurn = "enemy"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)


"""board and pawn locations consistency"""


def usePawn(pawn, game):
    while True:
        if hasattr(pawn, "__len__"):
            used_pawn = pawn[random.randint(0,  (game._enemy._RowLen - 1))]
        else:
            used_pawn = pawn

        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (game._enemy.IsMoveInDirPossible(
                used_pawn.X, used_pawn.Y, dirX, dirY)):

            game._enemy._usedPawn = used_pawn
            game._enemy.move(dirX, dirY)
            break


def testBoardPawnsConsistency():
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand")
    window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

    for i in range(25):
        usePawn(game._enemy._Pawns, game)
        usePawn(game._enemy._Neutron, game)

        usePawn(game._player._Pawns, game)
        usePawn(game._enemy._Neutron, game)

    playerPawnsCounter = 0
    enemyPawnsCounter = 0
    neutronCounter = 0
    EmptySpacesCounter = 0

    for row in game._Board._Board:
        for field in row:
            if (field == game._EnemyPawns[0].type):
                enemyPawnsCounter += 1
            elif (field == game._PlayerPawns[0].type):
                playerPawnsCounter += 1
            elif (field == game.Neutron.type):
                neutronCounter += 1
            else:
                EmptySpacesCounter += 1

    var = (playerPawnsCounter == RowLen and
           enemyPawnsCounter == RowLen and
           neutronCounter == 1 and
           EmptySpacesCounter == ((RowLen - 2) * RowLen) - 1
           )

    assert var is True


def testPawnsBoardConsistency():
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, "rand")
    window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

    for i in range(25):
        usePawn(game._enemy._Pawns, game)
        usePawn(game._enemy._Neutron, game)

        usePawn(game._player._Pawns, game)
        usePawn(game._player._Neutron, game)

    var = True
    board = game._Board._Board
    for pawn in game.EnemyPawns:
        if board[pawn.X][pawn.Y] != pawn.type:
            var = False

    for pawn in game.PlayerPawns:
        if board[pawn.X][pawn.Y] != pawn.type:
            var = False

    pawn = game.Neutron
    if board[pawn.X][pawn.Y] != pawn.type:
        var = False

    assert var is True


"""AI looking for win in one """


def SetPawnsWithOneWinOption_01(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(x, 0))
        self._Board.setSpace(x, 0, self._EnemyPawns[x].type)

    for x in range(rowLen):
        if (x != math.floor(self._RowLen/2)):
            self._PlayerPawns.append(
                Pawns.PlayerPawn(x, (rowLen - 1))
                )
            self._Board.setSpace(
                x, (rowLen - 1), self._PlayerPawns[x].type
                )
        else:
            self._PlayerPawns.append(
                Pawns.PlayerPawn(1, 1)
                )
            self._Board.setSpace(
                1, 1, self._PlayerPawns[x].type
                )
    middle = math.floor(self._RowLen/2)
    self._Neutron = Pawns.NeutronPawn(middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.type)


def testAIFindingWin_01(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption_01)
    var = True
    for i in range(20):
        RowLen = 7
        window = Window(RowLen)

        game = Game(RowLen, window, "AI")
        window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

        game._enemy.Update()

        game._enemy._usedPawn = game._Neutron
        game._enemy.Brain()

        if (game._Neutron.Y != RowLen-1):
            var = False
            break

    assert var is True


def SetPawnsWithOneWinOption_11(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(x, 0))
        self._Board.setSpace(x, 0, self._EnemyPawns[x].type)

    for x in range(rowLen):
        if (x != rowLen - 1):  #
            self._PlayerPawns.append(
                Pawns.PlayerPawn(x, (rowLen - 1))
                )
            self._Board.setSpace(
                x, (rowLen - 1), self._PlayerPawns[x].type
                )
        else:
            self._PlayerPawns.append(
                Pawns.PlayerPawn(1, 1)
                )
            self._Board.setSpace(
                1, 1, self._PlayerPawns[x].type
                )
    middle = math.floor(self._RowLen/2)
    self._Neutron = Pawns.NeutronPawn(middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.type)


def testAIFindingWin_11(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithOneWinOption_01)
    var = True
    for i in range(20):
        RowLen = 7
        window = Window(RowLen)

        game = Game(RowLen, window, "AI")
        window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

        game._enemy.Update()

        game._enemy._usedPawn = game._Neutron
        game._enemy.Brain()

        if (game._Neutron.Y != RowLen-1):
            var = False
            break

    assert var is True


"""AI choosin not fatal move"""


def SetPawnsWithEnemyDefenseless(self):
    rowLen = self._RowLen
    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(x, rowLen - 2))
        self._Board.setSpace(x, rowLen - 2, self._EnemyPawns[x].type)

    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(x, rowLen - 1))
        self._Board.setSpace(x, rowLen - 1, self._EnemyPawns[x].type)

    middle = math.floor(self._RowLen/2)
    self._Neutron = Pawns.NeutronPawn(middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.type)


def testNotLoosingAbility(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsWithEnemyDefenseless)
    var = True
    for i in range(20):
        RowLen = 7
        window = Window(RowLen)

        game = Game(RowLen, window, "AI")
        window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

        game._enemy.Update()

        game._enemy._usedPawn = game._Neutron
        game._enemy.Brain()

        if (game._Neutron.Y == 0):
            var = False
            break

    assert var is True
