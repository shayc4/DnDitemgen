from item_info import *
import random
def create():
    init_roll = random.randint(1,100)
    for x in item_list:
        if x['low_percent']<=init_roll<=x['high_percent']:
            selected_item_list = x['list']
    item_select_roll = random.randint(0,len(selected_item_list)-1)
    item = selected_item_list[item_select_roll]
    return item
