import pygame as pg

import engine.config as cfg

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
            if event.type == pg.QUIT:
                self.quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.quit()
    
    def update(self):
        pass
    
    def draw(self):
        self.window.fill((51, 51, 51))
        pg.display.flip();