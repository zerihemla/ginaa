from generators.npc_generator import GeneratedNPC
from generators.tavern_generator import GeneratedTavern
from generators.item_generator import GeneratedItem
from generators.potion_generator import GeneratedPotion
from generators.trap_generator import GeneratedTrap
from generators.treasure_generator import GeneratedTreasure
from generators.book_generator import GeneratedBook
from generators.prophecy_generator import Prophecy


from lists.occurrence_list.creepy_occurrences import creepy_occurrences_list
from lists.occurrence_list.random_occurrences import random_occurrences_list
from lists.encounter_lists.encounter_spice_list import encounter_spice_list


from wild_magic import get_wild_magic_effect


from custom_libs.helper_func import *

from PyQt5 import QtWidgets, uic

import os
import sys

# Load the Qt Designer file directly at runtime, so no pyuic5 build step is needed.
# When built with PyInstaller (build.py), bundled files are unpacked to sys._MEIPASS.
BASE_DIR = getattr(sys, "_MEIPASS", os.path.dirname(os.path.abspath(__file__)))
UI_FILE = os.path.join(BASE_DIR, "raw_ui_files", "ginaa_gui.ui")
Ui_Ginaa_GUI, _ = uic.loadUiType(UI_FILE)


class GinaaQtApp(Ui_Ginaa_GUI, QtWidgets.QMainWindow):
    def __init__(self):
        super(GinaaQtApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Ginaa    (Ginaa is not an acronym)")

        self.npc = GeneratedNPC()
        self.npc_text = ""
        self.tavern = GeneratedTavern()
        self.tavern_text = ""

        self.setup_buttons()

        QtWidgets.QApplication.setStyle("Fusion")

        self.tabWidget.setCurrentIndex(0)

    def setup_buttons(self):
        self.generate_char_button.clicked.connect(self.generate_npc_button_clicked)
        self.generate_tavern_button.clicked.connect(self.generate_tavern_button_clicked)

        self.clear_button.clicked.connect(self.clear_button_clicked)
        self.save_button.clicked.connect(self.save_button_clicked)

        self.random_item_button.clicked.connect(self.random_item_button_clicked)
        self.random_magic_item_button.clicked.connect(self.random_magic_item_button_clicked)
        self.random_corrupted_item_button.clicked.connect(self.random_corrupted_item_button_clicked)
        self.bad_item_button.clicked.connect(self.bad_item_button_clicked)
        self.useless_item_button.clicked.connect(self.useless_item_button_clicked)

        self.random_potion_button.clicked.connect(self.random_potion_button_clicked)

        self.generate_treasure_button.clicked.connect(self.generate_treasure_button_clicked)

        self.mechanical_trap_button.clicked.connect(self.random_mechanical_trap_button_clicked)
        self.magic_trap_button.clicked.connect(self.random_magical_trap_button_clicked)
        self.chaotic_trap_button.clicked.connect(self.random_chaotic_trap_button_clicked)


        self.creepy_occurrence_button.clicked.connect(self.creepy_occurrence_button_clicked)
        self.random_occurrence_button.clicked.connect(self.random_occurrence_button_clicked)
        self.combat_spices_button.clicked.connect(self.combat_spice_button_clicked)


        self.wild_magic_button.clicked.connect(self.wild_magic_button_clicked)
        self.prophecy_button.clicked.connect(self.prophecy_button_clicked)

        self.generate_book_button.clicked.connect(self.generate_book_button_clicked)

    #######################################
    ########NPC FUNCTIONS##################
    #######################################

    def generate_npc_button_clicked(self):

        type_index = self.character_type_box.currentIndex()
        # print(type_index)

        if self.chaotic_char_box.isChecked():
            self.npc.set_random_attributes(type_index)

        else:
            self.npc.set_story_attributes(type_index)

        self.npc_text = self.npc.get_text()
        self.print_to_console(self.npc_text)

    ##########################################
    #######TAVERN FUNCTIONS###################
    ##########################################

    def generate_tavern_button_clicked(self):
        self.tavern.setRandomAttributes()

        self.tavern_text = self.tavern.get_text()
        self.print_to_console(self.tavern_text)


    #######################################
    ####ITEM FUNCTIONS#####################
    #######################################
    def random_item_button_clicked(self):
        item = GeneratedItem()
        item.setRandomItem()
        text = item.get_text()
        self.print_to_console(text)

    def bad_item_button_clicked(self):
        item = GeneratedItem()
        item.getBadItem()
        text = item.get_text()
        self.print_to_console(text)


    def useless_item_button_clicked(self):
        item = GeneratedItem()
        item.getUselessItem()
        text = item.get_text()
        self.print_to_console(text)

    def random_magic_item_button_clicked(self):
        self.print_to_console("Random Magic Item Button is not yet functional\n")

    def random_corrupted_item_button_clicked(self):
        self.print_to_console("Random Corrupted Item Button is not yet functional\n")


    def random_potion_button_clicked(self):
        side_effect = self.include_side_effects_box.isChecked()
        potion = GeneratedPotion()
        potion.generate_attributes(side_effect)
        potion_text = potion.get_text()
        self.print_to_console(potion_text)


    def generate_treasure_button_clicked(self):
        rarity_list = []
        category_list = []
        if self.mundane_box.isChecked():
            rarity_list.append("Mundane")

        if self.common_box.isChecked():
            rarity_list.append("Common")

        if self.uncommon_box.isChecked():
            rarity_list.append("Uncommon")

        if self.rare_box.isChecked():
            rarity_list.append("Rare")

        if self.very_rare_box.isChecked():
            rarity_list.append("Very Rare")

        if self.legendary_box.isChecked():
            rarity_list.append("Legendary")


        if self.book_box.isChecked():
            category_list.append("Book")

        if self.weapon_box.isChecked():
            category_list.append("Weapon")

        if self.armor_box.isChecked():
            category_list.append("Armor")

        if self.treasure_box.isChecked():
            category_list.append("Treasure")

        if self.ring_box.isChecked():
            category_list.append("Ring")

        if self.wondrous_box.isChecked():
            category_list.append("Wondrous Item")

        if self.gear_box.isChecked():
            category_list.append("Adventuring Gear")

        if self.quest_hook_box.isChecked():
            category_list.append("Quest Hook")

        if self.potion_box.isChecked():
            category_list.append("Potion")


        num_items = self.num_treasure_box.value()

        for i in range(num_items):
            treasure = GeneratedTreasure()
            treasure.get_filtered_treasure(category_list, rarity_list)
            treasure_string = treasure.get_string()
            self.print_to_console(treasure_string)



    #######################################
    ####WILD MAGIC FUNCTIONS###############
    #######################################
    def wild_magic_button_clicked(self):
        wild_magic = "\n" + get_wild_magic_effect() + "\n"
        self.print_to_console(wild_magic)

    #######################################
    ####PROPHECY FUNCTIONS#################
    #######################################
    def prophecy_button_clicked(self):
        prophecy = Prophecy()
        prophecy_string = f"\n {prophecy.get_string()} \n"
        self.print_to_console(prophecy_string)

    #######################################
    ####BOOK FUNCTIONS#####################
    #######################################
    def generate_book_button_clicked(self):
        book = GeneratedBook()

        selected_category_list = []

        if self.funny_books_box.isChecked():
            selected_category_list.append("general_funny_book_titles")

        if self.general_books_box.isChecked():
            selected_category_list.append("general_book_titles")

        if self.evil_books_box.isChecked():
            selected_category_list.append("general_evil_book_titles")

        if self.evil_wizard_books_box.isChecked():
            selected_category_list.append("evil_wizard_book_titles")

        book.set_book_from_random_categories(selected_category_list)
        text = book.get_text()
        self.print_to_console(text)


    #######################################
    ####TRAP FUNCTIONS#####################
    #######################################
    def random_mechanical_trap_button_clicked(self):
        trap = GeneratedTrap()
        trap.generate_mechanical_trap()
        trap_text = trap.get_text()
        self.print_to_console(trap_text)

    def random_magical_trap_button_clicked(self):
        trap = GeneratedTrap()
        trap.generate_magical_trap()
        trap_text = trap.get_text()
        self.print_to_console(trap_text)

    def random_chaotic_trap_button_clicked(self):
        trap = GeneratedTrap()
        trap.generate_chaotic_trap()
        trap_text = trap.get_text()
        self.print_to_console(trap_text)


    def creepy_occurrence_button_clicked(self):
        occurrence = select_from_list(creepy_occurrences_list)
        self.print_to_console(occurrence)

    def random_occurrence_button_clicked(self):
        occurrence = select_from_list(random_occurrences_list)
        self.print_to_console(occurrence)


    def combat_spice_button_clicked(self):
        combat_spice = select_from_list(encounter_spice_list)
        self.print_to_console(combat_spice)


    #######################################
    ######SYSTEM FUNCTIONS#################
    #######################################

    def print_to_console(self, print_string:str, print_stars:bool=True):
        self.main_text.append(print_string)

        if print_stars:
            self.main_text.append(DIVIDER_STARS)


    def clear_button_clicked(self):
        self.main_text.clear()

    def save_button_clicked(self):
        file_location, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Output",
                                                                 os.path.expanduser("~"),
                                                                 "Text Files (*.txt);;All Files (*)")

        if not file_location:
            return

        # Always save as .txt. splitext only strips the real extension, so
        # dots in folder names (e.g. C:/Users/first.last/) are left alone.
        file_location = os.path.splitext(file_location)[0] + ".txt"

        with open(file_location, "w", encoding="utf-8") as save_file:
            save_file.write(self.main_text.toPlainText())




if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    qt_app = GinaaQtApp()

    try:
        qt_app.show()
        ret = app.exec_()

        qt_app.close()
        sys.exit(ret)

    except Exception as e:
        qt_app.close()
        sys.exit()