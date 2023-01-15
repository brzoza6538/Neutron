from Window import Window
from Game import Game


def getPlayerTypes():
    print("choose player types(write 'AI', 'rand', or 'player'):")
    while True:
        top = input("Player type on the bottom of the board:")
        if (top == "AI" or top == "rand" or top == "player"):
            break

    while True:
        bottom = input("Player type on the top of the board:")
        if (bottom == "AI" or bottom == "rand" or bottom == "player"):
            break

    return top, bottom


def main():
    top, bottom = getPlayerTypes()

    RowLen = 7  # num of tiles in a row - must be odd

    window = Window(RowLen)

    game = Game(RowLen, window, top, bottom)
    window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)
    window.PrintMiddleText(f"{game._whoseTurn.upper()} STARTS")

    while True:
        window.Update()

        game.Update()

        if (game.movedPawn is not None):
            window.move(game.movedPawn)

        if game.checkIfEnd():
            winner = (game.WhoWon().loc).upper()
            window.PrintMiddleText(f"{winner} WINS")
            window.on_closing()
            break


if __name__ == "__main__":
    main()
