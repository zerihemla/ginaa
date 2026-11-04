from lists.npc_lists.first_names import first_lists
from lists.npc_lists.last_names import last_lists
from lists.npc_lists.races import race_list
from lists.npc_lists.ages import age_list
from lists.npc_lists.description import description_lists
from lists.npc_lists.wants_and_needs import wants_lists
from lists.npc_lists.secret_or_obstacle import secret_lists
from lists.npc_lists.carrying import carrying_lists
from lists.npc_lists.quirks import quirk_list

from custom_libs.helper_func import *


class GeneratedNPC():
    def __init__(self):
        self.first_name = "---"
        self.last_name = "---"
        self.race = "---"
        self.age = "---"
        self.description = "---"
        self.wants_and_needs = "---"
        self.secret_or_obstacle = "---"
        self.carrying = "---"
        self.suggested_quirk = "---"

    def set_random_attributes(self, list_num):
        first_list = []
        last_list = []
        description_list = []
        wants_list = []
        secret_list = []
        carrying_list = []

        #Select from each list at random
        if list_num == 4:
            #Choose which of the lists we will pull each thing from
            first_list = select_from_list(first_lists)
            last_list = select_from_list(last_lists)
            description_list = select_from_list(description_lists)
            wants_list = select_from_list(wants_lists)
            secret_list = select_from_list(secret_lists)
            carrying_list = select_from_list(carrying_lists)

        #Set one list that we are selecting from
        else:
            first_list, last_list, description_list, wants_list, secret_list, carrying_list = self.get_lists(list_num)

        self.first_name = select_from_list_not_first(first_list)
        self.last_name = select_from_list_not_first(last_list)
        self.race = select_from_list(race_list)
        self.age = select_from_list(age_list)
        self.description = select_from_list_not_first(description_list)
        self.wants_and_needs = select_from_list_not_first(wants_list)
        self.secret_or_obstacle = select_from_list_not_first(secret_list)
        self.carrying = select_from_list_not_first(carrying_list)
        self.suggested_quirk = select_from_list(quirk_list)


    ##list num 0 is general
    ##list num 1 is small_town
    ##list num 2 is outskirts
    ##list num 3 is underdark
    ##list num 4 is any
    def get_lists(self, list_num):

        calc_list_num = list_num
        if list_num == 4:
            calc_list_num = get_rand_index(4)

        first_list = first_lists[calc_list_num]
        last_list = last_lists[calc_list_num]
        description_list = description_lists[calc_list_num]
        wants_list = wants_lists[calc_list_num]
        secret_list = secret_lists[calc_list_num]
        carrying_list = carrying_lists[calc_list_num]

        return first_list, last_list, description_list, wants_list, secret_list, carrying_list


    def set_story_attributes(self, list_num):
        first_list, last_list, description_list, wants_list, secret_list, carrying_list = self.get_lists(list_num)
        list_len = len(first_list)

        #This ensures we don't get index 0.
        #Index 0 is a label
        sel_index = get_rand_index(list_len -1 ) + 1

        self.first_name = first_list[sel_index]
        self.last_name = last_list[sel_index]
        self.suggested_quirk = select_from_list(quirk_list)
        self.description = description_list[sel_index]
        self.wants_and_needs = wants_list[sel_index]
        self.secret_or_obstacle = secret_list[sel_index]
        self.carrying = carrying_list[sel_index]

        #Age needs to be re-worked to interact with race somehow.
        self.age = select_from_list(age_list)
        self.race = select_from_list(race_list)


    def print_attributes(self):
        text = self.get_text()
        print(text)
        print(DIVIDER_STARS)

    def get_text(self):
        text = ("Name: " + self.first_name + " " + self.last_name + "\n" +
              "Sug. Race: " + self.race + "\n"
              "Sug. Age: " + self.age + "\n\n"

              "Possible Quirk: " + self.suggested_quirk + "\n" +
              "Desc: " + self.description + "\n" +

              "Wants: " + self.wants_and_needs + "\n\n" +
              "Secret: " + self.secret_or_obstacle + "\n" +
              "Carrying: " + self.carrying)
        return text



if __name__ == "__main__":

    selection = input("Chaotic Selection? (y/N)")

    npc = GeneratedNPC()

    if selection.lower().startswith("y"):
        npc.set_random_attributes(4)
    else:
        npc.set_story_attributes(4)

    npc.print_attributes()


