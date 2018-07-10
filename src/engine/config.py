
from os import path

ROOT_DIR = path.dirname(__file__)
RES_DIR = path.join(ROOT_DIR, "res")
FONT_DIR = path.join(RES_DIR, "fonts")

DEFAULT_FONT = path.join(FONT_DIR, "PressStart2P-Regular.ttf")

FPS = 30
TILE_SIZE = 8

KEY_REPEAT = True
KEY_REPEAT_SPD = 100
KEY_REPEAT_DELAY = 100

TILE_LAYER = 0
ACTOR_LAYER = 1
