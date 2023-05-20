import pygame, sys
from Visualiser2.config import Config
from game.utils.vector import Vector

pygame.init()

config = Config()

size: Vector = config.SCREEN_SIZE
# size = width, height = 1366, 768
tile_size: int = config.TILE_SIZE
black = 0, 0, 0

screen = pygame.display.set_mode((size.x, size.y))

clock = pygame.time.Clock()
simple_font = pygame.font.Font(None, 50)

tick: int = 0

turn_logs: list[dict]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE: sys.exit()

    # DO ACTIONS
    screen.fill(black)

    if(tick % config.NUMBER_OF_FRAMES_PER_TURN == 0):
        # NEXT TURN
        pass
    else:
        # NEXT ANIMATION FRAME
        pass

    tick += 1


    # Render Frame
    pygame.display.flip()
    clock.tick(config.FRAME_RATE)
