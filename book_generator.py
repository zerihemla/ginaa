from lists.book_lists.general_book_titles import general_book_titles_list

from lists.general_adjectives.colors import color_list
from lists.general_adjectives.item_conditions import item_conditions

from custom_libs.helper_func import *

EMPTY_TEXT = "---"

class GeneratedBook():
    def __init__(self):
        self.book_title = EMPTY_TEXT
        self.book_color = EMPTY_TEXT
        self.book_condition = EMPTY_TEXT
    def clear(self):
        self.__init__()

    def setGeneralBook(self):
        self.book_color = select_from_list(color_list)
        self.book_condition = select_from_list(item_conditions)
        self.book_title = select_from_list(general_book_titles_list)
        # self.item_condition = select_from_list(item_conditions)
        # self.item = select_from_list(item_list)
        # self.item_adj = select_from_list(adjective_list)

    def get_text(self):
        text = ""
        if self.book_color != EMPTY_TEXT:
            text += ("Color: " + self.book_color + "\n")

        if self.book_condition != EMPTY_TEXT:
            text += ("Condition: " + self.book_condition + "\n")

        if self.book_title != EMPTY_TEXT:
            text += "Title: " + self.book_title + "\n"

        return text

    def print(self):
        text = self.get_text()
        print(text)
        print(DIVIDER_STARS)



if __name__ == "__main__":

    item = GeneratedBook()
    item.setGeneralBook()
    item.print()
