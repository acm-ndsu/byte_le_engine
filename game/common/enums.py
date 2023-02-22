from enum import Enum


class DebugLevel(Enum):
    NONE = 0
    CLIENT = 1
    CONTROLLER = 2
    ENGINE = 3


class ObjectType(Enum):
    NONE = 4
    ACTION = 5
    PLAYER = 6


class ActionType(Enum):
    MOVE_UP = 7
    MOVE_DOWN = 8
    MOVE_LEFT = 9
    MOVE_RIGHT = 10
    INTERACT_UP = 11
    INTERACT_DOWN = 12
    INTERACT_LEFT = 13
    INTERACT_RIGHT = 14
    INTERACT_CENTER = 15
