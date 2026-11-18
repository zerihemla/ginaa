import random

from lists.book_lists.general_book_titles import general_book_titles_list
from lists.book_lists.evil_wizard_book_titles import evil_wizard_book_title_list
from lists.book_lists.general_evil_book_titles import general_evil_book_titles_list
from lists.book_lists.general_funny_book_titles import general_funny_book_titles_list
from lists.book_lists.childrens_book_titles import childrens_book_titles_list
from lists.book_lists.history_and_lore_book_titles import history_and_lore_book_titles_list
from lists.book_lists.romance_and_poetry_book_titles import romance_and_poetry_book_titles_list
from lists.book_lists.book_details import *

from lists.general_adjectives.colors import color_list
from lists.general_adjectives.item_conditions import item_conditions
from lists.general_adjectives.smells import smells_list

from custom_libs.helper_func import *

EMPTY_TEXT = "---"

#Chance (0 to 1) that a book has each optional detail, so not every book is strange.
ANONYMOUS_AUTHOR_CHANCE = 0.15
MARGINALIA_CHANCE = 0.5
TUCKED_INSIDE_CHANCE = 0.35
ODDITY_CHANCE = 0.2

book_list_dictionary = {}
book_list_dictionary["general_book_titles"] = general_book_titles_list
book_list_dictionary["general_evil_book_titles"] = general_evil_book_titles_list
book_list_dictionary["general_funny_book_titles"] = general_funny_book_titles_list
book_list_dictionary["evil_wizard_book_titles"] = evil_wizard_book_title_list
book_list_dictionary["childrens_book_titles"] = childrens_book_titles_list
book_list_dictionary["history_and_lore_book_titles"] = history_and_lore_book_titles_list
book_list_dictionary["romance_and_poetry_book_titles"] = romance_and_poetry_book_titles_list


def get_random_author():
    if random.random() < ANONYMOUS_AUTHOR_CHANCE:
        return select_from_list(book_anonymous_authors)

    return (select_from_list(book_author_titles)
            + select_from_list(book_author_first_names) + " "
            + select_from_list(book_author_last_names)
            + select_from_list(book_author_epithets))


def select_with_chance(this_list, chance):
    if random.random() < chance:
        return select_from_list(this_list)
    return EMPTY_TEXT


class GeneratedBook():
    def __init__(self):
        self.book_title = EMPTY_TEXT
        self.book_author = EMPTY_TEXT
        self.book_color = EMPTY_TEXT
        self.book_binding = EMPTY_TEXT
        self.book_size = EMPTY_TEXT
        self.book_condition = EMPTY_TEXT
        self.book_smell = EMPTY_TEXT
        self.book_language = EMPTY_TEXT
        self.book_accuracy = EMPTY_TEXT
        self.book_marginalia = EMPTY_TEXT
        self.book_tucked_inside = EMPTY_TEXT
        self.book_oddity = EMPTY_TEXT

    def clear(self):
        self.__init__()


    def set_book_from_random_categories(self, category_list):
        #No categories selected means any category.
        if not category_list:
            category_list = list(book_list_dictionary.keys())

        selected_category = select_from_list(category_list)
        self.set_book_from_list_name(selected_category)


    def set_book_from_list_name(self, list_name):
        selected_list = book_list_dictionary[list_name]
        self.book_title = select_from_list(selected_list)
        self.book_author = get_random_author()

        self.book_color = select_from_list(color_list)
        self.book_binding = select_from_list(book_bindings)
        self.book_size = select_from_list(book_sizes)
        self.book_condition = select_from_list(item_conditions)
        self.book_smell = select_from_list(smells_list)
        self.book_language = select_from_list(book_languages)
        self.book_accuracy = select_from_list(book_accuracy)

        self.book_marginalia = select_with_chance(book_marginalia, MARGINALIA_CHANCE)
        self.book_tucked_inside = select_with_chance(book_tucked_inside, TUCKED_INSIDE_CHANCE)
        self.book_oddity = select_with_chance(book_oddities, ODDITY_CHANCE)

    def get_text(self):
        text = ""
        if self.book_title != EMPTY_TEXT:
            text += "\nTitle: " + self.book_title + "\n"

        details = [
            ("Author", self.book_author),
            ("Color", self.book_color),
            ("Binding", self.book_binding),
            ("Size", self.book_size),
            ("Condition", self.book_condition),
            ("Smell", self.book_smell),
            ("Language", self.book_language),
            ("Accuracy", self.book_accuracy),
            ("Marginalia", self.book_marginalia),
            ("Tucked inside", self.book_tucked_inside),
            ("Oddity", self.book_oddity),
        ]

        for label, value in details:
            if value != EMPTY_TEXT:
                text += label + ": " + value + "\n"

        return text

    def print(self):
        text = self.get_text()
        print(text)
        print(DIVIDER_STARS)



if __name__ == "__main__":

    for i in range(3):
        book = GeneratedBook()
        book.set_book_from_random_categories([])
        book.print()
