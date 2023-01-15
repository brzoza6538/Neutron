from Window import Window
from Game import Game
import time

RowLen = 7  # num of tiles in a row - must be odd

window = Window(RowLen)

game = Game(RowLen, window, "AI", "AI")
window.SetPawns(game.TopPawns, game.Neutron, game.BottomPawns)

while True:
    window.Update()

    game.Update()

    if (game.movedPawn is not None):
        window.move(
            game.movedPawn, (game.movedPawn.X - game.movedPawn.lastX),
            (game.movedPawn.Y - game.movedPawn.lastY)
        )

    if game.checkIfEnd():
        winner = (game.WhoWon().loc).upper()
        window.PrintMiddleText(f"{winner} WINS")

        time.sleep(2)
        window.on_closing()
        break
