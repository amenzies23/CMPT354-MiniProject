import sqlite3

class LibraryManager:
    def __init__(self):
        self.con = sqlite3.connect("library.db")
        self.cur = self.con.cursor()

    def find_user_id(self, uid) -> bool:
        query = ("SELECT user_id "
                 "FROM User WHERE user_id = ?")

        res = self.cur.execute(query, (uid,))
        return res.fetchone() is not None

    def find_item(self, title) -> list:
        query = ("SELECT * "
                 "FROM Item i "
                 "LEFT JOIN Reading r ON i.item_id = r.item_id "
                 "LEFT JOIN Music m ON i.item_id = m.item_id "
                 "NATURAL JOIN ItemCategory "
                 "WHERE title LIKE ?")
        res = self.cur.execute(query, ('%' + title + '%',))

        return res.fetchall()

    def find_author(self, author) -> list:
        query = ("SELECT * "
                 "FROM Item "
                 "NATURAL JOIN Reading "
                 "NATURAL JOIN ItemCategory "
                 "WHERE author LIKE ?")
        res = self.cur.execute(query, ('%' + author + '%',))

        return res.fetchall()

    def find_artist(self, artist) -> list:
        query = ("SELECT * "
                 "FROM Item "
                 "NATURAL JOIN Music "
                 "NATURAL JOIN ItemCategory "
                 "WHERE artist LIKE ?")
        res = self.cur.execute(query, ('%' + artist + '%',))

        return res.fetchall()

    def find_genre(self, genre) -> list:
        query = ("SELECT * "
                 "FROM Item i "
                 "LEFT JOIN Reading r ON i.item_id = r.item_id "
                 "LEFT JOIN Music m ON i.item_id = m.item_id "
                 "NATURAL JOIN ItemCategory "
                 "WHERE genre LIKE ?")
        res = self.cur.execute(query, ('%' + genre + '%',))

        return res.fetchall()




            
        




    

    

