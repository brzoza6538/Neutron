from Window import Window
from Game import Game
from Main_gui import Main_gui


def Main():
    customData = Main_gui()
    Top = customData.TopPlayerType
    Bottom = customData.BottomPlayerType
    RowLen = customData.RowLen

    window = Window(RowLen)

    game = Game(RowLen, window, Top, Bottom)
    window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)
    window.PrintMiddleText(f"{game._whoseTurn.upper()} STARTS")

    while True:
        window.Update()

        game.Update()

        if (game.movedPawn is not None):
            window.Move(game.movedPawn)

        if game.CheckIfEnd():
            winner = (game.WhoWon().loc).upper()
            window.PrintMiddleText(f"{winner} WINS")
            window.OnClosing()
            break


if __name__ == '__main__':
    Main()
