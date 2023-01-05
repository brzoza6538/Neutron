from Window import Window
from Game import Game
import time

Window = Window()
Window.Render()

Game = Game(Window, 1)

Window.Render()
Window.SetFrame()

while True:
    Game.Update()
    # Window.Update()
    if Game.checkIfEnd():
        Game.WhoWon()
        time.sleep(2)
        Window.on_closing()
        break
"""co jeśli wybrany randomowy pionek nie ma drogi ucieczki
The object of the game is to move the neutron into your home row, cause your opponent to move the neutron into your home row, or to block the neutron completely so your opponent can't move it.
linia trajektoria neutrona podawana w neutronie?
kiedy updateowac window"""
