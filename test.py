
from ursina import *
from system.animation import SpriteSheetAnimation

app = Ursina()
print('package_folder:', application.package_folder)
print('asset_folder:', application.asset_folder)

# горизонтальний спрайтшит (рядок з кадрами)
player = SpriteSheetAnimation(
    texture_path='sprite/enemy_sprite/enemy_animation.png',
    frame_count=8,
    fps=6,
    orientation="horizontal",   # <-- можна вибрати "vertical" або "horizontal"
    scale=2
)

def update():
    player.update()

app.run()

