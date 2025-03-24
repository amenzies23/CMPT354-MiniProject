def display_message(message) -> None:
    print(message)

def display_error(error_message) -> None:
    print(error_message)

def get_user_input_int(prompt) -> int:
    return int(input(prompt))

def get_user_input(prompt) -> str:
    return input(prompt)

def display_items(items) -> None:
    print("---------------------------------")
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
    print()
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

def display_music(items) -> None:
    print()
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
    print()
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