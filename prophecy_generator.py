from lists.prophecy_lists.adjective import adjective_list
from lists.prophecy_lists.noun import noun_list
from lists.prophecy_lists.verb import verb_list
from lists.prophecy_lists.prophecy_form import form_list

from custom_libs.helper_func import *

MAX_NUM_RANDOM_THINGS = 10

class Prophecy():
    def __init__(self):
        pass

        self.print_string = ""
        self.selected_string_form = ""
        self.local_noun_list = []
        self.local_adjective_list = []
        self.local_verb_list = []

        for i in range(MAX_NUM_RANDOM_THINGS):
            self.local_noun_list.append(select_from_list(noun_list))
            self.local_adjective_list.append(select_from_list(adjective_list))
            self.local_verb_list.append(select_from_list(verb_list))


        self.selected_string_form = select_from_list(form_list)
        self.print_string = (f"The {self.local_adjective_list[0]} {self.local_noun_list[0]} {self.local_verb_list[0]}\
                             while the {self.local_adjective_list[1]} {self.local_noun_list[1]} {self.local_verb_list[1]}")
        
        self.populate_string()

    def populate_string(self):
        self.print_string = self.selected_string_form

        for i in range(MAX_NUM_RANDOM_THINGS):
            self.print_string = self.print_string.replace(f"V{i}", self.local_verb_list[i])
            self.print_string = self.print_string.replace(f"N{i}", self.local_noun_list[i])
            self.print_string = self.print_string.replace(f"A{i}", self.local_adjective_list[i])


    def print(self):
        print(self.selected_string_form)
        print(self.print_string)



if __name__ == "__main__":
    prophecy = Prophecy()
    prophecy.print()