from ursina import *

app = Ursina()

cube = Entity(model='cube', texture='white_cube', scale=2, position=(0,1,0))
floor = Entity(model='plane', scale=10, texture='white_cube', texture_scale=(10,10), collider='box')

app.run()
