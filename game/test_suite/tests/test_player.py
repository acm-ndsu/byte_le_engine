import unittest
from game.common.player import Player
from game.common.game_object import GameObject
from game.common.avatar import Avatar
from game.common.enums import *


class TestPlayer(unittest.TestCase):

    def setUp(self) -> None:
        self.object_type: ObjectType = ObjectType.PLAYER
        self.functional: bool = True
        self.player: Player = Player
        self.
