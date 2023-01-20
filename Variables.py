from enum import Enum


class Type(Enum):
    AI = "AI"
    PLAYER = "player"
    RANDOM = "random"


class Set(Enum):
    BOTTOM = "bottom"
    TOP = "top"
    NEUTRON = "neutron"
