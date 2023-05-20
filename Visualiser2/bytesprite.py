import pygame as pyg
from game.utils.vector import Vector


class ByteSprite:
    active_sheet: pyg.image
    spritesheets: list[pyg.image]
    object_type: int
    layer: int
    position: Vector

    def __init__(self):
        # Add implementation here for selecting the sprite sheet to use
        pass

    def select_active_sheet(self, data: dict, layer: int, pos: Vector) -> None:
        # Add implementation here for selecting the sprite sheet to use
        pass
