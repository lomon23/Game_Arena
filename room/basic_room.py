from ursina import *

class Room(Entity):
    def __init__(self, scale=10, height=5):
        super().__init__()

        thickness = 0.2  
        
        self.floor = Entity(
            parent=self,
            model="plane",
            scale=(scale, 1, scale),
            texture="white_cube",
            texture_scale=(scale, scale),
            collider="box",
            position=(0, 0, 0)
        )

        
        wall_positions = [
            ((0, height / 2, scale / 2 - thickness / 2), (0, 0, 0)),          
            ((0, height / 2, -scale / 2 + thickness / 2), (0, 180, 0)),       
            ((-scale / 2 + thickness / 2, height / 2, 0), (0, 90, 0)),       
            ((scale / 2 - thickness / 2, height / 2, 0), (0, -90, 0)),       
        ]

        self.walls = []
        for pos, rot in wall_positions:
            wall = Entity(
                parent=self,
                model="cube",
                scale=(scale, height, thickness),
                texture="brick",
                texture_scale=(scale, height),
                collider="box",
                position=pos,
                rotation=rot
            )
            self.walls.append(wall)

