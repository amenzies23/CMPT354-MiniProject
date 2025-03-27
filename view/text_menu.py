#
# TextMenu class is responsible for displaying various menus of the library system. This class uses an array
# of MenuEntry objects to represent menu options and their corresponsing actions.
#
class TextMenu:
    #
    # MenuEntry is a utility class to bundle the name of the menu entry and corresponding action
    #
    class MenuEntry:
        def __init__(self, text, action):
            self.text = text
            self.action = action

    def __init__(self, title, entries):
        self.title = title
        self.entries = entries

    def display_menu(self):
        print(f"{self.title}")
        for i, entry in enumerate(self.entries, start=1):
            print(f"{i}. {entry.text}")










