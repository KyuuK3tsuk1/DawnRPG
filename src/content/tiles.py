import pygame as pg
import random

import src.engine.config as cfg
import src.util.colors as Colors
import src.util.directions as Directions


class Tiles:
    class Tile(pg.sprite.Sprite):
        def __init__(self, stage, x, y):
            self._layer = cfg.TILE_LAYER
            self.stage = stage
            self.x, self.y = x, y
            super().__init__(self.stage.game.all_sprites)
            self.image = self.to_glyph("")
            self.rect = self.image.get_rect()
            self.rect.topleft = self.x * cfg.TILE_SIZE, self.y * cfg.TILE_SIZE

            self.is_solid = False
            self.opens_to = None
            self.closes_to = None

        def to_glyph(self, char, fg_color=Colors.White, bg_color=Colors.Black):
            font = pg.font.Font(cfg.DEFAULT_FONT, cfg.TILE_SIZE)
            glyph = font.render(char, True, fg_color, bg_color)
            glyph = pg.transform.scale(glyph, (cfg.TILE_SIZE, cfg.TILE_SIZE))
            return glyph

    class Floor(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image = self.to_glyph(u"\u00B7", Colors.Grey)

    class Wall(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image = self.to_glyph("#", Colors.Black, Colors.White)

            self.is_solid = True

        # Made it an option to set all the tiles
        # that don't enclose playable space
        # black filler tiles
        def change_to_black(self):
            neighbor_count = 0
            for direction in Directions.All:
                dx, dy = direction
                tile = self.stage.get_tile(self.x + dx, self.y + dy)
                if type(tile) == type(self):
                    neighbor_count += 1

            print(neighbor_count)
            if neighbor_count == 4:
                self.image = pg.Surface((cfg.TILE_SIZE, cfg.TILE_SIZE))

    class Tree(Wall):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            chars = [u"\u2660", u"\u25B2"]
            self.image = self.to_glyph(random.choice(chars), Colors.Green)

    class OpenDoor(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image = self.to_glyph("-", Colors.Yellow)

            self.closes_to = Tiles.ClosedDoor

    class ClosedDoor(Tile):
        def __init__(self, stage, x, y):
            super().__init__(stage, x, y)
            self.image = self.to_glyph("+", Colors.Yellow)

            self.is_solid = True
            self.opens_to = Tiles.OpenDoor
