import sys
sys.path.append("../")

from lists.treasure_lists.tresure import *

from custom_libs.helper_func import *

# self.name = name
# self.description = description
# self.value = value
# self.rarity = rarity
# self.weight = weight
# self.category = category
# self.properties = properties
# self.requirements = requirements


class GeneratedTreasure():
    def __init__(self):
        self.treasure = Treasure()

    def get_string(self):
        ret_string = self.treasure.get_string()
        return ret_string

    def print(self):
        print_string = self.get_string()
        print(print_string)


    def get_random_treasure(self):
        self.treasure = select_from_list(treasure_table)

    #The possibilities for category are Wondrous Item, Book, Weapon, Treasure, Armor, Ring
    #The possibilities for rarity are Mundane, Common, Uncommon, Rare, Very Rare, Legendary
    def get_filtered_treasure(self, category_filters=[], rarity_filters=[]):

        filtered_list1 = []
        filtered_list2 = []

        #Filter the catigory
        if len(category_filters) == 0:
            filtered_list1 = treasure_table

        else:
            for item in treasure_table:
                for filter in category_filters:
                    if item.category == filter:
                        filtered_list1.append(item)

        #Filter the rarity
        if len(rarity_filters) == 0:
            filtered_list2 = filtered_list1

        else:
            for item in filtered_list1:
                for filter in rarity_filters:
                    if item.rarity == filter:
                        filtered_list2.append(item)

        if len(filtered_list2) > 1:
            self.treasure = select_from_list(filtered_list2)

        else:
            self.treasure.name = "Filter too restrictive. No items in list"






if __name__ == "__main__":

    treasure1 = GeneratedTreasure()
    # treasure1.get_random_treasure()
    treasure1.get_filtered_treasure(["Book", "Ring"], ["Common"])
    treasure1.print()