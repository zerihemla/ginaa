from lists.npc_lists.first_names import first_list
from lists.npc_lists.last_names import last_list
from lists.npc_lists.races import race_list
from lists.npc_lists.ages import age_list
from lists.npc_lists.description import description_list
from lists.npc_lists.wants_and_needs import wants_list
from lists.npc_lists.secret_or_obstacle import secret_list
from lists.npc_lists.carrying import carrying_list

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

    def setRandomAttributes(self):
        self.first_name = select_from_list(first_list)
        self.last_name = select_from_list(last_list)
        self.race = select_from_list(race_list)
        self.age = select_from_list(age_list)
        self.description = select_from_list(description_list)
        self.wants_and_needs = select_from_list(wants_list)
        self.secret_or_obstacle = select_from_list(secret_list)
        self.carrying = select_from_list(carrying_list)

    def setStoryAttributes(self):
        list_len = 160 #This will only create characters from the NPC and Random Encounters books.
        sel_index = get_rand_index(list_len)

        # print("Stable Selection Num: " + str(sel_index))

        self.first_name = first_list[sel_index]
        self.last_name = last_list[sel_index]
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
              "Desc: " + self.description + "\n" +
              "Wants: " + self.wants_and_needs + "\n\n" +
              "Secret: " + self.secret_or_obstacle + "\n" +
              "Carrying: " + self.carrying)
        return text



if __name__ == "__main__":

    selection = input("Caotic Selection? (y/N)")

    npc = GeneratedNPC()

    if  ("y" or "Y") in selection:
        num_variations = len(first_list) * len(last_list) * len(race_list) * len(age_list) * len(
            description_list) * len(wants_list) * len(secret_list) * len(carrying_list)

        print("\nNum Possible Variations: " + str(num_variations))

        npc.setRandomAttributes()

    else:
        # num_first = len(first_list)
        # num_last = len(last_list)
        # num_desc = len(description_list)
        # num_wants = len(wants_list)
        # num_secrets = len(secret_list)
        # num_carrying = len(carrying_list)
        #
        # print("Num First: " + str(num_first))
        # print("Num Last: " + str(num_last))
        # print("Num Desc: " + str(num_desc))
        # print("Num Wants: " + str(num_wants))
        # print("Num Secrets: " + str(num_secrets))
        # print("Num Carrying: " + str(num_carrying) + "\n\n")

        npc.setStoryAttributes()



    npc.print_attributes()

    # i = 1
    # for name in first_list:
    #     print(str(i) + ": " + name)
    #     i += 1


