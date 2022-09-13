import random

from lists.tavern_names1 import tavern1_list
from lists.tavern_names2 import tavern2_list
from lists.tavern_feel import tavern_feel_list
from lists.tavern_look import tavern_look_list

DIVIDER_STARS = "*************************************************"

def get_rand_index(list_size:int):
    return random.randint(0, (list_size-1))

def select_from_list(this_list:list):
    list_len = len(this_list)
    sel_index = get_rand_index(list_len)
    sel_item = this_list[sel_index]
    return sel_item

class GeneratedTavern():
    def __init__(self):
        self.name1 = "---"
        self.name2 = "---"
        self.feel = "---"
        self.decor = "---"

    def setRandomAttributes(self):
        self.name1 = select_from_list(tavern1_list)
        self.name2 = select_from_list(tavern2_list)
        self.feel = select_from_list(tavern_feel_list)
        self.decor = select_from_list(tavern_look_list)

    def get_text(self):
        text = ("Name: " + self.name1 + " " + self.name2 + "\n" +
              "Feel: " + self.feel+ "\n\n"
              "Decor: " + self.decor)
        return text

    def print_attributes(self):
        text = self.get_text()
        print(text)
        print(DIVIDER_STARS)




if __name__ == "__main__":

    tavern = GeneratedTavern()
    tavern.setRandomAttributes()
    tavern.print_attributes()