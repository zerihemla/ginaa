import sys
sys.path.append("../")

from lists.prophecy_lists.adjective import adjective_list
from lists.prophecy_lists.subjects import subject_list
from lists.prophecy_lists.verbs import verb_list
from lists.prophecy_lists.places import place_list
from lists.prophecy_lists.things import thing_list
from lists.prophecy_lists.nouns import noun_list
from lists.prophecy_lists.wepons import wepon_list
from lists.prophecy_lists.objects import object_list
from lists.prophecy_lists.good_adjective import good_adjective_list
from lists.prophecy_lists.bad_adjective import bad_adjective_list
from lists.prophecy_lists.prophecy_form import form_list



from custom_libs.helper_func import *

import re


class Prophecy():
    def __init__(self):
        pass

        self.print_string = ""
        self.selected_string_form = ""


        self.selected_string_form = select_from_list(form_list)   
        self.populate_string()

    def populate_string(self):
        self.print_string = self.selected_string_form

        highest_index = self._find_highest_number(self.selected_string_form)

        for i in range(highest_index, -1, -1):
            self.print_string = self.print_string.replace(f"P{i}", select_from_list(place_list))
            self.print_string = self.print_string.replace(f"S{i}", select_from_list(subject_list))
            self.print_string = self.print_string.replace(f"O{i}", select_from_list(object_list))
            self.print_string = self.print_string.replace(f"W{i}", select_from_list(wepon_list))
            self.print_string = self.print_string.replace(f"V{i}", select_from_list(verb_list))
            self.print_string = self.print_string.replace(f"G{i}", select_from_list(good_adjective_list))
            self.print_string = self.print_string.replace(f"B{i}", select_from_list(bad_adjective_list))
            self.print_string = self.print_string.replace(f"A{i}", select_from_list(adjective_list))
            self.print_string = self.print_string.replace(f"T{i}", select_from_list(thing_list))
            self.print_string = self.print_string.replace(f"N{i}", select_from_list(noun_list))


    def get_string(self):
        return self.print_string

    def print(self):
        print(self.selected_string_form)
        print(self.print_string)

    def _find_highest_number(self, string:str):
        # Find all sequences of digits in the string
        numbers = re.findall(r'\d+', string)

        # Convert the list of number strings to integers
        numbers = [int(num) for num in numbers]

        # Return the highest number
        if numbers:
            return max(numbers)        # Find all sequences of digits in the string
        numbers = re.findall(r'\d+', string)

        # Convert the list of number strings to integers
        numbers = [int(num) for num in numbers]

        # Return the highest number
        if numbers:
            return max(numbers)
        else:
            return 0  # No numbers found



if __name__ == "__main__":
    prophecy = Prophecy()
    prophecy.print()