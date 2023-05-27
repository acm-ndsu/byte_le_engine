import pygame as pyg
from game.utils.vector import Vector
from Visualiser2.config import Config


class ByteSprite(pyg.sprite.Sprite):
    active_sheet: list[pyg.Surface]  # The current spritesheet being used.
    spritesheets: list[list[pyg.Surface]]
    object_type: int
    layer: int
    position: Vector
    rect: pyg.Rect
    __frame_index: int  # Selects the sprite from the spritesheet to be used. Used for animation
    screen: pyg.Surface
    config: Config = Config()

    def __init__(self):
        # Add implementation here for selecting the sprite sheet to use
        super().__init__()
        pass

    def select_active_sheet(self, data: dict, layer: int, pos: Vector) -> None:
        self.__frame_index = 0  # Starts the new spritesheet at the beginning
        # Add implementation here for selecting the sprite sheet to use

    def render(self, layer: int):
        if layer is None or layer != self.layer:
            return

        # Places the given sprite at the rectangle's location
        self.screen.blit(self.active_sheet[self.__frame_index], self.rect)
        self.__frame_index = (self.__frame_index + 1) % self.config.NUMBER_OF_FRAMES_PER_TURN # selects the current sprite

