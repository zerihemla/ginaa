from lists.item_lists.items import item_list
from lists.item_lists.item_adjectives import adjective_list

from custom_libs.helper_func import *

class GeneratedItem():
    def __init__(self):
        self.item = "---"
        self.item_adj = "---"

    def setRandomItem(self):

        self.item = select_from_list(item_list)
        self.item_adj = select_from_list(adjective_list)

    def get_text(self):
        text = ""
        if self.item_adj != "---":
            text += ("Adj: " + self.item_adj + "\n")

        if self.item != "---":
            text += "Item: " + self.item + "\n"

        return text


    def print_item(self):
        text = self.get_text()

        print(text)
        print(DIVIDER_STARS)


if __name__ == "__main__":

    item = GeneratedItem()
    item.setRandomItem()
    item.print_item()