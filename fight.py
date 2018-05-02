from hero import Hero
from enemy import Enemy
from weapon import Weapon
from spell import Spell


class Fight:
    def __init__(self, hero, enemy):
        self.hero = hero
        self.enemy = enemy

    def start_fight(self):
        while self.hero.is_alive() and self.enemy.is_alive():
            self.enemy.take_damage(self.hero.bigger_damage())
            self.hero.take_damage(self.enemy.attack())
        if self.hero.is_alive():
            print("Enemy is dead")
            
        else:
            print("Hero is dead")
        return self.hero.is_alive()


h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100)
weapon = Weapon("weapon", 200)
h.equip(weapon)
spell = Spell()
h.learn(spell)
enemy = Enemy(health=100, mana=100, damage=20)
fight = Fight(h, enemy)
fight.start_fight()
 