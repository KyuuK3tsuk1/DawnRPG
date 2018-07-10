
import src.util.directions as Directions


class Action:
    def __init__(self, actor):
        self.actor = actor

    def perform(self):
        pass


class Walk(Action):
    def __init__(self, actor, direction):
        super().__init__(actor)
        self.direction = direction

    def perform(self):
        dx, dy = self.direction
        next_tile = self.actor.stage.get_tile(
            self.actor.x + dx, self.actor.y + dy)
        if next_tile.opens_to is not None:
            return OpenDoor(self.actor, self.direction).perform()
        if not next_tile.is_solid:
            self.actor.stage.actors[self.actor.x][self.actor.y] = None
            self.actor.x += dx
            self.actor.y += dy
            self.actor.stage.actors[self.actor.x][self.actor.y] = self.actor


class OpenDoor(Action):
    def __init__(self, actor, direction):
        super().__init__(actor)
        self.direction = direction

    def perform(self):
        if self.direction is None:
            for direction in Directions.All:
                dx, dy = direction
                tile = self.actor.stage.get_tile(
                    self.actor.x + dx, self.actor.y + dy)
                if tile.opens_to is not None:
                    self.actor.stage.set_tile(
                        self.actor.x + dx, self.actor.y + dy, tile.opens_to)
                    return
        else:
            dx, dy = self.direction
            tile = self.actor.stage.get_tile(
                self.actor.x + dx, self.actor.y + dy)
            if tile.opens_to is not None:
                self.actor.stage.set_tile(
                    self.actor.x + dx, self.actor.y + dy, tile.opens_to)
                return


class CloseDoor(Action):
    def __init__(self, actor, direction=None):
        super().__init__(actor)
        self.direction = direction

    def perform(self):
        if self.direction is None:
            for direction in Directions.All:
                dx, dy = direction
                tile = self.actor.stage.get_tile(
                    self.actor.x + dx, self.actor.y + dy)
                if tile.closes_to is not None:
                    self.actor.stage.set_tile(
                        self.actor.x + dx, self.actor.y + dy, tile.closes_to)
                    return
        else:
            dx, dy = self.direction
            tile = self.actor.stage.get_tile(
                self.actor.x + dx, self.actor.y + dy)
            if tile.closes_to is not None:
                self.actor.stage.set_tile(
                    self.actor.x + dx, self.actor.y + dy, tile.closes_to)
                return
