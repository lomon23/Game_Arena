from ursina import Ursina
from room.basic_room import Room
from entity.player import Player

app = Ursina()

room = Room(scale = 20)
player = Player( position = (0, 1, 0))

app.run() 
