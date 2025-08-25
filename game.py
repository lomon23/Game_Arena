from ursina import *
from room.basic_room import Room
from entity.player import Player
from entity.enemy import Enemy2D

def start_game():
    # Тут створюємо всі об'єкти гри
    room = Room(scale=20)
    player = Player(position=(0, 2, 0))
    enemy = Enemy2D(player, position=(5,0,5))
    sky = Sky(texture='sprite/room_sprite/indigo_up.jpg')

    # Якщо потрібен update
    def update():
        player.update()
        enemy.update()

