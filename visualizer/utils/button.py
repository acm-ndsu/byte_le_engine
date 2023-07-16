import typing

import pygame
from visualizer.utils.text import Text
from game.utils.vector import Vector
from typing import Optional, Callable
from typing import TypeAlias

"""
Class that creates an intractable button extending the Text class.

Defaults same as defaults used in Text class.
"""

# typing alias for color
Color: TypeAlias = str | int | tuple[int, int, int, Optional[int]] | list[
    int, int, int, Optional[int]] | pygame.Color


class Button(Text):

    def __init__(self, screen: pygame.Surface, text: str, font_size: int, color_hover: Color, color_clicked: Color, action: Callable = None,
                 font_name: str = 'bauhaus93',
                 color: Color = pygame.Color('#daa520'),
                 position: Vector = Vector(0, 0)):
        super().__init__(screen, text, font_size, font_name, color, position)
        self.color_hover: Color = color_hover       # color for hovering over button
        self.color_clicked: Color = color_clicked   # color for clicking button
        self.color_default: Color = self.color
        self.action: Callable = action
        self.mouse: pygame.mouse = pygame.mouse     # get mouse object from pygame for reference


    # getter methods
    @property
    def color_hover(self) -> Color:
        return self.__color_hover

    @property
    def color_clicked(self) -> Color:
        return self.__color_clicked

    @property
    def mouse(self) -> pygame.mouse:
        return self.__mouse

    @property
    def action(self) -> Callable:
        return self.__action

    # setter methods

    @color_hover.setter
    def color_hover(self, color_hover: Color) -> None:
        try:
            self.__color_hover: Color = pygame.Color(color_hover)
        except (ValueError, TypeError):
            raise ValueError(
                f'{self.__class__.__name__}.color_hover must be a one of the following types: str or int or tuple('
                f'int, int, int, [int]) or list(int, int, int, [int]) or pygame.Color.')

    @color_clicked.setter
    def color_clicked(self, color_clicked: Color) -> None:
        try:
            self.__color_clicked: Color = pygame.Color(color_clicked)
        except (ValueError, TypeError):
            raise ValueError(
                f'{self.__class__.__name__}.color_clicked must be a one of the following types: str or int or tuple('
                f'int, int, int, [int]) or list(int, int, int, [int]) or pygame.Color.')

    @mouse.setter
    def mouse(self, mouse: pygame.mouse) -> None:
        if mouse is None:
            raise ValueError(f'{self.__class__.__name__}.mouse must be of type pygame.mouse')
        self.__mouse: pygame.mouse = mouse

    @action.setter
    def action(self, action: Callable) -> None:
        if action is not None and not isinstance(action, Callable):
            raise ValueError(f'{self.__class__.__name__}.action must be of type Callable')
        self.__action = action

    # methods

    def execute(self, *args, **kwargs) -> any:
        return self.action(*args, **kwargs)

    def mouse_hover(self) -> bool:
        self.color = self.color_default
        if self.rect.collidepoint(self.__mouse.get_pos()):
            self.color = self.color_hover
            return True
        return False

    def mouse_clicked(self, event: pygame.event) -> None:
        if self.mouse_hover() and event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.color = self.color_clicked
                self.execute()
