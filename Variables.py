from enum import Enum


class Type(Enum):
    AI = "AI"
    PLAYER = "player"
    RANDOM = "random"


class Set(Enum):
    BOTTOM = "bottom"
    TOP = "top"
    NEUTRON = "neutron"


class Colors(Enum):

    NEUTRON = "#F7CFF6"

    # playablePlayer
    CHOSEN = "Orange"
    SIGHT = "Red"

    # top pawns colors
    TAI = "#85C1E9"
    TPLAYER = "#F1948A"
    TRANDOM = "#82E0AA"

    # bottom pawns colors
    BAI = "#21618C"
    BPLAYER = "#943126"
    BRANDOM = "#1D8348"

    # Window
    BACKGROUND = "Grey"
    FRAME = "Black"
    TEXT = "Yellow"
