from view.text_menu import TextMenu
from view.text_ui import *

class Controller:
    def __init__(self, library_manager) -> None:
        self.library_manager = library_manager
        self.user_id = None

        self.menu_entries = [
                TextMenu.MenuEntry("Find an Item", self.find_item),
                TextMenu.MenuEntry("Borrow an Item", self.borrow_item),
                TextMenu.MenuEntry("Return an Item", self.return_item),
                TextMenu.MenuEntry("Donate an Item", self.donate_item),
                TextMenu.MenuEntry("Find an Event", self.find_event),
                TextMenu.MenuEntry("Register for an Event", self.register_event),
                TextMenu.MenuEntry("Volunteering Opportunities", self.volunteer),
                TextMenu.MenuEntry("Request For Recommendations", self.request_recommendation),
                TextMenu.MenuEntry("Exit", self.exit_menu)
            ]
        self.main_menu = TextMenu("Main Menu", self.menu_entries)

    def set_user_id(self, user_id) -> None:
        self.user_id = user_id

    def start(self) -> None:
        self.prompt_for_user_id()

        while True:
            self.main_menu.display_menu()
            option = self.get_selection(len(self.menu_entries))
            self.menu_entries[option - 1].action()

    def prompt_for_user_id(self) -> None:
        to_repeat = True
        while to_repeat:
            try:
                user_id = get_user_input_int("Enter your User ID: ")

                if self.library_manager.find_user_id(user_id):
                    self.set_user_id(user_id)
                    to_repeat = False
                else:
                    display_error(f"Error: Invalid User Id.")
            except ValueError:
                    display_error(f"Error: Invalid User Id.")
        

    def get_selection(self, max_value) -> int:
        while True:
            try:
                selection = get_user_input_int(f"Enter [1-{max_value}]: ")

                if 1 <= selection <= max_value:
                    return selection
                self.main_menu.display_menu()
                display_error(f"Error: Enter a number between 1 and {max_value}.")
            except ValueError:
                self.main_menu.display_menu()
                display_error(f"Error: Invalid input.")

    def find_item(self) -> None:
        display_message("find_item")
        return
    
    def borrow_item(self) -> None:
        display_message("borrow_item")
        return
    
    def return_item(self) -> None:
        display_message("return_item")
        return

    def donate_item(self) -> None:
        display_message("donate_item")
        return

    def find_event(self) -> None:
        display_message("find_event")
        return

    def register_event(self) -> None:
        display_message("register_event")
        return

    def volunteer(self) -> None:
        display_message("volunteer")
        return

    def request_recommendation(self) -> None:
        display_message("request_recommendation")
        return

    def exit_menu(self) -> None:
        exit()









                



        
        
