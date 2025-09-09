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
        self.weapon_pivot = Entity(parent=self, position=(0.5, 1.5, 1))
        self.weapon = Entity(
            model='sprite/weapon_sprite/oSword.obj',
            texture='sprite/weapon_sprite/tSword_Difusse.png',
            parent=self.weapon_pivot,
            position=(0, 0, 0),
            scale=0.1,
            rotation=(0, 80, 0)
        )

    def input(self, key):
        if key == 'left mouse down':
            # анімуємо обертання на 90 градусів по Y
            self.weapon_pivot.animate('rotation_x', 100, duration=0.2, curve=curve.in_out_quad)
            invoke(lambda: self.weapon_pivot.animate('rotation_x', 0, duration=0.15, curve=curve.in_out_quad), delay=0.15)

        
        
