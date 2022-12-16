import Pawns
import Window


class Player:
    def __init__(self, Window: Window, YourPawns, TheirPawns, ):
        """główna kalsa 
        modyfikuje tablice, nie robi jej"""
        self._Window = Window

    def Render(self):
        for pawn in range(5):
            self._pawns[pawn].update()

    def update(self):
        pawn