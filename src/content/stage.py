
from .tiles import Tiles


class Stage:
    def __init__(self, game, width, height):
        self.game = game
        self.width = width
        self.height = height

        self.actors = [[None for x in range(self.width)]
                       for y in range(self.height)]
        self.tiles = [[None for x in range(self.width)]
                      for y in range(self.height)]
        self.items = []

    def generate(self):
        self.fill_with(Tiles.Wall)
        for x in range(1, self.width - 1):
            for y in range(1, self.height - 1):
                self.set_tile(x, y, Tiles.Floor)

        self.set_tile(self.width // 2, self.height // 2, Tiles.ClosedDoor)

    def fill_with(self, tile_type):
        self.tiles = [[tile_type(self, x, y) for x in range(
            self.width)] for y in range(self.height)]
 
    def in_bounds(self, x, y) -> bool:
        if (0 <= x < self.width) and (0 <= y < self.height):
            return True
        return False

    def get_tile(self, x, y):
        if self.in_bounds(x, y):
            return self.tiles[x][y]

    def set_tile(self, x, y, new_tile):
        if self.in_bounds(x, y):
            self.tiles[x][y] = new_tile(self, x, y)

    def get_actor_at(self, x, y):
        if self.in_bounds(x, y):
            return self.actors[x][y]

    def get_item_at(self, x, y):
        for item in self.items:
            if (item.x, item.y) == (x, y):
                return item
            else:
                return None
