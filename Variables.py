from enum import Enum


class Type(Enum):
    """different types of players"""
    AI = "AI"
    PLAYER = "player"
    RANDOM = "random"


class Set(Enum):
    """data telling us where was a staring point for an object"""
    BOTTOM = "bottom"
    TOP = "top"
    NEUTRON = "neutron"


class Colors(Enum):
    """colors used in a game"""
    NEUTRON = "#F7CFF6"

    # playablePlayer
    CHOSEN = "Orange"
    SIGHT = "Red"

    # bottom pawns colors
    BAI = "#85C1E9"
    BPLAYER = "#F1948A"
    BRANDOM = "#82E0AA"

    # top pawns colors
    TAI = "#21618C"
    TPLAYER = "#943126"
    TRANDOM = "#1D8348"

    # Window
    BACKGROUND = "Grey"
    FRAME = "Black"
    TEXT = "Yellow"
