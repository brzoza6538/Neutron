from Window import Window
from Game import Game

Window = Window()
Window.Render()

Game = Game(Window, 1)

Window.Render()

while True:
    Window.update()

"""zrób 3 podklasy jednostek - sterowane przez ciebie, AI i randomowo"""
