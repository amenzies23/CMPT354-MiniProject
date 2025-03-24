from view.text_menu import TextMenu
from view.text_ui import *

class Controller:
    def __init__(self, library_manager) -> None:
        self.library_manager = library_manager
        self.user_id = None

        self.menu_entries = [
                TextMenu.MenuEntry("Find an Item", self.find_item),
                TextMenu.MenuEntry("Return an Item", self.return_item),
                TextMenu.MenuEntry("Donate an Item", self.donate_item),
                TextMenu.MenuEntry("Find an Event", self.find_event),
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
            option = self.get_selection(len(self.menu_entries), self.main_menu)
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

    def get_selection(self, max_value, menu) -> int:
        while True:
            try:
                selection = get_user_input_int(f"Enter [1-{max_value}]: ")

                if 1 <= selection <= max_value:
                    return selection
                menu.display_menu()
                display_error(f"Error: Enter a number between 1 and {max_value}.")
            except ValueError:
                menu.display_menu()
                display_error(f"Error: Invalid input.")

    def find_item(self) -> None:
        find_entries = [
                TextMenu.MenuEntry("Find by title", self.find_title),
                TextMenu.MenuEntry("Find by author", self.find_author),
                TextMenu.MenuEntry("Find by artist", self.find_artist),
                TextMenu.MenuEntry("Find by genre", self.find_genre),
                TextMenu.MenuEntry("Exit", None)
            ]
        
        find_menu = TextMenu("Find Item Menu", find_entries)
        find_menu.display_menu()
        option = self.get_selection(len(find_entries), find_menu)
        find_entries[option - 1].action()

        self.borrow_item()



    def find_title(self) -> None:
        title = get_user_input("Enter title of item: ")
        items = self.library_manager.find_item(title)
        if len(items) == 0:
            display_message("\nNo Items Found.")
        else:
            display_message(f"\nNumber of Items Found: {len(items)}")
            display_items(items)

    def find_author(self) -> None:
        author = get_user_input("Enter author's name: ")
        items = self.library_manager.find_author(author)
        if len(items) == 0:
            display_message("\nNo Items Found.")
        else:
            display_message(f"\nNumber of Items Found: {len(items)}")
            display_readings(items)

    def find_artist(self) -> None:
        artist = get_user_input("Enter artist's name: ")
        items = self.library_manager.find_artist(artist)
        if len(items) == 0:
            display_message("\nNo Items Found.")
        else:
            display_message(f"\nNumber of Items Found: {len(items)}")
            display_music(items)

    def find_genre(self) -> None:
        genre = get_user_input("Enter genre: ")
        items = self.library_manager.find_genre(genre)
        if len(items) == 0:
            display_message("\nNo Items Found.")
        else:
            display_message(f"\nNumber of Items Found: {len(items)}")
            display_items(items)

    def borrow_item(self) -> None:
        item_id = get_user_input_int("Type Item ID to Borrow: ")
        print(item_id)
        return
    
    def return_item(self) -> None:
        display_message("return_item")
        return

    def donate_item(self) -> None:
        display_message("donate_item")
        return

    def find_event(self) -> None:
        if self.user_id is None:
            display_error("Error: User ID not set.")
            return
        
        recommended_events = self.library_manager.get_recommended_events(self.user_id)
        if not recommended_events:
            display_message("No recommended events found.")
        else:
            display_message("Recommended Events for you:")
            display_events(recommended_events)
        event_entries = [
                TextMenu.MenuEntry("Register for an event", self.register_event),
                TextMenu.MenuEntry("View all events", self.view_all_events),
                TextMenu.MenuEntry("Exit to main menu", self.main_menu.display_menu),
        ]
        event_menu = TextMenu("Find Event Menu", event_entries)
        event_menu.display_menu()
        option = self.get_selection(len(event_entries), event_menu)
        event_entries[option - 1].action()

        return
    
    def view_all_events(self) -> None:
        # Fetch all events from the database
        all_events = self.library_manager.get_all_events()
        if not all_events:
            display_message("No events found.")
        else:
            display_message("All Events:")
            display_events(all_events)
            
        event_entries = [
                TextMenu.MenuEntry("Register for an event", self.register_event),
                TextMenu.MenuEntry("Exit to main menu", self.main_menu.display_menu),
        ]
        event_menu = TextMenu("View all events menu", event_entries)
        event_menu.display_menu()
        option = self.get_selection(len(event_entries), event_menu)
        event_entries[option - 1].action()

    def register_event(self) -> None:
        if self.user_id is None:
            display_error("Error: User ID not set.")
            return
        event_id = get_user_input_int("Enter the Event ID you want to register for: ")
        if self.library_manager.register_user_for_event(self.user_id, event_id):
            display_message("Successfully registered for the event.")
        else:
            display_error("Error: Could not register for the event.")
        return

    def volunteer(self) -> None:
        display_message("volunteer")
        return

    def request_recommendation(self) -> None:
        if self.user_id is None:
            display_error("Error: User ID not set.")
            return
        
        recommended_events = self.library_manager.get_recommended_events(self.user_id)
        if not recommended_events:
            display_message("No recommended events found.")
        else:
            display_message("Recommended Events for you:")
            display_events(recommended_events)
        return

    def exit_menu(self) -> None:
        exit()










                



        
        
