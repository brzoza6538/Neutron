from enum import Enum


class Type(Enum):
    AI = "AI"
    PLAYER = "player"
    RANDOM = "random"
    NEUTRON = "neutron"


class Set(Enum):
    BOTTOM = "bottom"
    TOP = "top"
