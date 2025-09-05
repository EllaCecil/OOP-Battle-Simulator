from enemy import Enemy

class BigDuck(Enemy):
    def __init__(self, name):
        super().__init__(name)
        self.health = 300
        self.attack_power = 20
    def attack(self):
        if self.health < 50:
            self.attack_power = 80
        elif self.health < 150:
            self.attack_power = 60
        elif self.health < 200:
            self.attack_power = 40
        elif self.health < 250:
            self.attack_power = 30
        return self.attack_power