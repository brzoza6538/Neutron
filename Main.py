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
