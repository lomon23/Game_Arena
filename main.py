from ursina import *
from room.basic_room import Room
from entity.player import Player
from entity.enemy import Enemy2D 
from ui.menu import MainMenu 

app = Ursina()

menu = MainMenu()
#room = Room(scale = 20)
#player = Player( position = (0, 2, 0))
#ememy = Enemy2D( player, position=(5,0,5)),
#sky = Sky(texture = 'sprite/room_sprite/indigo_up.jpg')

app.run() 
