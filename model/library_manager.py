import sqlite3

class LibraryManager:
    def __init__(self):
        self.con = sqlite3.connect("library.db")
        self.cur = self.con.cursor()

    def find_user_id(self, uid) -> bool:
        res = self.cur.execute("SELECT user_id FROM User WHERE user_id = ?", (uid,))
        return res.fetchone() is not None
            
        




    

    

