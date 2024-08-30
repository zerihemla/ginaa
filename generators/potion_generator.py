import sys
sys.path.append("../")

from lists.potion_lists.potion_label import label_list
from lists.potion_lists.potion_bottle import bottle_list
from lists.potion_lists.potion_taste_and_smell import taste_and_smell_list
from lists.potion_lists.potion_colors import color_list
from lists.potion_lists.potion_appearance import appearance_list
from lists.potion_lists.potion_strength import strength_list
from lists.potion_lists.potion_main_effect import main_effect_list
from lists.potion_lists.potion_side_effects import side_effect_list


from custom_libs.helper_func import *

class GeneratedPotion():
    def __init__(self):
        self.label = "---"
        self.bottle = "---"
        self.smell = "---"
        self.taste = "---"
        self.color = "---"
        self.appearance = "---"
        self.strength = "---"
        self.main_effect = "---"
        self.side_effect = "---"

    def generate_attributes(self, generate_side_effect:bool=True):
        self.label = select_from_list(label_list)
        self.bottle = select_from_list(bottle_list)
        self.smell = select_from_list(taste_and_smell_list)
        self.taste = select_from_list(taste_and_smell_list)
        self.color = select_from_list(color_list)
        self.appearance = select_from_list(appearance_list)
        self.strength = select_from_list(strength_list)
        self.main_effect = select_from_list(main_effect_list)

        if generate_side_effect:
            self.side_effect = select_from_list(side_effect_list)




    def print_attributes(self):
        text = self.get_text()
        print(text)
        print(DIVIDER_STARS)


    def get_text(self):
        text =  ("Label: " + self.label + "\n" +
        "Bottle: " + self.bottle + "\n" +
        "Color: " + self.color + "\n" +
        "Appearance: " + self.appearance + "\n\n"

        "Smell: " + self.smell + "\n" +
        "Taste: " + self.taste + "\n\n" +

        "Strength: " + self.strength + "\n" +
        "Effect: " + self.main_effect + "\n")

        if self.side_effect != "---":
            text += "Side Effect: " + self.side_effect + "\n"

        return text



if __name__ == "__main__":

    test_potion = GeneratedPotion()
    test_potion.generate_attributes()
    test_potion.print_attributes()
