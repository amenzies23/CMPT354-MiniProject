import sqlite3

class LibraryManager:
    def __init__(self):
        self.con = sqlite3.connect("../library.db")
        print("library.db connected")

    

    

