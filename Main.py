from Window import Window
from Game import Game
import time

Window = Window()
Window.Render()

Game = Game(Window, 1)

Window.Render()
Window.SetFrame()

while True:
    print(Game._Board, "\n")
    Game.Update()
    print(Game._Board, "\n")

    Window.Update()
    time.sleep(1)
"""zrób 3 podklasy jednostek - sterowane przez ciebie, AI i randomowo"""
