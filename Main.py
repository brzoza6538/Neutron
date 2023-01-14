from Window import Window
from Game import Game
import time
from PlayablePlayer import PlayablePlayer

RowLen = 7  # num of tiles in a row - must be odd

window = Window(RowLen)

game = Game(RowLen, window, 1)
window.SetPawns(game.EnemyPawns, game.Neutron, game.PlayerPawns)

while True:
    window.Update()

    game.Update()

    if (game.movedPawn is not None):
        window.move(
            game.movedPawn, (game.movedPawn.X - game.movedPawn.lastX),
            (game.movedPawn.Y - game.movedPawn.lastY)
        )

    if game.checkIfEnd():
        if (isinstance(game.WhoWon(), PlayablePlayer)):
            window.PrintMiddleText("WYGRAŁEŚ")
        else:
            window.PrintMiddleText("PRZEGRAŁEŚ")

        time.sleep(2)
        window.on_closing()
        break


"""
The object of the game is to move the neutron into your home row, cause your
opponent to move the neutron into your home row, or to block the neutron
completely so your opponent can't move it.
w Game dorobić metode sprawdzającą czy neutron jest otoczony
i wywoływać w updacie gry kiedy updateowac window
"""
