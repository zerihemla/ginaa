from lists.magic_lists.wild_magic import wild_magic_list

from custom_libs.helper_func import *

def get_wild_magic_effect():
    ret_string = select_from_list(wild_magic_list)
    return ret_string


if __name__ == "__main__":

    print(get_wild_magic_effect())