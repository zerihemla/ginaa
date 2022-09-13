from built_ui_files import ginaa_gui

from npc_generator import GeneratedNPC
from tavern_generator import GeneratedTavern

#These were copied straight from RCade
# from PyQt5 import QtCore
# from PyQt5 import QtSerialPort
from PyQt5 import QtWidgets
# from PyQt5.QtCore import QThreadPool, QTimer
# from PyQt5.QtGui import QColor
# from PyQt5.QtWidgets import QMessageBox, QDialog, QDialogButtonBox, QFormLayout, QLineEdit

import qdarktheme


import sys


DIVIDER_STARS = "*************************************************"


class GinaaQtApp(ginaa_gui.Ui_Ginaa_GUI, QtWidgets.QMainWindow):
    def __init__(self):
        super(GinaaQtApp, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Ginaa    (Ginaa is not an acronym)")

        self.npc = GeneratedNPC()
        self.npc_text = ""
        self.tavern = GeneratedTavern()
        self.tavern_text = ""

        self.setup_buttons()

        self.setStyleSheet(qdarktheme.load_stylesheet("light", "rounded"))

    def setup_buttons(self):
        self.generate_char_button.clicked.connect(self.generate_npc_button_clicked)
        self.generate_tavern_button.clicked.connect(self.generate_tavern_button_clicked)

        self.clear_button.clicked.connect(self.clear_button_clicked)
        self.save_button.clicked.connect(self.save_button_clicked)

        self.random_item_button.clicked.connect(self.random_item_button_clicked)
        self.random_magic_item_button.clicked.connect(self.random_magic_item_button_clicked)
        self.random_corrupted_item_button.clicked.connect(self.random_corrupted_item_button_clicked)

    #######################################
    ########NPC FUNCTIONS##################
    #######################################

    def generate_npc_button_clicked(self):

        if self.chaotic_char_box.isChecked():
            self.npc.setRandomAttributes()

        else:
            self.npc.setStoryAttributes()

        self.npc_text = self.npc.get_text()
        self.main_text.append(self.npc_text)
        self.main_text.append(DIVIDER_STARS)

    ##########################################
    #######TAVERN FUNCTIONS###################
    ##########################################

    def generate_tavern_button_clicked(self):
        self.tavern.setRandomAttributes()

        self.tavern_text = self.tavern.get_text()
        self.main_text.append(self.tavern_text)
        self.main_text.append(DIVIDER_STARS)


    #######################################
    ####ITEM FUNCTIONS#####################
    #######################################
    def random_item_button_clicked(self):
        self.main_text.append("Random Item Button is not yet functional\n")

    def random_magic_item_button_clicked(self):
        self.main_text.append("Random Magic Item Button is not yet functional\n")

    def random_corrupted_item_button_clicked(self):
        self.main_text.append("Random Corrupted Item Button is not yet functional\n")


    #######################################
    ######SYSTEM FUNCTIONS#################
    #######################################

    def clear_button_clicked(self):
        self.main_text.clear()

    def save_button_clicked(self):
        options = QtWidgets.QFileDialog.Options()
        # options |= QtWidgets.QFileDialog.DontUseNativeDialog
        file_location = QtWidgets.QFileDialog.getSaveFileName(self, "QFileDialog.getSaveFileName()",
                                                              "./local_test_data", "All Files (*);;Text Files (*.txt)",
                                                              options=options)

        file_location_string = str(file_location[0])

        if file_location_string == "":
            return

        file_location_string = file_location_string.split(".")[0]

        file_location_string += ".txt"

        console_sting = self.main_text.toPlainText()

        save_file = open(file_location_string, "w")
        save_file.write(console_sting)

        save_file.close()




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