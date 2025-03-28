def display_message(message) -> None:
    print(message)

def display_error(error_message) -> None:
    print(error_message)

def get_user_input_int(prompt) -> int:
    return int(input(prompt))

def get_user_input(prompt) -> str:
    return input(prompt)

def display_items(items) -> None:
    for item in items:
        if item[9] == None:
            message = (
                f"Item ID: {item[0]}\n"
                f"Title: {item[4]}\n"
                f"Artist: {item[13]}\n"
                f"Number Of Songs: {item[14]}\n"
                f"Status: {item[5]}\n"
                f"Genre: {item[6]}\n"
                f"Location: {item[7]}\n"
                f"Publisher Name: {item[8]}\n"
                f"Category Name: {item[15]}\n"
                f"---------------------------------\n"
            )
            display_message(message)
        if item[12] == None:
            message = (
                f"Item ID: {item[0]}\n"
                f"Title: {item[4]}\n"
                f"Author: {item[11]}\n"
                f"ISBN: {item[10]}\n"
                f"Status: {item[5]}\n"
                f"Genre: {item[6]}\n"
                f"Location: {item[7]}\n"
                f"Publisher Name: {item[8]}\n"
                f"Category Name: {item[15]}\n"
                f"---------------------------------\n"
            )
            display_message(message)

def display_readings(items) -> None:
    for item in items:
            message = (
                f"Item ID: {item[0]}\n"
                f"Title: {item[4]}\n"
                f"Author: {item[10]}\n"
                f"ISBN: {item[9]}\n"
                f"Status: {item[5]}\n"
                f"Genre: {item[6]}\n"
                f"Location: {item[7]}\n"
                f"Publisher Name: {item[8]}\n"
                f"Category Name: {item[11]}\n"
                f"---------------------------------\n"
            )
            display_message(message)

def display_borrowed_items(items) -> None:
    for item in items:
        message = (
            f"Item ID: {item[0]}\n"
            f"Title: {item[1]}\n"
            f"Borrow Date: {item[2]}\n"
            f"Due Date: {item[3]}\n"
            f"---------------------------------\n"
        )
        display_message(message)

def display_music(items) -> None:
    for item in items:
            message = (
                f"Item ID: {item[0]}\n"
                f"Title: {item[4]}\n"
                f"Artist: {item[9]}\n"
                f"Number Of Songs: {item[10]}\n"
                f"Status: {item[5]}\n"
                f"Genre: {item[6]}\n"
                f"Location: {item[7]}\n"
                f"Publisher Name: {item[8]}\n"
                f"Category Name: {item[11]}\n"
                f"---------------------------------\n"
            )
            display_message(message)
    
def display_events(events) -> None:
    for event in events:
        message = (
            f"Event ID: {event[0]}\n"
            f"Room Number: {event[3]}\n"
            f"Description: {event[4]}\n"
            f"Date: {event[5]}\n"
            f"Time: {event[6]} - {event[7]}\n"
            f"---------------------------------\n"
        )
        display_message(message)

def display_library_info(library_data) -> None:
    message = (
        f"\nLibrary Name: {library_data[0][0]}\n"
        f"Address: {library_data[0][1]}\n"
        f"Phone: {library_data[0][2]}\n"
        f"Email: {library_data[0][3]}\n"
        f"\nHours:\n"
        f"Monday-Friday: 9am - 9pm\n"
        f"Saturday: 10am - 6pm\n"
        f"Sunday: 12pm - 5pm\n"
        f"---------------------------------\n"
    )
    display_message(message)

def display_cli_instructions() -> None:
    instructions = (
        "Command Line Interface Instructions:\n"
        "1. Navigation:\n"
        "  - Use the numbers to select menu options\n"
        "  - Press Enter to confirm your selection\n"
        "2. Searching for Items:\n"
        "  - You can search by title, author, artist or genre\n"
        "3. Borrowing:\n"
        "  - You'll need the Item ID to borrow\n"
        "  - Find this through search first\n"
        "4. Need more help?\n"
        "  - Select other options from this menu\n"
    )
    display_message(instructions)

