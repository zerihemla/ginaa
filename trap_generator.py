from lists.trap_lists.trap_mechanical_trap import mechanical_trap_list
from lists.trap_lists.trap_mechanical_tell import mechanical_tell_list
from lists.trap_lists.trap_mechanical_source import mechanical_source_list

from lists.trap_lists.trap_magic_trap import magic_trap_list
from lists.trap_lists.trap_magic_tell import magic_tell_list
from lists.trap_lists.trap_magic_source import magic_source_list

from custom_libs.helper_func import *


class GeneratedTrap():
    def __init__(self):
        self.source = "---"
        self.tell = "---"
        self.trap = "---"

    def generate_mechanical_trap(self):
        self.source = select_from_list(mechanical_source_list)
        self.trap = select_from_list(mechanical_trap_list)
        self.tell = select_from_list(mechanical_tell_list)

    def generate_magical_trap(self):
        self.source = select_from_list(magic_source_list)
        self.trap = select_from_list(magic_trap_list)
        self.tell = select_from_list(magic_tell_list)

    def generate_chaotic_trap(self):
        is_magic_source = random.randint(0,1)
        is_magic_trap = random.randint(0,1)
        is_magic_tell = random.randint(0,1)

        if is_magic_source:
            self.source = select_from_list(magic_source_list)
        else:
            self.source = select_from_list(mechanical_source_list)

        if is_magic_trap:
            self.trap = select_from_list(magic_trap_list)
        else:
            self.trap = select_from_list(mechanical_trap_list)


        if is_magic_tell:
            self.tell = select_from_list(magic_tell_list)
        else:
            self.tell = select_from_list(mechanical_tell_list)

    def print_attributes(self):
        text = self.get_text()
        print(text)
        print(DIVIDER_STARS)

    def get_text(self):
        text = ("Source: " + self.source + "\n" +
                "Tell: " + self.tell + "\n" +
                "Trap: " + self.trap + "\n")
        return text


if __name__ == "__main__":
    trap = GeneratedTrap()
    trap.generate_chaotic_trap()
    trap.print_attributes()