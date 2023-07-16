import random

import pygame
from visualizer.bytesprites.exampleTileBS import ExampleTileBS
from visualizer.bytesprites.exampleWallBS import ExampleWallBS
from visualizer.bytesprites.exampleBS import ExampleBS
from game.utils.vector import Vector
from visualizer.utils.text import Text
from visualizer.utils.button import Button


class Adapter:
    def __init__(self, screen):
        self.screen = screen
        self.bytesprites = []
        self.populate_bytesprite = pygame.sprite.Group()
        self.text = Text(screen, 'Wow, text', 12)
        self.text2 = Text(self.screen, 'Wow, you clicked the button', 12, 'arial', '#950af2', Vector(100, 150))
        self.button = Button(self.screen, "Wow, button", 12, '#fff000', '#1ceb42', self.on_click())
        self.clicked = False

    def on_click(self) -> any:
        self.clicked = True

    def on_event(self, event):
        for self.event in pygame.event.get():
            self.button.mouse_clicked(event)

    def prerender(self):
        ...

    def continue_animation(self):
        ...

    def recalc_animation(self, turn_log: dict):
        ...

    def populate_bytesprites(self) -> pygame.sprite.Group:
        # Instantiate all bytesprites for each object ands add them here
        self.populate_bytesprite.add(ExampleTileBS(self.screen))
        self.populate_bytesprite.add(ExampleWallBS(self.screen))
        self.populate_bytesprite.add(ExampleBS(self.screen))
        return self.populate_bytesprite.copy()

    def render(self):
        if random.randint(0, 4) == 4:
            self.text.color = '#fff000'
        else:
            self.text.color = '#daa520'
        self.text.position = Vector(100 + random.randint(-25, 25), 50)

        self.button.position = Vector(100, 100)
        self.button.mouse_hover()

        self.text.render()
        if self.clicked:
            self.text2.render()

        self.button.render()

    def clean_up(self):
        ...
