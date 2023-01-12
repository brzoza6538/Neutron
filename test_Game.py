from Window import Window
from Game import Game
import Pawns
import RandomPlayer
import PlayablePlayer


def SetPawnsSurroundingNeutron(self):
    rowLen = self._Window.numOfSpaces

    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.RandomPawn(self._Window, x, 0))
        self._Board.setSpace(x, 0, self._EnemyPawns[x].type)

    for x in range(rowLen-1):
        self._PlayerPawns.append(
            Pawns.PlayerPawn(self._Window, x, 2))
        self._Board.setSpace(
            x, 2, self._PlayerPawns[x].type)

    self._PlayerPawns.append(
        Pawns.PlayerPawn(self._Window, 1, 1))
    self._Board.setSpace(
        1, 1, self._PlayerPawns[rowLen-1].type)

    self._Neutron = Pawns.NeutronPawn(self._Window, 0, 1)
    self._Board.setSpace(0, 1,  self._Neutron.type)


def test_surroundedNeutronILose(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)

    window = Window()

    game = Game(window, 1)

    game.Update()
    x = game.WhoWon()
    # assert game.checkIfEnd() is True
    assert isinstance(x, RandomPlayer.RandomPlayer)


def test_surroundedNeutronIWin(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsSurroundingNeutron)

    window = Window()

    game = Game(window, 1)
    game._whoseTurn = "enemy"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtEnemy(self):
    rowLen = self._Window.numOfSpaces
    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(self._Window, x, 1))
        self._Board.setSpace(x, 1, self._EnemyPawns[x].type)

    for x in range(rowLen):
        self._PlayerPawns.append(
            Pawns.PlayerPawn(self._Window, x, (rowLen - 1))
            )
        self._Board.setSpace(
            x, (rowLen - 1), self._PlayerPawns[x].type
            )
    middle = 0
    self._Neutron = Pawns.NeutronPawn(self._Window, middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.type)


def testNeutronAtEnemyPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)

    window = Window()

    game = Game(window, 1)
    game._whoseTurn = "player"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)
# Game.checkIfEnd()


def testNeutronAtEnemyEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtEnemy)

    window = Window()

    game = Game(window, 1)
    game._whoseTurn = "enemy"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, PlayablePlayer.PlayablePlayer)


def SetPawnsNeutronAtPlayer(self):
    rowLen = self._Window.numOfSpaces
    for x in range(rowLen):
        self._EnemyPawns.append(Pawns.AIPawn(self._Window, x, 1))
        self._Board.setSpace(x, 1, self._EnemyPawns[x].type)

    for x in range(rowLen):
        self._PlayerPawns.append(
            Pawns.PlayerPawn(self._Window, x, (rowLen - 1))
            )
        self._Board.setSpace(
            x, (rowLen - 1), self._PlayerPawns[x].type
            )
    middle = rowLen - 1
    self._Neutron = Pawns.NeutronPawn(self._Window, middle, middle)
    self._Board.setSpace(middle, middle,  self._Neutron.type)


def testNeutronAtPlayerPlayerTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    window = Window()

    game = Game(window, 1)
    game._whoseTurn = "player"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)
# Game.checkIfEnd()


def testNeutronAtPlayerEnemyTurn(monkeypatch):
    monkeypatch.setattr("Game.Game.SetPawns", SetPawnsNeutronAtPlayer)

    window = Window()

    game = Game(window, 1)
    game._whoseTurn = "enemy"

    game.Update()
    x = game.WhoWon()
    assert isinstance(x, RandomPlayer.RandomPlayer)

# @TODO zrób z 10 rand ruchów i później sprawdź czy plansza nadąża
