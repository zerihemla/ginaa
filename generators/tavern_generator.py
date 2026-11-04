from lists.tavern_lists.tavern_names1 import tavern1_list
from lists.tavern_lists.tavern_names2 import tavern2_list
from lists.tavern_lists.tavern_feel import tavern_feel_list
from lists.tavern_lists.tavern_look import tavern_look_list

from custom_libs.helper_func import *


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