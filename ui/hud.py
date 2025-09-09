class HUD:
    def __init__(self):
        self.health = 100
        self.stamina = 100
        self.max_health = 100
        self.max_stamina = 100

        self.health_bg = Entity(parent=camera.ui, model='quad', color=color.dark_red, scale=(0.3,0.03), position=(-0.35,0.45))
        self.health_bar = Entity(parent=self.health_bg, model='quad', color=color.red, scale=(1,1), origin=(-0.5,0.5))

        self.stamina_bg = Entity(parent=camera.ui, model='quad', color=color.gray, scale=(0.3,0.03), position=(-0.35,0.4))
        self.stamina_bar = Entity(parent=self.stamina_bg, model='quad', color=color.green, scale=(1,1), origin=(-0.5,0.5))

    def update(self):
        self.health_bar.scale_x = self.health / self.max_health
        self.stamina_bar.scale_x = self.stamina / self.max_stamina

