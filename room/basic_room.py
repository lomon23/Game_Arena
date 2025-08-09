from ursina import *

class Room(Entity):
    def __init__(self, scale = 10):
        super().__init__()
        self.floor = Entity(parent = self, model = "plane", scale = (scale, 1 ,scale ),         texture = "while_cube", texture_scale = (scale, scale), collider = "box")



