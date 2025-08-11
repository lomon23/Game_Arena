from ursina import *

class Enemy2D(Entity):
    def __init__(self, player, position=(0,0,0), speed=2):
        super().__init__(
            model='quad',                # плоский спрайт
            texture='white_cube',        # постав сюди свою текстуру
            position=position,
            scale=(1,1,1),
            billboard=True,              # завжди повертає до камери
            double_sided=True,
            collider='box'
        )
        self.player = player
        self.speed = speed

    def update(self):
        # Вектор від противника до гравця по XZ (горизонтальна площина)
        direction = Vec3(
            self.player.x - self.x,
            0,
            self.player.z - self.z
        ).normalized()

        # Рух до гравця
        self.position += direction * self.speed * time.dt
