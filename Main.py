from Window import Window
from Game import Game
# import time

Window = Window()
Window.Render()

Game = Game(Window, 1)

Window.Render()
Window.SetFrame()

while True:
    Game.Update()

    Window.Update()
"""zrób 3 podklasy jednostek - sterowane przez ciebie, AI i randomowo"""
