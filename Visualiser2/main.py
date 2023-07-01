import sys

import pygame

from Visualiser2.adapter import Adapter
from Visualiser2.bytesprites.bytesprite import ByteSprite
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
        self.bytesprite_templates = pygame.sprite.Group()
        self.bytesprite_map: [[[ByteSprite]]] = list()

    def load(self):
        self.turn_logs = logs_to_dict()
        self.bytesprite_templates = self.adapter.populate_bytesprites()

    def prerender(self):
        self.screen.fill(self.config.BACKGROUND_COLOR)
        self.prerender()

    def render(self):
        if self.tick % self.config.NUMBER_OF_FRAMES_PER_TURN == 0:
            # NEXT TURN
            self.recalc_animation(self.turn_logs[f'turn_{self.tick // self.config.NUMBER_OF_FRAMES_PER_TURN + 1:04d}'])
            self.adapter.recalc_animation(
                self.turn_logs[f'turn_{self.tick // self.config.NUMBER_OF_FRAMES_PER_TURN + 1:04d}'])
        else:
            # NEXT ANIMATION FRAME
            self.continue_animation()
            self.adapter.continue_animation()

        self.adapter.render()
        pygame.display.flip()
        self.tick += 1

    def recalc_animation(self, turn_data: dict) -> None:
        """
        Determine what bytesprites are needed at which location and calls logic to determine active spritesheet and render
        :param turn_data: A dictionary of all the turn data for current turn
        :return: None
        """
        game_map: [[dict]] = turn_data['game_board']['game_map']
        # Iterate on each row on the game map
        row: list
        for y, row in enumerate(game_map):
            # Add rows to bytesprite_map if needed
            if len(self.bytesprite_map) < y + 1:
                self.bytesprite_map.append(list())
            # Iterate on each tile in the row
            tile: dict
            for x, tile in enumerate(row):
                # Add tiles to row if needed
                if len(self.bytesprite_map[y]) < x + 1:
                    self.bytesprite_map[y].append(list())
                # Render layers on tile
                temp_tile: dict | None = tile
                z: int = 0
                while temp_tile is not None:
                    # Add layers if needed
                    if len(self.bytesprite_map[y][x]) < z + 1:
                        self.bytesprite_map[y][x].append(None)

                    # Create or replace bytesprite at current tile on this current layer
                    if self.bytesprite_map[y][x][z] is None or self.bytesprite_map[y][x][z].object_type != temp_tile[
                        'object_type']:
                        sprite_class: ByteSprite | None = next(t for t in self.bytesprite_templates.sprites() if
                                                               isinstance(t, ByteSprite) and t.object_type == temp_tile[
                                                                   'object_type'])
                        # Check that a bytesprite template exists for current object type
                        if sprite_class is None:
                            raise ValueError(
                                f'Must provide a bytesprite for each object type! Missing object_type: {temp_tile["object_type"]}')

                        # Instantiate a new bytesprite on current layer
                        self.bytesprite_map[y][x][z] = sprite_class.__class__(self.screen)

                    # Call render logic on bytesprite
                    self.bytesprite_map[y][x][z].update(temp_tile, z, Vector(y=y, x=x))
                    # increase iteration
                    temp_tile = temp_tile.get('occupied_by')
                    z += 1

                # clean up additional layers
                while len(self.bytesprite_map[y][x]) > z:
                    self.bytesprite_map[y][x].pop()

    def continue_animation(self) -> None:
        row: list
        tile: list
        sprite: ByteSprite
        [[[sprite.set_image_and_render() for sprite in tile] for tile in row] for row in self.bytesprite_map]

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
