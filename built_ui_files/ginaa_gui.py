# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ginaa_gui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ginaa_GUI(object):
    def setupUi(self, Ginaa_GUI):
        Ginaa_GUI.setObjectName("Ginaa_GUI")
        Ginaa_GUI.resize(931, 754)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Ginaa_GUI.sizePolicy().hasHeightForWidth())
        Ginaa_GUI.setSizePolicy(sizePolicy)
        self.centralwidget = QtWidgets.QWidget(Ginaa_GUI)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.main_frame = QtWidgets.QFrame(self.centralwidget)
        self.main_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_frame.setObjectName("main_frame")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.main_frame)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.main_sep_line = QtWidgets.QFrame(self.main_frame)
        self.main_sep_line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.main_sep_line.setLineWidth(2)
        self.main_sep_line.setFrameShape(QtWidgets.QFrame.VLine)
        self.main_sep_line.setObjectName("main_sep_line")
        self.gridLayout_4.addWidget(self.main_sep_line, 0, 1, 2, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.save_button = QtWidgets.QPushButton(self.main_frame)
        self.save_button.setObjectName("save_button")
        self.horizontalLayout.addWidget(self.save_button)
        self.clear_button = QtWidgets.QPushButton(self.main_frame)
        self.clear_button.setObjectName("clear_button")
        self.horizontalLayout.addWidget(self.clear_button)
        self.gridLayout_4.addLayout(self.horizontalLayout, 1, 2, 1, 1)
        self.main_text = QtWidgets.QTextEdit(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_text.sizePolicy().hasHeightForWidth())
        self.main_text.setSizePolicy(sizePolicy)
        self.main_text.setObjectName("main_text")
        self.gridLayout_4.addWidget(self.main_text, 0, 0, 2, 1)
        self.tabWidget = QtWidgets.QTabWidget(self.main_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setObjectName("tabWidget")
        self.peeps_and_paces_tab = QtWidgets.QWidget()
        self.peeps_and_paces_tab.setObjectName("peeps_and_paces_tab")
        self.gridLayout_16 = QtWidgets.QGridLayout(self.peeps_and_paces_tab)
        self.gridLayout_16.setObjectName("gridLayout_16")
        self.char_button_frame = QtWidgets.QFrame(self.peeps_and_paces_tab)
        self.char_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.char_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.char_button_frame.setObjectName("char_button_frame")
        self.gridLayout = QtWidgets.QGridLayout(self.char_button_frame)
        self.gridLayout.setObjectName("gridLayout")
        self.chaotic_char_box = QtWidgets.QCheckBox(self.char_button_frame)
        self.chaotic_char_box.setObjectName("chaotic_char_box")
        self.gridLayout.addWidget(self.chaotic_char_box, 2, 0, 1, 1)
        self.character_type_box = QtWidgets.QComboBox(self.char_button_frame)
        self.character_type_box.setObjectName("character_type_box")
        self.character_type_box.addItem("")
        self.character_type_box.addItem("")
        self.character_type_box.addItem("")
        self.character_type_box.addItem("")
        self.character_type_box.addItem("")
        self.gridLayout.addWidget(self.character_type_box, 3, 0, 1, 1)
        self.characters_line = QtWidgets.QFrame(self.char_button_frame)
        self.characters_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.characters_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.characters_line.setObjectName("characters_line")
        self.gridLayout.addWidget(self.characters_line, 1, 0, 1, 1)
        self.generate_char_button = QtWidgets.QPushButton(self.char_button_frame)
        self.generate_char_button.setObjectName("generate_char_button")
        self.gridLayout.addWidget(self.generate_char_button, 4, 0, 1, 1)
        self.character_labels = QtWidgets.QLabel(self.char_button_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.character_labels.setFont(font)
        self.character_labels.setObjectName("character_labels")
        self.gridLayout.addWidget(self.character_labels, 0, 0, 1, 1)
        self.gridLayout_16.addWidget(self.char_button_frame, 0, 0, 1, 1)
        self.taverns_button_frame = QtWidgets.QFrame(self.peeps_and_paces_tab)
        self.taverns_button_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.taverns_button_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.taverns_button_frame.setObjectName("taverns_button_frame")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.taverns_button_frame)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.tavern_label = QtWidgets.QLabel(self.taverns_button_frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tavern_label.setFont(font)
        self.tavern_label.setObjectName("tavern_label")
        self.gridLayout_2.addWidget(self.tavern_label, 0, 0, 1, 1)
        self.tavern_line = QtWidgets.QFrame(self.taverns_button_frame)
        self.tavern_line.setFrameShape(QtWidgets.QFrame.HLine)
        self.tavern_line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.tavern_line.setObjectName("tavern_line")
        self.gridLayout_2.addWidget(self.tavern_line, 1, 0, 1, 1)
        self.generate_tavern_button = QtWidgets.QPushButton(self.taverns_button_frame)
        self.generate_tavern_button.setObjectName("generate_tavern_button")
        self.gridLayout_2.addWidget(self.generate_tavern_button, 2, 0, 1, 1)
        self.gridLayout_16.addWidget(self.taverns_button_frame, 1, 0, 1, 1)
        self.frame_7 = QtWidgets.QFrame(self.peeps_and_paces_tab)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.gridLayout_15 = QtWidgets.QGridLayout(self.frame_7)
        self.gridLayout_15.setObjectName("gridLayout_15")
        self.wild_magic_label = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.wild_magic_label.setFont(font)
        self.wild_magic_label.setObjectName("wild_magic_label")
        self.gridLayout_15.addWidget(self.wild_magic_label, 0, 0, 1, 1)
        self.line_7 = QtWidgets.QFrame(self.frame_7)
        self.line_7.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_7.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_7.setObjectName("line_7")
        self.gridLayout_15.addWidget(self.line_7, 1, 0, 1, 1)
        self.wild_magic_button = QtWidgets.QPushButton(self.frame_7)
        self.wild_magic_button.setObjectName("wild_magic_button")
        self.gridLayout_15.addWidget(self.wild_magic_button, 2, 0, 1, 1)
        self.gridLayout_16.addWidget(self.frame_7, 2, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 301, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_16.addItem(spacerItem, 3, 0, 1, 1)
        self.tabWidget.addTab(self.peeps_and_paces_tab, "")
        self.items_tab = QtWidgets.QWidget()
        self.items_tab.setObjectName("items_tab")
        self.gridLayout_20 = QtWidgets.QGridLayout(self.items_tab)
        self.gridLayout_20.setObjectName("gridLayout_20")
        self.frame_2 = QtWidgets.QFrame(self.items_tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.frame_2)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.gridLayout_6.addWidget(self.label_2, 0, 0, 1, 1)
        self.line_2 = QtWidgets.QFrame(self.frame_2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 1, 0, 1, 1)
        self.random_potion_button = QtWidgets.QPushButton(self.frame_2)
        self.random_potion_button.setFlat(False)
        self.random_potion_button.setObjectName("random_potion_button")
        self.gridLayout_6.addWidget(self.random_potion_button, 3, 0, 1, 1)
        self.include_side_effects_box = QtWidgets.QCheckBox(self.frame_2)
        self.include_side_effects_box.setChecked(True)
        self.include_side_effects_box.setObjectName("include_side_effects_box")
        self.gridLayout_6.addWidget(self.include_side_effects_box, 2, 0, 1, 1)
        self.gridLayout_20.addWidget(self.frame_2, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.items_tab)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.gridLayout_3.addWidget(self.line, 1, 0, 1, 1)
        self.random_item_button = QtWidgets.QPushButton(self.frame)
        self.random_item_button.setObjectName("random_item_button")
        self.gridLayout_3.addWidget(self.random_item_button, 2, 0, 1, 1)
        self.random_magic_item_button = QtWidgets.QPushButton(self.frame)
        self.random_magic_item_button.setObjectName("random_magic_item_button")
        self.gridLayout_3.addWidget(self.random_magic_item_button, 3, 0, 1, 1)
        self.random_corrupted_item_button = QtWidgets.QPushButton(self.frame)
        self.random_corrupted_item_button.setObjectName("random_corrupted_item_button")
        self.gridLayout_3.addWidget(self.random_corrupted_item_button, 4, 0, 1, 1)
        self.gridLayout_20.addWidget(self.frame, 0, 0, 1, 1)
        self.frame_8 = QtWidgets.QFrame(self.items_tab)
        self.frame_8.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_8.setObjectName("frame_8")
        self.gridLayout_19 = QtWidgets.QGridLayout(self.frame_8)
        self.gridLayout_19.setObjectName("gridLayout_19")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.num_treasure_box = QtWidgets.QSpinBox(self.frame_8)
        self.num_treasure_box.setMinimum(1)
        self.num_treasure_box.setMaximum(10)
        self.num_treasure_box.setObjectName("num_treasure_box")
        self.horizontalLayout_2.addWidget(self.num_treasure_box)
        self.generate_treasure_button = QtWidgets.QPushButton(self.frame_8)
        self.generate_treasure_button.setObjectName("generate_treasure_button")
        self.horizontalLayout_2.addWidget(self.generate_treasure_button)
        self.gridLayout_19.addLayout(self.horizontalLayout_2, 7, 0, 1, 1)
        self.gridLayout_17 = QtWidgets.QGridLayout()
        self.gridLayout_17.setObjectName("gridLayout_17")
        self.mundane_box = QtWidgets.QCheckBox(self.frame_8)
        self.mundane_box.setChecked(False)
        self.mundane_box.setObjectName("mundane_box")
        self.gridLayout_17.addWidget(self.mundane_box, 0, 0, 1, 1)
        self.common_box = QtWidgets.QCheckBox(self.frame_8)
        self.common_box.setChecked(False)
        self.common_box.setObjectName("common_box")
        self.gridLayout_17.addWidget(self.common_box, 0, 1, 1, 1)
        self.uncommon_box = QtWidgets.QCheckBox(self.frame_8)
        self.uncommon_box.setChecked(False)
        self.uncommon_box.setObjectName("uncommon_box")
        self.gridLayout_17.addWidget(self.uncommon_box, 1, 0, 1, 1)
        self.rare_box = QtWidgets.QCheckBox(self.frame_8)
        self.rare_box.setObjectName("rare_box")
        self.gridLayout_17.addWidget(self.rare_box, 1, 1, 1, 1)
        self.very_rare_box = QtWidgets.QCheckBox(self.frame_8)
        self.very_rare_box.setObjectName("very_rare_box")
        self.gridLayout_17.addWidget(self.very_rare_box, 2, 0, 1, 1)
        self.legendary_box = QtWidgets.QCheckBox(self.frame_8)
        self.legendary_box.setObjectName("legendary_box")
        self.gridLayout_17.addWidget(self.legendary_box, 2, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_17, 2, 0, 1, 1)
        self.line_9 = QtWidgets.QFrame(self.frame_8)
        self.line_9.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_9.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_9.setObjectName("line_9")
        self.gridLayout_19.addWidget(self.line_9, 3, 0, 1, 1)
        self.line_8 = QtWidgets.QFrame(self.frame_8)
        self.line_8.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_8.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_8.setObjectName("line_8")
        self.gridLayout_19.addWidget(self.line_8, 1, 0, 1, 1)
        self.treasure_labsl = QtWidgets.QLabel(self.frame_8)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.treasure_labsl.setFont(font)
        self.treasure_labsl.setObjectName("treasure_labsl")
        self.gridLayout_19.addWidget(self.treasure_labsl, 0, 0, 1, 1)
        self.gridLayout_18 = QtWidgets.QGridLayout()
        self.gridLayout_18.setObjectName("gridLayout_18")
        self.book_box = QtWidgets.QCheckBox(self.frame_8)
        self.book_box.setChecked(False)
        self.book_box.setObjectName("book_box")
        self.gridLayout_18.addWidget(self.book_box, 0, 0, 1, 1)
        self.weapon_box = QtWidgets.QCheckBox(self.frame_8)
        self.weapon_box.setChecked(False)
        self.weapon_box.setObjectName("weapon_box")
        self.gridLayout_18.addWidget(self.weapon_box, 0, 1, 1, 1)
        self.armor_box = QtWidgets.QCheckBox(self.frame_8)
        self.armor_box.setChecked(False)
        self.armor_box.setObjectName("armor_box")
        self.gridLayout_18.addWidget(self.armor_box, 1, 0, 1, 1)
        self.treasure_box = QtWidgets.QCheckBox(self.frame_8)
        self.treasure_box.setChecked(False)
        self.treasure_box.setObjectName("treasure_box")
        self.gridLayout_18.addWidget(self.treasure_box, 1, 1, 1, 1)
        self.ring_box = QtWidgets.QCheckBox(self.frame_8)
        self.ring_box.setChecked(False)
        self.ring_box.setObjectName("ring_box")
        self.gridLayout_18.addWidget(self.ring_box, 2, 0, 1, 1)
        self.wonderous_box = QtWidgets.QCheckBox(self.frame_8)
        self.wonderous_box.setChecked(False)
        self.wonderous_box.setObjectName("wonderous_box")
        self.gridLayout_18.addWidget(self.wonderous_box, 2, 1, 1, 1)
        self.gridLayout_19.addLayout(self.gridLayout_18, 4, 0, 1, 1)
        self.line_10 = QtWidgets.QFrame(self.frame_8)
        self.line_10.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_10.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_10.setObjectName("line_10")
        self.gridLayout_19.addWidget(self.line_10, 5, 0, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.frame_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_19.addWidget(self.label_7, 6, 0, 1, 1)
        self.gridLayout_20.addWidget(self.frame_8, 2, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 233, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_20.addItem(spacerItem1, 3, 0, 1, 1)
        self.tabWidget.addTab(self.items_tab, "")
        self.dungon_tab = QtWidgets.QWidget()
        self.dungon_tab.setObjectName("dungon_tab")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.dungon_tab)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.frame_3 = QtWidgets.QFrame(self.dungon_tab)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout_9 = QtWidgets.QGridLayout(self.frame_3)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.label_3 = QtWidgets.QLabel(self.frame_3)
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.gridLayout_9.addWidget(self.label_3, 0, 0, 1, 1)
        self.line_3 = QtWidgets.QFrame(self.frame_3)
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.gridLayout_9.addWidget(self.line_3, 1, 0, 1, 1)
        self.mechanical_trap_button = QtWidgets.QPushButton(self.frame_3)
        self.mechanical_trap_button.setObjectName("mechanical_trap_button")
        self.gridLayout_9.addWidget(self.mechanical_trap_button, 2, 0, 1, 1)
        self.magic_trap_button = QtWidgets.QPushButton(self.frame_3)
        self.magic_trap_button.setObjectName("magic_trap_button")
        self.gridLayout_9.addWidget(self.magic_trap_button, 3, 0, 1, 1)
        self.chaotic_trap_button = QtWidgets.QPushButton(self.frame_3)
        self.chaotic_trap_button.setObjectName("chaotic_trap_button")
        self.gridLayout_9.addWidget(self.chaotic_trap_button, 4, 0, 1, 1)
        self.gridLayout_10.addWidget(self.frame_3, 0, 0, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 352, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout_10.addItem(spacerItem2, 1, 0, 1, 1)
        self.tabWidget.addTab(self.dungon_tab, "")
        self.gridLayout_4.addWidget(self.tabWidget, 0, 2, 1, 1)
        self.gridLayout_5.addWidget(self.main_frame, 0, 0, 1, 1)
        Ginaa_GUI.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ginaa_GUI)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 931, 22))
        self.menubar.setObjectName("menubar")
        Ginaa_GUI.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ginaa_GUI)
        self.statusbar.setObjectName("statusbar")
        Ginaa_GUI.setStatusBar(self.statusbar)

        self.retranslateUi(Ginaa_GUI)
        self.tabWidget.setCurrentIndex(1)
        self.character_type_box.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(Ginaa_GUI)

    def retranslateUi(self, Ginaa_GUI):
        _translate = QtCore.QCoreApplication.translate
        Ginaa_GUI.setWindowTitle(_translate("Ginaa_GUI", "MainWindow"))
        self.save_button.setText(_translate("Ginaa_GUI", "Save"))
        self.clear_button.setText(_translate("Ginaa_GUI", "Clear"))
        self.chaotic_char_box.setText(_translate("Ginaa_GUI", "Chaotic Char"))
        self.character_type_box.setItemText(0, _translate("Ginaa_GUI", "General"))
        self.character_type_box.setItemText(1, _translate("Ginaa_GUI", "Small Town"))
        self.character_type_box.setItemText(2, _translate("Ginaa_GUI", "Outskirts"))
        self.character_type_box.setItemText(3, _translate("Ginaa_GUI", "Underdark"))
        self.character_type_box.setItemText(4, _translate("Ginaa_GUI", "Any"))
        self.generate_char_button.setText(_translate("Ginaa_GUI", "Generate Character"))
        self.character_labels.setText(_translate("Ginaa_GUI", "Characters"))
        self.tavern_label.setText(_translate("Ginaa_GUI", "Taverns"))
        self.generate_tavern_button.setText(_translate("Ginaa_GUI", "Generate Tavern"))
        self.wild_magic_label.setText(_translate("Ginaa_GUI", "Wild Magic"))
        self.wild_magic_button.setText(_translate("Ginaa_GUI", "Gen WIld Magic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.peeps_and_paces_tab), _translate("Ginaa_GUI", "Peeps&&Places"))
        self.label_2.setText(_translate("Ginaa_GUI", "Potions"))
        self.random_potion_button.setText(_translate("Ginaa_GUI", "Random Potion"))
        self.include_side_effects_box.setText(_translate("Ginaa_GUI", "Include SIe Effects"))
        self.label.setText(_translate("Ginaa_GUI", "Items"))
        self.random_item_button.setText(_translate("Ginaa_GUI", "Random Item"))
        self.random_magic_item_button.setText(_translate("Ginaa_GUI", "Random Magic"))
        self.random_corrupted_item_button.setText(_translate("Ginaa_GUI", "Random Corrupted"))
        self.generate_treasure_button.setText(_translate("Ginaa_GUI", "Gen. Treasure"))
        self.mundane_box.setText(_translate("Ginaa_GUI", "Mundane"))
        self.common_box.setText(_translate("Ginaa_GUI", "Common"))
        self.uncommon_box.setText(_translate("Ginaa_GUI", "Uncommon"))
        self.rare_box.setText(_translate("Ginaa_GUI", "Rare"))
        self.very_rare_box.setText(_translate("Ginaa_GUI", "Very Rare"))
        self.legendary_box.setText(_translate("Ginaa_GUI", "Legendary"))
        self.treasure_labsl.setText(_translate("Ginaa_GUI", "Treasure"))
        self.book_box.setText(_translate("Ginaa_GUI", "Book"))
        self.weapon_box.setText(_translate("Ginaa_GUI", "Weapon"))
        self.armor_box.setText(_translate("Ginaa_GUI", "Armor"))
        self.treasure_box.setText(_translate("Ginaa_GUI", "Treasure"))
        self.ring_box.setText(_translate("Ginaa_GUI", "Ring"))
        self.wonderous_box.setText(_translate("Ginaa_GUI", "Wonderous"))
        self.label_7.setText(_translate("Ginaa_GUI", "Num to Gen"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.items_tab), _translate("Ginaa_GUI", "Items"))
        self.label_3.setText(_translate("Ginaa_GUI", "Traps"))
        self.mechanical_trap_button.setText(_translate("Ginaa_GUI", "Mechanical"))
        self.magic_trap_button.setText(_translate("Ginaa_GUI", "Magic"))
        self.chaotic_trap_button.setText(_translate("Ginaa_GUI", "Chaotic"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.dungon_tab), _translate("Ginaa_GUI", "Dungon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Ginaa_GUI = QtWidgets.QMainWindow()
    ui = Ui_Ginaa_GUI()
    ui.setupUi(Ginaa_GUI)
    Ginaa_GUI.show()
    sys.exit(app.exec_())
