import pygame as pg

import src.content.stage as stage
import src.content.actors as actors
import src.engine.config as cfg


class Engine:
    def __init__(self, title, win_w, win_h):
        self.title = title
        self.win_w = win_w
        self.win_h = win_h

        self.window = pg.display.set_mode((self.win_w, self.win_h))
        self.clock = pg.time.Clock()
        self.running = True

        pg.display.set_caption(self.title)

        if cfg.KEY_REPEAT:
            pg.key.set_repeat(cfg.KEY_REPEAT_DELAY, cfg.KEY_REPEAT_SPD)

        self.setup()

    def setup(self):
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.actors = []
        self.current_actor = 0

        self.stage = stage.Stage(self, 10, 10)
        self.stage.generate()

        self.player = actors.Hero(self, self.stage, 2, 2)

    def add_actor(self, actor):
        self.actors.append(actor)

    def quit(self):
        self.running = False

    def start(self):
        while self.running:
            self.clock.tick(cfg.FPS)
            self.handle_events()
            self.update()
            self.draw()

    def handle_events(self):
        for event in pg.event.get():

            self.player.handle_input(event)

            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()

    def update(self):
        action = self.actors[self.current_actor].get_action()
        if action is None:
            return
        action.perform()
        self.actors[self.current_actor].update()
        self.current_actor = (self.current_actor + 1) % len(self.actors)

    def draw(self):
        self.window.fill((51, 51, 51))
        self.all_sprites.draw(self.window)
        pg.display.flip()
