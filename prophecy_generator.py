from lists.prophecy_lists.adjective import adjective_list
from lists.prophecy_lists.noun import noun_list
from lists.prophecy_lists.verb import verb_list

from custom_libs.helper_func import *


class Prophecy():
    def __init__(self):
        pass

        self.print_string = ""
        self.local_noun_list = []
        self.local_adjective_list = []
        self.local_verb_list = []

        for i in range(3):
            self.local_noun_list.append(select_from_list(noun_list))
            self.local_adjective_list.append(select_from_list(adjective_list))
            self.local_verb_list.append(select_from_list(verb_list))

        self.print_string = (f"The {self.local_adjective_list[0]} {self.local_noun_list[0]} {self.local_verb_list[0]}\
                             while the {self.local_adjective_list[1]} {self.local_noun_list[1]} {self.local_verb_list[1]}")

    def print(self):
        print(self.print_string)



if __name__ == "__main__":
    prophecy = Prophecy()
    prophecy.print()