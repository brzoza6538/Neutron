from Window import Window
from Game import Game
import time

window = Window()

game = Game(window, 1)

while True:
    window.Update()
    game.Update()
    if game.checkIfEnd():
        game.ShowWhoWon()
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
