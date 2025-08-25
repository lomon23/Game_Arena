
from ursina import *

app = Ursina()

enemy_walk = SpriteSheetAnimation(
    'sprite/enemy_sprite/enemy_animation.png',
    rows=1,      # один ряд
    cols=8,      # вісім колонок
    fps=6,
    scale=3,
    loop=True
)

app.run()

