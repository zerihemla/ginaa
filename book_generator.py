from lists.book_lists.general_book_titles import general_book_titles_list
from lists.book_lists.evil_wizard_book_titles import evil_wizard_book_title_list
from lists.book_lists.general_evil_book_titles import general_evil_book_titles_list
from lists.book_lists.general_funny_book_titles import general_funny_book_titles_list

from lists.general_adjectives.colors import color_list
from lists.general_adjectives.item_conditions import item_conditions
from lists.general_adjectives.smells import smells_list

from custom_libs.helper_func import *

import random

EMPTY_TEXT = "---"

book_list_dictionary = {}
book_list_dictionary["general_book_titles"] = general_book_titles_list
book_list_dictionary["general_evil_book_titles"] = general_evil_book_titles_list
book_list_dictionary["general_funny_book_titles"] = general_funny_book_titles_list
book_list_dictionary["evil_wizard_book_titles"] = evil_wizard_book_title_list

class GeneratedBook():
    def __init__(self):
        self.book_title = EMPTY_TEXT
        self.book_color = EMPTY_TEXT
        self.book_smell = EMPTY_TEXT
        self.book_condition = EMPTY_TEXT
    def clear(self):
        self.__init__()


    def set_book_from_random_catigories(self, catigory_list):
        #If the list has stuff in it.
        if catigory_list:
            num_catigories = len(catigory_list)
            selected_catigory_index = random.randint(0, num_catigories-1)
            selected_catigory = catigory_list[selected_catigory_index]
            self.set_book_from_list_name(selected_catigory)


    def set_book_from_list_name(self, list_name):
        self.book_color = select_from_list(color_list)
        self.book_condition = select_from_list(item_conditions)
        self.book_smell = select_from_list(smells_list)

        selected_list = book_list_dictionary[list_name]
        self.book_title = select_from_list(selected_list)
        # self.item_condition = select_from_list(item_conditions)
        # self.item = select_from_list(item_list)
        # self.item_adj = select_from_list(adjective_list)

    def get_text(self):
        text = ""
        if self.book_color != EMPTY_TEXT:
            text += ("Color: " + self.book_color + "\n")

        if self.book_condition != EMPTY_TEXT:
            text += ("Condition: " + self.book_condition + "\n")

        if self.book_smell != EMPTY_TEXT:
            text += ("Smell: " + self.book_smell + "\n")

        if self.book_title != EMPTY_TEXT:
            text += "\nTitle: " + self.book_title + "\n"

        return text

    def print(self):
        text = self.get_text()
        print(text)
        print(DIVIDER_STARS)



if __name__ == "__main__":

    item = GeneratedBook()
    item.setGeneralBook()
    item.print()
