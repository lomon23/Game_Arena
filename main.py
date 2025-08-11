from ursina import *
from room.basic_room import Room
from entity.player import Player
from entity.enemy import Enemy2D  

app = Ursina()

room = Room(scale = 20)
player = Player( position = (0, 2, 0))
Enemy2D(player, position=(5,0,5)),
sky = Sky(texture = 'sprite/room_sprite/indigo_up.jpg')

app.run() 
