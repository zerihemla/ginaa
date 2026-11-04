from lists.item_lists.items import item_list
from lists.item_lists.item_adjectives import adjective_list

from lists.item_lists.bad_item_list import bad_item_list
from lists.item_lists.useless_items import useless_item_list

from lists.general_adjectives.item_conditions import item_conditions

from custom_libs.helper_func import *

EMPTY_TEXT = "---"

class GeneratedItem():
    def __init__(self):
        self.item = EMPTY_TEXT
        self.item_adj = EMPTY_TEXT
        self.item_condition = EMPTY_TEXT
    def clear(self):
        self.__init__()

    def setRandomItem(self):
        self.item_condition = select_from_list(item_conditions)
        self.item = select_from_list(item_list)
        self.item_adj = select_from_list(adjective_list)

    def getUselessItem(self):
        self.item = select_from_list(useless_item_list)

    def getBadItem(self):
        self.item = select_from_list(bad_item_list)

    def get_text(self):
        text = ""
        if self.item_adj != EMPTY_TEXT:
            text += ("Adj: " + self.item_adj + "\n")

        if self.item_condition != EMPTY_TEXT:
            text += ("Condition: " + self.item_condition + "\n")

        if self.item != EMPTY_TEXT:
            text += "Item: " + self.item + "\n"

        return text

    def print(self):
        text = self.get_text()

        print(text)
        print(DIVIDER_STARS)



if __name__ == "__main__":

    item = GeneratedItem()
    item.setRandomItem()
    item.print()

    item .clear()
    item.getUselessItem()
    item.print()

    item.clear()
    item.getBadItem()
    item.print()