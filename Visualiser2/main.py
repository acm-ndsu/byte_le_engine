import sys

import pygame

from Visualiser2.adapter import Adapter
from Visualiser2.config import Config
from Visualiser2.utils.log_reader import logs_to_dict
from game.utils.vector import Vector


class ByteVisualiser:

    def __init__(self):
        pygame.init()
        self.config = Config()
        self.turn_logs: dict[str:dict] = {}
        self.size: Vector = self.config.SCREEN_SIZE
        # size = width, height = 1366, 768
        self.tile_size: int = self.config.TILE_SIZE

        self.screen = pygame.display.set_mode((self.size.x, self.size.y))
        self.adapter = Adapter(self.screen)

        self.clock = pygame.time.Clock()
        self.simple_font = pygame.font.Font(None, 50)

        self.tick: int = 0
        self.bytesprites = pygame.sprite.Group()

    def load(self):
        self.turn_logs = logs_to_dict()
        self.bytesprites = self.adapter.populate_bytesprites()

    def prerender(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.prerender()

    def render(self):
        if self.tick % self.config.NUMBER_OF_FRAMES_PER_TURN == 0:
            # NEXT TURN
            self.adapter.recalc_animation(
                self.turn_logs[f'turn_{self.tick // self.config.NUMBER_OF_FRAMES_PER_TURN + 1:04d}'])
        else:
            # NEXT ANIMATION FRAME
            self.adapter.continue_animation()

        self.adapter.render()
        pygame.display.flip()
        self.tick += 1

    def postrender(self):
        self.adapter.clean_up()
        self.clock.tick(self.config.FRAME_RATE)

    def loop(self):
        self.load()
        while True:
            # pygame events used to exit the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: sys.exit()

                self.adapter.on_event(event)

            self.prerender()
            self.render()
            self.postrender()


if __name__ == '__main__':
    byte_visualiser: ByteVisualiser = ByteVisualiser()
    byte_visualiser.loop()
