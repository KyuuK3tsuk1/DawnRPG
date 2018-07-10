import random
import pygame as pg

from .stage import Stage
from .tiles import Tiles


class Dungeon(Stage):
    def __init__(self, game, width, height):
        super().__init__(game, width, height)

        self.MAX_ROOM_SIZE = 15
        self.MIN_ROOM_SIZE = 6
        self.MAX_ROOMS = 50

    def generate(self):
        self.fill_with(Tiles.Wall)

        rooms = []
        num_rooms = 0

        for r in range(self.MAX_ROOMS):
            size = random.randrange(self.MIN_ROOM_SIZE, self.MAX_ROOM_SIZE, 2)
            rectangularity = random.randrange(0, 1 + size // 2)
            room_w = size
            room_h = size
            if random.randint(0, 1) == 1:
                room_w += rectangularity
            else:
                room_h += rectangularity
            
            room_x = random.randint(0, self.width - room_w)
            room_y = random.randint(0, self.height - room_h)

            new_room = pg.Rect(room_x, room_y, room_w, room_h)

            failed = False
            for other_room in rooms:
                if new_room.colliderect(other_room) or \
                        new_room.right == other_room.left or\
                        new_room.left == other_room.right or\
                        new_room.top == other_room.bottom or \
                        new_room.bottom == other_room.top:
                    failed = True
                    break

            if not failed:
                self.create_room(new_room)
                (new_x, new_y) = new_room.center
                print(new_x, new_y)

                if num_rooms != 0:
                    prev_x, prev_y = rooms[-1].center
                    if random.randint(0, 1) == 1:
                        self.create_hor_tunnel(prev_x, new_x, prev_y)
                        self.create_vir_tunnel(prev_y, new_y, new_x)
                    else:
                        self.create_vir_tunnel(prev_y, new_y, prev_x)
                        self.create_hor_tunnel(prev_x, new_x, new_y)

                rooms.append(new_room)
                num_rooms += 1

    def create_room(self, room):
        for x in range(room.x, room.right):
            for y in range(room.y, room.bottom):
                self.set_tile(x, y, Tiles.Floor)

    def create_hor_tunnel(self, x1, x2, y):
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        for x in range(x_min, x_max + 1):
            self.set_tile(x, y, Tiles.Floor)

    def create_vir_tunnel(self, y1, y2, x):
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        for y in range(y_min, y_max + 1):
            self.set_tile(x, y, Tiles.Floor)
