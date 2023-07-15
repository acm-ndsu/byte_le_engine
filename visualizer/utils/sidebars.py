import pygame as pyg
from visualizer.config import Config
from game.utils.vector import Vector


class Sidebars:

    def __init__(self):
        self.__config = Config()
        self.top = pyg.Surface(self.__config.SIDEBAR_TOP_DIMENSIONS.as_tuple())
        self.top_rect = self.top.get_rect()
        self.top_rect.midtop = Vector(x=self.__config.SCREEN_SIZE.x // 2,
                                      y=self.__config.SIDEBAR_TOP_PADDING).as_tuple()
        self.bottom = pyg.Surface(self.__config.SIDEBAR_BOTTOM_DIMENSIONS.as_tuple())
        self.bottom_rect = self.bottom.get_rect()
        self.bottom_rect.midbottom = Vector(x=self.__config.SCREEN_SIZE.x // 2,
                                            y=self.__config.SCREEN_SIZE.y - self.__config.SIDEBAR_BOTTOM_PADDING).as_tuple()  # handling the correct padding since it will be on the bottom
        self.left = pyg.Surface(self.__config.SIDEBAR_LEFT_DIMENSIONS.as_tuple())
        self.left_rect = self.left.get_rect()
        self.left_rect.midleft = Vector(x=self.__config.SIDEBAR_LEFT_PADDING,
                                        y=self.__config.SCREEN_SIZE.y // 2).as_tuple()
        self.right = pyg.Surface(self.__config.SIDEBAR_RIGHT_DIMENSIONS.as_tuple())
        self.right_rect = self.right.get_rect()
        self.right_rect.midright = Vector(x=self.__config.SCREEN_SIZE.x - self.__config.SIDEBAR_RIGHT_PADDING,
                                          y=self.__config.SCREEN_SIZE.y // 2).as_tuple()
