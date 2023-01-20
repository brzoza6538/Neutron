from Window import Window
from Game import Game
from MainGui import MainGui


def Main():
    customData = MainGui()
    top = customData.topPlayerType
    bottom = customData.bottomPlayerType
    rowlen = customData.rowlen

    window = Window(rowlen)

    game = Game(rowlen, window, top, bottom)
    window.SetPawns(game.topPawns, game.neutron, game.bottomPawns)
    window.PrintMiddleText(f"{game.whoseTurn.value.upper()} STARTS")

    while True:
        window.Update()

        game.Update()

        if (game.movedPawn is not None):
            window.Move(game.movedPawn)

        if game.CheckIfEnd():
            winner = (game.WhoWon().set.value).upper()
            window.PrintMiddleText(f"{winner} WINS")
            window.OnClosing()
            break


if __name__ == '__main__':
    Main()
