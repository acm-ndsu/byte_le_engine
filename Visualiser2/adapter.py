import pygame


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
        self.populate_bytesprite.add()
        return self.populate_bytesprite.copy()

    def render(self): ...

    def clean_up(self): ...
