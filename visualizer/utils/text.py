import pygame
from game.utils.vector import Vector
from typing import Optional

"""
class that creates text to be displayed in the visualizer within a rectangle

defaults used unless otherwise stated:
font: Bauhaus93
color: #daa520          (yellowish)
position: Vector(0, 0)  (representing pixels on screen, top left pixel)
"""


class Text:
    def __init__(self, screen: pygame.Surface, text: str, font_size: int, font_name: str = 'bauhaus93', color: str | int | tuple[int, int, int, Optional[int]] | list[int, int, int, Optional[int]] | pygame.Color = pygame.Color('#daa520'), position: Vector = Vector(0, 0)):
        self.screen: pygame.Surface = screen  # assign screen used
        self.text: str = text  # assign text used
        self.font_size: int = font_size  # assign font size used
        self.font_name: str = font_name  # name of font used
        self.color: str | int | tuple[int, int, int, Optional[int]] | list[int, int, int, Optional[int]] | pygame.Color = color  # assign color used
        self.position: Vector = position  # assign position used
        self.__font: pygame.font.Font = pygame.font.SysFont(self.font_name, self.font_size)  # get font from list of
        # SysFont, adjust size
        self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)  # render text with color
        self.__rect: pygame.Rect = self.__text_surface.get_rect()  # get rectangle used
        self.__rect.topleft: tuple[int, int] = self.position.as_tuple()  # set top left position of rect to position

    # render text and rectangle to screen
    def render(self) -> None:
        self.screen.blit(self.__text_surface, self.__rect)

    # getter methods
    @property
    def screen(self) -> pygame.Surface:
        return self.__screen

    @property
    def text(self) -> str:
        return self.__text

    @property
    def font_name(self) -> str:
        return self.__font_name

    @property
    def font_size(self) -> int:
        return self.__font_size

    @property
    def color(self) -> pygame.Color:
        return self.__color

    @property
    def position(self) -> Vector:
        return self.__position

    # setter methods
    @screen.setter
    def screen(self, screen: pygame.Surface) -> None:
        if screen is None or not isinstance(screen, pygame.Surface):
            raise ValueError(f'{self.__class__.__name__}.screen must be of type pygame.Surface.')
        self.__screen: pygame.Surface = screen

    @text.setter
    def text(self, text: str) -> None:
        if text is None or not isinstance(text, str):
            raise ValueError(f'{self.__class__.__name__}.text must be a str.')
        self.__text: str = text
        # reevaluate text
        self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
        self.__rect: pygame.Rect = self.__text_surface.get_rect()
        self.__rect.topleft: tuple[int, int] = self.position.as_tuple()

    @font_name.setter
    def font_name(self, font_name: str) -> None:
        if font_name is None or not isinstance(font_name, str):
            raise ValueError(f'{self.__class__.__name__}.font_name must be a str.')
        self.__font_name: str = font_name
        # reevaluate text with new font
        self.__font: pygame.font.Font = pygame.font.SysFont(self.font_name, self.font_size)
        self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
        self.__rect: pygame.Rect = self.__text_surface.get_rect()
        self.__rect.topleft: tuple[int, int] = self.position.as_tuple()

    @font_size.setter
    def font_size(self, font_size: int) -> None:
        if font_size is None or not isinstance(font_size, int):
            raise ValueError(f'{self.__class__.__name__}.font_size must be an int.')
        self.__font_size: int = font_size
        # reevaluate text with new font size
        self.__font: pygame.font.Font = pygame.font.SysFont(self.font_name, self.font_size)
        self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
        self.__rect: pygame.Rect = self.__text_surface.get_rect()
        self.__rect.topleft: tuple[int, int] = self.position.as_tuple()

    @color.setter
    def color(self, color: str | int | tuple[int, int, int, Optional[int]] | list[int, int, int, Optional[int]] | pygame.Color) -> None:
        try:
            self.__color: pygame.Color = pygame.Color(color)
            # reevaluate text with new font color
            self.__text_surface: pygame.Surface = self.__font.render(self.text, True, self.color)
            self.__rect: pygame.Rect = self.__text_surface.get_rect()
            self.__rect.topleft: tuple[int, int] = self.position.as_tuple()
        except (ValueError, TypeError):
            raise ValueError(f'{self.__class__.__name__}.color must be a one of the following types: str or int or tuple(int, int, int, [int]) or list(int, int, int, [int]) or pygame.Color.')

    @position.setter
    def position(self, position: Vector) -> None:
        if position is None or not isinstance(position, Vector):
            raise ValueError(f'{self.__class__.__name__}.position must be a Vector.')
        self.__position: Vector = position
        # reevaluate text position with new position
        self.__rect.topleft: tuple[int, int] = self.position.as_tuple()
