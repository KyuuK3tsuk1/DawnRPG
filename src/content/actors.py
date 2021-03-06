import pygame as pg

import src.engine.config as cfg
import src.content.actions as actions
import src.util.directions as Directions
import src.util.colors as Colors


class Actor(pg.sprite.Sprite):
    def __init__(self, game, stage, x, y):
        self._layer = cfg.ACTOR_LAYER
        self.game = game
        self.stage = stage
        self.x, self.y = x, y
        super().__init__(self.game.all_sprites)
        self.image = self.to_glyph("@", Colors.Red)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.x * cfg.TILE_SIZE, self.y * cfg.TILE_SIZE

        self.game.add_actor(self)

        self.next_action = None
    
    def to_glyph(self, char, fg_color):
        font = pg.font.Font(cfg.DEFAULT_FONT, cfg.TILE_SIZE)
        glyph = font.render(char, True, fg_color, Colors.Black)
        return glyph

    def get_action(self):
        action = self.next_action
        self.next_action = None
        return action

    def set_next_action(self, next_action):
        self.next_action = next_action

    def update(self):
        self.rect.topleft = self.x * cfg.TILE_SIZE, self.y * cfg.TILE_SIZE


class Hero(Actor):
    def __init__(self, game, stage, x, y):
        super().__init__(game, stage, x, y)

        self.image = self.to_glyph("@", Colors.Green)

    def handle_input(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.set_next_action(actions.Walk(self, Directions.Up))
            if event.key == pg.K_a:
                self.set_next_action(actions.Walk(self, Directions.Left))
            if event.key == pg.K_s:
                self.set_next_action(actions.Walk(self, Directions.Down))
            if event.key == pg.K_d:
                self.set_next_action(actions.Walk(self, Directions.Right))
            if event.key == pg.K_e:
                self.set_next_action(actions.OpenDoor(self, None))
            if event.key == pg.K_q:
                self.set_next_action(actions.CloseDoor(self, None))
