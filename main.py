from controller.controller import Controller
from model.library_manager import LibraryManager

if __name__ == "__main__":
    library_manager = LibraryManager() 
    controller = Controller(library_manager)

    controller.start()

