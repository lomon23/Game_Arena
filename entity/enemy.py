
from ursina import *
import random, math
from entity.entities import EnemyEntity
from system.animation import SpriteSheetAnimation





class Enemy2D(Entity):
    def __init__(self, player, position=(0,1,0), speed=2, patrol_bounds=None):
        super().__init__(
            #model='quad',
            origin_y=1,
            position=position,
            scale=(2,3,0),
            billboard=False,
            double_sided=True,
            collider='box'
        )

        # анімація як дочірній компонент, підхоплює position, scale і parent
        self.anim = SpriteSheetAnimation(
            texture_path='sprite/enemy_sprite/enemy_animation.png',
            frame_count=8,
            fps=6,
            orientation="horizontal",
            parent=self,         # робимо дочірнім
            scale=1,              # анімація буде під масштаб батька
            position = (0, 0.5, 0)
        )

        self.stats = EnemyEntity()  
        self.player = player
        self.speed = speed
        self.state = 'patrol'
        self.view_distance = 8.0
        self.time_since_seen = 0

        # Параметри атаки
        self.attack_speed = 1.5       # сек між ударами
        self.damage = 10              # шкода
        self.stamina_cost = 20        # скільки стаміни йде на удар
        self.stamina_recovery_threshold = 25  # скільки треба накопичити, щоб знову бити
        self.attack_range = 3.0
        self.attack_cooldown = 0      # таймер кулдауна

        # Патруль
        self.patrol_distance_range = (1.0, 3.0)
        self.patrol_angle_range = (30.0, 180.0)
        self.patrol_wait_range = (0.5, 1.5)
        self.heading_angle = random.uniform(0, 360)
        self.patrol_target = None
        self.wait_timer = 0.0
        self.patrol_bounds = patrol_bounds
        self._set_new_patrol_target()

        # UI над головою
        self._create_bars()



    def _create_bars(self):
        self.hp_bar_bg = Entity(parent=self, model='quad', color=color.red,
                                scale=(1.5, 0.15, 1), position=(0, 1, 0))
        self.hp_bar = Entity(parent=self.hp_bar_bg, model='quad', color=color.green,
                             scale=(1, 1, 1), position=(-0.5, 0, 1), origin=(-0.5, 0))

        self.stamina_bar_bg = Entity(parent=self, model='quad', color=color.gray,
                                     scale=(1.5, 0.1, 1), position=(0, 0.8, -0.01))
        self.stamina_bar = Entity(parent=self.stamina_bar_bg, model='quad', color=color.azure,
                                  scale=(1, 1, 1), position=(-0.5, 0, -0.1), origin=(-0.5, 0))

    def _set_new_patrol_target(self):
        distance = random.uniform(*self.patrol_distance_range)
        angle_delta = random.choice([-1, 1]) * random.uniform(*self.patrol_angle_range)
        self.heading_angle = (self.heading_angle + angle_delta) % 360
        rad = math.radians(self.heading_angle)
        direction = Vec3(math.sin(rad), 0, math.cos(rad))
        target = self.position + direction * distance
        if self.patrol_bounds:
            min_x, max_x, min_z, max_z = self.patrol_bounds
            target.x = max(min_x, min(max_x, target.x))
            target.z = max(min_z, min(max_z, target.z))
        self.patrol_target = target
        self.wait_timer = 0.0

    def update(self):
    # Відновлення стаміни
        self.position.y = 0  # стоїть на підлозі

        if self.player:
            target_pos = Vec3(self.player.position.x, self.position.y, self.player.position.z)
            self.look_at(target_pos)


        self.stats.stamina = min(self.stats.max_stamina, self.stats.stamina + 5 * time.dt)

    # Оновлення UI
        self.hp_bar.scale_x = self.stats.health / self.stats.max_health
        self.stamina_bar.scale_x = self.stats.stamina / self.stats.max_stamina

    # Відновлення кулдауну
        if self.attack_cooldown > 0:
            self.attack_cooldown -= time.dt
        if hasattr(self, 'current_move_dir') and self.current_move_dir.length() > 0:
            # Повертаємось лише по осі Y (горизонтально)
            target_pos = self.position + self.current_move_dir
            self.look_at(target_pos, 'y')
    # Перевірка гравця
        if self.player:
            vec_to_player = self.player.position - self.position
            vec_to_player.y = 0
            if vec_to_player.length() <= self.view_distance:
                self.state = 'chase'
                self.time_since_seen = 0
            elif self.state == 'chase':
                self.time_since_seen += time.dt
                if self.time_since_seen >= 3:
                    self.state = 'patrol'

    # Виклик поведінки
        if self.state == 'patrol':
            self.Patrol()
        elif self.state == 'chase':
            self.Chase()

    def Patrol(self):
        if self.patrol_target is None:
            self._set_new_patrol_target()
            return
        dir_vec = self.patrol_target - self.position
        dir_vec.y = 0
        dist = dir_vec.length()
        if dist <= 0.05:
            if self.wait_timer <= 0:
                self.wait_timer = random.uniform(*self.patrol_wait_range)
            else:
                self.wait_timer -= time.dt
                if self.wait_timer <= 0:
                    self._set_new_patrol_target()
            return
        move_dir = dir_vec.normalized()
        self.position += move_dir * self.speed * time.dt

    def Chase(self):
        dir_vec = self.player.position - self.position
        dir_vec.y = 0
        dist = dir_vec.length()

        if dist <= self.attack_range:
            self.Attack()
            return

        move_dir = dir_vec.normalized()
        self.position += move_dir * self.speed * 1.5 * time.dt

    def Attack(self):
        # Перевіряємо кулдаун
        if self.attack_cooldown > 0:
            return

        # Перевіряємо стаміну
        if self.stats.stamina < self.stamina_cost:
            # Якщо стаміни не вистачає — чекаємо поки набереться більше порогу
            if self.stats.stamina < self.stamina_recovery_threshold:
                return

        # Використовуємо стаміну
        if not self.stats.use_stamina(self.stamina_cost):
            return

        # Завдаємо шкоди
#        print(f"Ворог б'є гравця на {self.damage} HP!")

        # Ставимо кулдаун
        self.attack_cooldown = self.attack_speed    

    def Dodge(self):
        # Ворога відштовхуємо від гравця
        direction = self.position - self.player.position
        direction.y = 0
        if direction.length() == 0:
            direction = Vec3(random.uniform(-1,1), 0, random.uniform(-1,1))

        move_dir = direction.normalized()
        dodge_speed = self.speed * 1.5
        self.position += move_dir * dodge_speed * time.dt

    # Зменшуємо таймер і перевіряємо стаміну для повернення
        self.dodge_timer -= time.dt
        if self.dodge_timer <= 0 and self.stats.stamina >= self.stamina_recovery_threshold:
            self.state = 'chase'  # або patrol, залежно від логіки
