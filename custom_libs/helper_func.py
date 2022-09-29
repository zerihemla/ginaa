import random


DIVIDER_STARS = "*************************************************"

def get_rand_index(list_size:int):
    return random.randint(0, (list_size-1))

def select_from_list(this_list:list):
    list_len = len(this_list)
    sel_index = get_rand_index(list_len)
    sel_item = this_list[sel_index]
    return sel_item

def select_from_list_not_first(this_list:list):
    list_len = len(this_list)
    sel_index = get_rand_index(list_len - 1) + 1
    sel_item = this_list[sel_index]
    return sel_item