class GameEntity:
    def __init__(self, health, stamina, damage, speed, weapon=None, armor=0, score_value=0):
        self.health = health
        self.max_health = health
        self.stamina = stamina
        self.max_stamina = stamina
        self.damage = damage
        self.speed = speed
        self.weapon = weapon
        self.armor = armor
        self.score_value = score_value
        self.alive = True

    def take_damage(self, amount):
        reduced_damage = max(0, amount - self.armor)
        self.health = max(0, self.health - reduced_damage)
        if self.health == 0:
            self.alive = False

    def heal(self, amount):
        self.health = min(self.max_health, self.health + amount)

    def use_stamina(self, amount):
        if self.stamina >= amount:
            self.stamina -= amount
            return True
        return False

    def regenerate_stamina(self, amount):
        self.stamina = min(self.max_stamina, self.stamina + amount)

    def is_alive(self):
        return self.alive


class PlayerEntity(GameEntity):
    def __init__(self):
        super().__init__(
            health=150,
            stamina=120,
            damage=15,
            speed=5,
            weapon="Sword",
            armor=5
        )


class EnemyEntity(GameEntity):
    def __init__(self):
        super().__init__(
            health=80,
            stamina=50,
            damage=8,
            speed=2.5,
            weapon="Claws",
            score_value=50
        )
