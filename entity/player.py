from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController


class Player(FirstPersonController):
    def __init__(self, position = (0,1,0)):
        super().__init__()
        self.position = position
        #self.model = "cube",
        #self.color = color.red, 
        self.speed = 5
        
        

    #def upadate(self):
    #    if held_keys['a']:
    #        self.rotation_y -= 2
    #    if held_keys['d']:
    #        self.rotation_y += 2
