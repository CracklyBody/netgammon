import config as c
from game import Game


class Backgammon(Game):
    def __init__(self):
        super().__init__(
            c.CAPTION,
            c.SCREEN_WIDTH,
            c.SCREEN_HEIGHT,
            c.BACKGROUND_IMAGE,
            c.FRAME_RATE
        )