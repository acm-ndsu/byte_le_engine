from game.utils.vector import Vector


class Config:
    __NUMBER_OF_FRAMES_PER_TURN: int = 4
    __TILE_SIZE: int = 16
    __SCALE: int = 2
    __SCREEN_SIZE: Vector = Vector(x=1366, y=768)  # width, height
    __FRAME_RATE: int = 4

    @property
    def NUMBER_OF_FRAMES_PER_TURN(self) -> int:
        return self.__NUMBER_OF_FRAMES_PER_TURN

    @property
    def TILE_SIZE(self) -> int:
        return self.__TILE_SIZE

    @property
    def SCALE(self) -> int:
        return self.__SCALE

    @property
    def SCREEN_SIZE(self) -> Vector:
        return self.__SCREEN_SIZE

    @property
    def FRAME_RATE(self) -> int:
        return self.__FRAME_RATE
