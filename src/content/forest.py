import random

from .stage import Stage
from .tiles import Tiles


class Forest(Stage):
    def __init__(self, game, width, height):
        super().__init__(game, width, height)

        self.percent_goal = 40
        self.walk_iter = 25000
        self.center_weight = 20
        self.prev_dir_weight = 70

    def generate(self):
        self.walk_iter = max(self.walk_iter, (self.width * self.height * 10))
        self.fill_with(Tiles.Tree)

        self.filled = 0
        self.prev_dir = None
        self.drunk_x = random.randint(2, self.width - 2)
        self.drunk_y = random.randint(2, self.height - 2)
        self.filled_goal = self.width * self.height * self.percent_goal

        for _ in range(self.walk_iter):
            self.walk()
            if self.filled >= self.filled_goal:
                break

    def walk(self):
        n, s, e, w = 1.0, 1.0, 1.0, 1.0

        if self.drunk_x <= self.width * 0.25:
            e += self.center_weight
        elif self.drunk_y >= self.height * 0.75:
            w += self.center_weight

        if self.drunk_y <= self.height * 0.25:
            s += self.center_weight
        elif self.drunk_y >= self.height * 0.75:
            n += self.center_weight

        if self.prev_dir == 'n':
            n += self.prev_dir_weight
        if self.prev_dir == 's':
            s += self.prev_dir_weight
        if self.prev_dir == 'e':
            e += self.prev_dir_weight
        if self.prev_dir == 'w':
            w += self.prev_dir_weight

        total = n + s + e + w

        n /= total
        s /= total
        e /= total
        w /= total

        choice = random.random()
        if 0 <= choice < n:
            dx, dy = 0, -1
            direction = 'n'
        elif n <= choice < (n + s):
            dx, dy = 0, 1
            direction = 's'
        elif (n + s) <= choice < (n + s + e):
            dx, dy = 1, 0
            direction = 'e'
        else:
            dx, dy = -1, 0
            direction = 'w'

        if (0 < self.drunk_x + dx < self.width - 1) and (0 < self.drunk_y + dy < self.height - 1):
                self.drunk_x += dx
                self.drunk_y += dy
                if type(self.get_tile(self.drunk_x, self.drunk_y)) == Tiles.Tree:
                    self.set_tile(self.drunk_x, self.drunk_y, Tiles.Floor)
                    self.filled += 1
                self.prev_dir = direction
