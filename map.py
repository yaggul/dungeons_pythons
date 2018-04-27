from dungeon import Dungeon
from hero import Hero

h = Hero(name="Bron", title="Dragonslayer", health=100, mana=100, mana_regeneration_rate=2)

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
print('Move down')
map.move_hero('down')
map.print_map()
print('Move up')
map.move_hero('up')
map.print_map()

