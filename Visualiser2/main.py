import json
import pygame, sys
from Visualiser2.config import Config
from Visualiser2.bytesprite import ByteSprite
from game.utils.vector import Vector
from Visualiser2.utils.log_reader import logs_to_dict
from pathlib import Path


class ByteVisualiser:

    def __init__(self):
        pygame.init()
        self.config = Config()
        self.turn_logs: dict[str:dict] = {}
        self.size: Vector = self.config.SCREEN_SIZE
        # size = width, height = 1366, 768
        self.tile_size: int = self.config.TILE_SIZE

        self.screen = pygame.display.set_mode((self.size.x, self.size.y))

        self.clock = pygame.time.Clock()
        self.simple_font = pygame.font.Font(None, 50)

        self.tick: int = 0

    def load(self):
        self.turn_logs = logs_to_dict()

    def prerender(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        if self.tick % self.config.NUMBER_OF_FRAMES_PER_TURN == 0:
            # TODO: Make Connections to Adapter class to Trigger Methods to Populate Frame lists
            # NEXT TURN
            pass
        else:
            # NEXT ANIMATION FRAME
            pass
        self.tick += 1

    def render(self):
        pygame.display.flip()

    def postrender(self):
        self.clock.tick(self.config.FRAME_RATE)

    def loop(self):
        self.load()
        while True:
            # pygame events used to exit the loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT: sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE: sys.exit()
                # TODO: Add event method to adapter

            self.prerender()
            self.render()
            self.postrender()


if __name__ == '__main__':
    byte_visualiser: ByteVisualiser = ByteVisualiser()
    byte_visualiser.loop()
