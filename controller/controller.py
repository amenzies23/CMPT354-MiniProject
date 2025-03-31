from view.text_menu import TextMenu
from view.text_ui import *

#
# Controller class allows for communication between the model and view. It is responsible
# for initialzing the menues, receiving user input and sending to the database.
#
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
                TextMenu.MenuEntry("Request Event Recommendations", self.request_recommendation),
                TextMenu.MenuEntry("Volunteering Opportunities", self.volunteer),
                TextMenu.MenuEntry("Ask a librarian for help", self.librarian_help),
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
                display_message("")

                if self.library_manager.find_user_id(user_id):
                    self.set_user_id(user_id)
                    to_repeat = False
                else:
                    display_error(f"Error: Invalid User Id.\n")
            except ValueError:
                    display_error(f"Error: Invalid User Id.\n")

    def get_selection(self, max_value, menu) -> int:
        while True:
            try:
                selection = get_user_input_int(f"Enter [1-{max_value}]: ")
                display_message("")

                if 1 <= selection <= max_value:
                    return selection
                menu.display_menu()
                display_error(f"Error: Enter a number between 1 and {max_value}.\n")
            except ValueError:
                menu.display_menu()
                display_error(f"Error: Invalid input.\n")

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
        selected_action = find_entries[option - 1].action

        if selected_action:
            selected_action()

    def find_title(self) -> None:
        title = get_user_input("Enter title of item: ")
        display_message("")
        items = self.library_manager.find_item(title)
        if len(items) == 0:
            display_message("No Items Found.\n")
        else:
            display_message(f"Number of Items Found: {len(items)}\n")
            display_items(items)

    def find_author(self) -> None:
        author = get_user_input("Enter author's name: ")
        display_message("")
        items = self.library_manager.find_author(author)
        if len(items) == 0:
            display_message("No Items Found.\n")
        else:
            display_message(f"Number of Items Found: {len(items)}\n")
            display_readings(items)

    def find_artist(self) -> None:
        artist = get_user_input("Enter artist's name: ")
        display_message("")
        items = self.library_manager.find_artist(artist)
        if len(items) == 0:
            display_message("No Items Found.\n")
        else:
            display_message(f"Number of Items Found: {len(items)}\n")
            display_music(items)

    def find_genre(self) -> None:
        genre = get_user_input("Enter genre: ")
        display_message("")
        items = self.library_manager.find_genre(genre)
        if len(items) == 0:
            display_message("No Items Found.\n")
        else:
            display_message(f"Number of Items Found: {len(items)}\n")
            display_items(items)

    def borrow_item(self) -> None:
        try:
            item_id = get_user_input_int("Type Item ID to Borrow (-1 to Cancel): ")
            display_message("")
            if item_id == -1:
                return
            elif not self.library_manager.borrow_item(self.user_id, item_id):
                display_message("No Item Found.\n")
            else:
                display_message(f"Item {item_id} successfully borrowed\n")
        except ValueError:
            display_error(f"Error: Invalid Input.\n")

    
    def return_item(self) -> None:
        items = self.library_manager.get_all_borrowed_items(self.user_id)
        if len(items) == 0:
            display_message("No Items Found.\n")
        else:
            display_borrowed_items(items)
            self.update_item_status()
    
    def update_item_status(self) -> None:
        try:
            item_id = get_user_input_int("Type Item ID to Return (-1 to Cancel): ")
            display_message("")
            if item_id == -1:
                return
            elif not self.library_manager.return_item(self.user_id, item_id):
                display_message("Not a Valid Item.\n")
            else:
                display_message(f"Item {item_id} successfully returned\n")
        except ValueError:
            display_error(f"Error: Invalid Input.\n")
        return

    def get_item_categories(self, type_of_item) -> str:
        item_categories = None
        if type_of_item == "Reading":
            item_categories = [
                    TextMenu.MenuEntry("Book", self.return_string("Book")),
                    TextMenu.MenuEntry("Journal", self.return_string("Journal")),
                    TextMenu.MenuEntry("Online Book", self.return_string("Online Book")),
                    TextMenu.MenuEntry("Magazine", self.return_string("Magainze")),
                ]
        else:
            item_categories = [
                    TextMenu.MenuEntry("CD", self.return_string("CD")),
                    TextMenu.MenuEntry("Vinyl", self.return_string("Vinyl"))
                ]


        item_category_menu = TextMenu("Select Item Category", item_categories)
        item_category_menu.display_menu()
        option = self.get_selection(len(item_categories), item_category_menu)
        return item_categories[option - 1].action


    def return_string(self, item_category) -> str:
        return item_category

    def donate_item(self) -> None:
        while True:
            type_of_item = get_user_input("Donate Reading or Music (-1 to Cancel): ")
            if type_of_item == "-1":
                return
            elif type_of_item in {"Reading", "Music"}:
                title = get_user_input("Provide Title: ")
                category = self.get_item_categories(type_of_item)
                genre = get_user_input("Provide Genre: ")
                publisher_name = get_user_input("Provide Publisher Name: ")
                isbn = ""
                num_songs = 0
                author = ""
                artist = ""


                if type_of_item == "Reading":
                    author = get_user_input("Provide Author: ")
                    while True:
                        isbn = get_user_input("Provide isbn (13 digits): ")
                        if len(isbn) == 13 and isbn.isdigit():
                            break
                        display_error(f"Error: Invalid Input.\n")
                elif type_of_item == "Music":
                    artist = get_user_input("Provide Artist: ")
                    while True:
                        try:
                            num_songs = get_user_input_int("Provide Number of Songs: ")
                            break
                        except ValueError:
                            display_error(f"Error: Invalid Input.\n")
                self.library_manager.donate_item(type_of_item, title, artist, author, isbn, num_songs, category, genre, publisher_name)
                display_message(f"Item successfully donated\n")
                break
            else:
                display_error(f"Error: Invalid Input.\n")

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
        display_message("Volunteering Opportunities\n")
        display_message("We are always looking for volunteers to help with our events and programs.")
        display_message("Please confirm here if you would like to volunteer with the lirbary:")
        decision = get_user_input("Type 'yes' to volunteer or 'no' to exit: ")
        # Making the user type yes as a way to confirm their decision, but we also need to check for existing user in employee table
        if decision == "yes":
            result = self.library_manager.register_volunteer(self.user_id)
            if result:
                display_message("Thank you for volunteering with us!\n"
                "A librarian will reach out to you shortly with more information on how to proceed.\n")
            else:
                display_error("\nError: Could not register as volunteer.\n"
                "Please come see a librarian for more information.\n")

        elif decision == "no":
            display_message("Thank you for considering volunteering with us.")
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
    
    def librarian_help(self) -> None:
        help_entries = [
            TextMenu.MenuEntry("How to use this system", self.cli_instructions),
            TextMenu.MenuEntry("Library hours and information", self.library_info),
            TextMenu.MenuEntry("Contact a librarian", self.contact_librarian),
            TextMenu.MenuEntry("Return to main menu", self.main_menu.display_menu)
        ]
    
        help_menu = TextMenu("Librarian Help Menu", help_entries)
        help_menu.display_menu()
        option = self.get_selection(len(help_entries), help_menu)
        help_entries[option - 1].action()
        
    def cli_instructions(self) -> None:
        display_cli_instructions()
        return_to_menu = [
            TextMenu.MenuEntry("Return to help menu", self.librarian_help),
            TextMenu.MenuEntry("Return to main menu", self.main_menu.display_menu)
        ]
        return_menu = TextMenu("Library Info Menu", return_to_menu)
        return_menu.display_menu()

        option = self.get_selection(len(return_to_menu), return_menu)
        return_to_menu[option - 1].action()

    def library_info(self) -> None:
        library_data = self.library_manager.get_library_info()
        if not library_data:
            display_error("Error: Library information not available in database.")
            return
        
        display_library_info(library_data)

        return_to_menu = [
            TextMenu.MenuEntry("Return to help menu", self.librarian_help),
            TextMenu.MenuEntry("Return to main menu", self.main_menu.display_menu)
        ]
        return_menu = TextMenu("Library Info Menu", return_to_menu)
        return_menu.display_menu()

        option = self.get_selection(len(return_to_menu), return_menu)
        return_to_menu[option - 1].action()

    def contact_librarian(self) -> None:
        display_message("Contact a librarian\n")
        display_message("\nPlease leave your message and contact information below,"
        "\nand a librarian will get back to you as soon as possible.")
        # For now, since we dont have any functionality for a librarian to reach back out, this is going nowhere.
        while True:
            email = get_user_input("\nYour email address: ").strip()
            if "@" in email and "." in email:  # Very basic email check
                break
            display_error("\nPlease enter a valid email address (example@domain.com)")
        message = get_user_input("\nEnter your message: ")
        display_message("\nThank you for your message!\n")
        display_message("A librarian will reach out to you shortly!\n")
        return_to_menu = [
            TextMenu.MenuEntry("Return to help menu", self.librarian_help),
            TextMenu.MenuEntry("Return to main menu", self.main_menu.display_menu)
        ]
        return_menu = TextMenu("Please return to the main menu or help menu", return_to_menu)
        return_menu.display_menu()

        option = self.get_selection(len(return_to_menu), return_menu)
        return_to_menu[option - 1].action()

        return

    def exit_menu(self) -> None:
        exit()










                



        
        
