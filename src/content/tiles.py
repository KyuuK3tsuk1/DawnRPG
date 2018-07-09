import pygame as pg

import src.engine.config as cfg
import src.util.colors as Colors


class Tiles:
    class Tile(pg.sprite.Sprite):
        def __init__(self, stage, x, y):
            self._layer = cfg.TILE_LAYER
            self.stage = stage
            self.x, self.y = x, y
            super().__init__(self.stage.game.all_sprites)
            self.image = pg.Surface((cfg.TILE_SIZE, cfg.TILE_SIZE))
            self.rect = self.image.get_rect()
            self.rect.topleft = self.x * cfg.TILE_SIZE, self.y * cfg.TILE_SIZE

            self.is_solid = False
            self.opens_to = None
            self.closes_to = None

    class Floor(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image.fill(Colors.White)

    class Wall(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image.fill(Colors.Black)

            self.is_solid = True

    class Tree(Wall):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image.fill(Colors.Green)

    class OpenDoor(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image.fill(Colors.Yellow)

            self.closes_to = Tiles.ClosedDoor

    class ClosedDoor(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image.fill(Colors.Orange)

            self.is_solid = True
            self.opens_to = Tiles.OpenDoor
