import pygame
from visualizer.bytesprites.exampleTileBS import ExampleTileBS
from visualizer.bytesprites.exampleWallBS import ExampleWallBS
from visualizer.bytesprites.exampleBS import ExampleBS
from visualizer.utils.sidebars import Sidebars

class Adapter:
    def __init__(self, screen):
        self.screen = screen
        self.bytesprites = []
        self.populate_bytesprite = pygame.sprite.Group()

    def on_event(self, event): ...

    def prerender(self): ...

    def continue_animation(self): ...

    def recalc_animation(self, turn_log: dict): ...

    def populate_bytesprites(self) -> pygame.sprite.Group:
        # Instantiate all bytesprites for each object ands add them here
        self.populate_bytesprite.add(ExampleTileBS(self.screen))
        self.populate_bytesprite.add(ExampleWallBS(self.screen))
        self.populate_bytesprite.add(ExampleBS(self.screen))
        return self.populate_bytesprite.copy()

    def render(self, sidebars: Sidebars):
        sidebars.left.fill('#FF7F00')
        sidebars.top.fill('#7FFF00')
        sidebars.bottom.fill('#00FF7F')
        sidebars.right.fill('#007FFF')

    def clean_up(self): ...
