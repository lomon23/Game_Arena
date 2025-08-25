from ursina import *
from ursina import texture_importer

texture_importer.Texture.default_filtering = None\

class MainMenu(Entity):
    def __init__(self):
        super().__init__()
        self.logo = Entity(
            parent = camera.ui,
            model = "quad",
            texture = "sprite_ui/menu_sprite/game_name_for_menu.png",
            scale = (0.6, 0.3),
            y = 0.3
        ) 
        self.start_btn = Button(
            texture="sprite_ui/menu_sprite/game_btn_start.png",
            scale=(0.6, 0.3),
            y=-0.010,

            color=color.white,  # щоб по дефолту була картинка
            highlight_color=color.rgba(0,0,0,150),  # затемнення при наведенні
            pressed_color=color.rgba(100, 100, 100, 255),  # при наведенні стає трохи прозорішою
               # коли натискаєш
            on_click=self.start_game
        )

        self.quit_btn = Button(
            texture="sprite_ui/menu_sprite/game_btn_quit.png",
            scale=(0.6, 0.3),
            y=-0.30,
            color=color.white,
            highlight_color=color.rgba(0,0,0,150),  # затемнення при наведенні
            pressed_color=color.rgba(100, 100, 100, 255), 
            on_click=application.quit
        )
        self.bg = Entity(
            parent = camera.ui,
            model = 'quad',
            texture = 'sprite_ui/menu_sprite/background.png',
            scale = (2, 1),
            z = 1
        )

    def start_game(self):
        from game import start_game
        # вимикаємо меню
        self.bg.enabled = False
        self.logo.enabled = False
        self.start_btn.enabled = False
        self.quit_btn.enabled = False
        # запускаємо гру
        start_game()
