from dungeon import Dungeon
from hero import Hero
from fight import Fight
from weapon import Weapon
from spell import Spell
from enemy import Enemy


h = Hero(name="Bron", title="Dragonslayer", health=20, mana=100)
weapon = Weapon("weapon", 200)
h.equip(weapon)
spell = Spell()
h.learn(spell)
enemy = Enemy(health=100, mana=100, damage=20)

map = Dungeon('level1.txt')

map.print_map()
print()
map.spawn(h)

print()
map.print_map()
map.move_hero('right')
print('Move right')
map.print_map()
print('Move left')
map.move_hero('left')
map.print_map()
print('move down')
map.move_hero('down')
map.print_map()
print('Move up')
map.move_hero('up')
map.print_map()
# print('move down')
# map.move_hero('down')
# map.print_map()
# print('move right')
# map.move_hero('right')
# map.print_map()
# map.pick_treasure()
# #print(map.hero.get_health())
# print('move down')
# map.move_hero('down')
# print()
# map.print_map()
# #print(map.pick_treasure())

# print('Healt', map.hero.get_health())
# print('Mana', map.hero.get_mana())

