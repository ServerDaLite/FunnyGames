items = {
    "Fish": 60,
    "Sword": 50,
    "Flop": 40,
    "Rock": 30,
    "Pebble": 20,
    "George": 10,
    "Mary": 1,
}

from random import random

def random_item(items_list):
    total_chance = sum([val for val in items_list.values()])
    items = list()
    for item in items_list:
        if items_list[item] / total_chance > random():
            items.append(item)
    return items if len(items) > 0 else ["Nothing"]

def generate_items_menu(items_list):
    total_chance = sum([val for val in items_list.values()])
    return ["*" for item in items], [val/total_chance for val in items_list.values()]

result = random_item(items)
item, chances = generate_items_menu(items)
items = list(items)

for it in result:
    if it == "Nothing":
        print("YOU LOST!!! HAHAHAHA")
    else:
        item[items.index(it)] = it

for pos in range(len(items)):
    print(f"{item[pos]} == {chances[pos]}")
            
