from item_info import *
import random

#takes roll and list returns item
def percent_select_roll(roll, _list):
    for i in _list:
        if i['low_percent'] <= roll <= i['high_percent']:
            selected_item = i
    return selected_item


def create():
    init_roll = random.randint(1, 100)
    selected_item_list = percent_select_roll(init_roll, item_list)
    item_select_roll = random.randint(1, 100)
    item = percent_select_roll(item_select_roll, selected_item_list['list'])
    return item
