from Window import Window
from Game import Game
import Pawns
import RandomPlayer
import PlayablePlayer
import random


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

    game = Game(RowLen, window, 1)

    game.Update()
    x = game.WhoWon()
    # assert game.checkIfEnd() is True
    assert isinstance(x, RandomPlayer.RandomPlayer)


def testSurroundedNeutronPlayerWins(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, 1)
    game._whoseTurn = "enemy"

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

    game = Game(RowLen, window, 1)
    game._whoseTurn = "player"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)
# Game.checkIfEnd()


def testNeutronAtEnemyEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, 1)
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

    game = Game(RowLen, window, 1)
    game._whoseTurn = "player"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)
# Game.checkIfEnd()


def testNeutronAtPlayerEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, 1)
    game._whoseTurn = "enemy"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)

# @TODO zrób z 10 rand ruchów i później sprawdź czy plansza nadąża


def usePawn(pawn, game, window):
    while True:
        if hasattr(pawn, "__len__"):
            used_pawn = pawn[random.randint(0,  (game._enemy._RowLen - 1))]
        else:
            used_pawn = pawn

        dirX = random.randint(-1, 1)
        dirY = random.randint(-1, 1)

        if (game._enemy.IsMoveInDirPossible(used_pawn.X, used_pawn.Y, dirX, dirY)):

            game._enemy.move(used_pawn, dirX, dirY)
            break


def testBoardPawnsConsistency():
    # losujesz n ruchów
    # sprawdzasz lokalizacje pionków względem planszy
    # sprawdzas ile niepustych pól na planszy ile pionków jednego rodzaju ile drugiego

    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, 1)
    window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

    for i in range(25):
        usePawn(game._enemy._Pawns, game, window)
        usePawn(game._enemy._Neutron, game, window)

        usePawn(game._player._Pawns, game, window)
        usePawn(game._enemy._Neutron, game, window)

    playerPawnsCounter = 0
    enemyPawnsCounter = 0
    neutronCounter = 0
    EmptySpacesCounter = 0

    for row in game._Board._Board:
        for field in row:
            if (field == game._EnemyPawns[0].color):
                enemyPawnsCounter += 1
            elif (field == game._PlayerPawns[0].color):
                playerPawnsCounter += 1
            elif (field == game.Neutron.color):
                neutronCounter += 1
            else:
                EmptySpacesCounter += 1

    var = (playerPawnsCounter == RowLen and enemyPawnsCounter == RowLen and neutronCounter == 1 and EmptySpacesCounter == ((RowLen - 2) * RowLen) - 1)
    assert var is True


def testPawnsBoardConsistency():
    # jeden losowy pionek otocznony i ma sie ruszyc
    RowLen = 7
    window = Window(RowLen)

    game = Game(RowLen, window, 1)
    window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

    for i in range(25):
        usePawn(game._enemy._Pawns, game, window)
        usePawn(game._enemy._Neutron, game, window)

        usePawn(game._player._Pawns, game, window)
        usePawn(game._enemy._Neutron, game, window)

    var = True
    board = game._Board._Board
    for pawn in game.EnemyPawns:
        if board[pawn.X][pawn.Y] != pawn.color:
            var = False

    for pawn in game.PlayerPawns:
        if board[pawn.X][pawn.Y] != pawn.color:
            var = False

    pawn = game.Neutron
    if board[pawn.X][pawn.Y] != pawn.color:
        var = False

    assert var is True
