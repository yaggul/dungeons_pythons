from dungeon import Dungeon, h
from hero import Hero



#h = Hero(name="Bron", title="Dragonslayer", health=10, mana=10, mana_regeneration_rate=2)

map = Dungeon('level1.txt')

map.print_map()
print()
map.spawn(h)

print()
map.print_map()
#map.move_hero('right')
#print('Move right')
#print(map.print_map())
#print('Move left')
#map.move_hero('left')
#map.print_map()
#map.move_hero('down')
#map.print_map()
#print('Move up')
#map.move_hero('up')
#map.print_map()
print('move down')
map.move_hero('down')
map.print_map()
print('move right')
map.move_hero('right')
map.print_map()
map.pick_treasure()
#print(map.hero.get_health())
print('move right')
map.move_hero('right')
map.print_map()
#print(map.pick_treasure())

print('Healt', map.hero.get_health())
print('Mana', map.hero.get_mana())

