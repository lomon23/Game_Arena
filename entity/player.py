from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController



class Player(FirstPersonController):
    def __init__(self, position=(0, 1, 0)):
        super().__init__()
        self.position = position
        self.speed = 10

        # Модель та колір гравця (можна розкоментувати для тестів)
        # self.model = 'cube'
        # self.color = color.red
        # self.scale = (1, 2, 1)

        # Додати меч як дочірню модель гравця
        self.weapon = Entity(
            model='sprite/weapon_sprite/oSword.obj',  # твоя модель меча
            texture='sprite/weapon_sprite/tSword_Difusse.png',              # якщо буде текстура
            parent=self,                              # прив'язка до гравця
            position=(0.5, 1.5 , 1),                  # відносно гравця
            scale=0.1,
            rotation = (0, 80, 0)
            #rotation_y = -80
        )

        
