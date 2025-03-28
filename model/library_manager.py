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

    def borrow_item(self, user_id, item_id) -> bool:
        # Ensure item exists or available
        query = "SELECT * FROM Item WHERE item_id = ? AND status LIKE 'Available'"
        self.cur.execute(query, (item_id,))
        if not self.cur.fetchone():
            return False

        query = "INSERT INTO Borrows (user_id, item_id) VALUES (?, ?)"
        self.cur.execute(query, (user_id, item_id))

        query = "UPDATE Item SET status = 'Not available' WHERE item_id = ?"
        self.cur.execute(query, (item_id,))
        self.con.commit()

        return True

    def get_all_borrowed_items(self, user_id) -> list:
        query = """
            SELECT i.item_id, title, borrow_date, due_date
            FROM Borrows b INNER JOIN Item i ON b.item_id = i.item_id
            WHERE user_id = ? AND status LIKE 'Not available' AND return_date IS NULL
            """
        self.cur.execute(query, (user_id,))

        return self.cur.fetchall()

    def return_item(self, user_id, item_id ) -> bool:
        query = "SELECT * FROM Item WHERE item_id = ? AND status LIKE 'Not available'"
        self.cur.execute(query, (item_id,))
        if not self.cur.fetchone():
            return False

        query = "UPDATE Borrows SET return_date = datetime('now', 'localtime') WHERE item_id = ? AND user_id = ?"
        self.cur.execute(query, (item_id, user_id))

        query = "UPDATE Item SET status = 'Available' WHERE item_id = ?"
        self.cur.execute(query, (item_id,))
        self.con.commit()

        return True

    def donate_item(self, type_of_item, title, artist, author, isbn, num_songs, category, genre, publisher_name) -> None:
        # find the category id
        query = "SELECT category_id FROM ItemCategory WHERE category_name = ?"
        self.cur.execute(query, (category,))
        category = self.cur.fetchone()
        category_id = None

        if category:
            category_id = category[0]
        else:
            query = "INSERT INTO ItemCategory (category_name) VALUES (?)"
            self.cur.execute(query, (category,))
            category_id = self.cur.lastrowid
        
        query = "INSERT INTO Item (category_id, library_name, address, title, status, genre, publisher_name) VALUES (?, 'Burnaby Public Library', '7311 Kingsway', ?, 'To Be Added', ?, ?)"

        self.cur.execute(query, (category_id, title, genre, publisher_name))

        item_id = self.cur.lastrowid

        if type_of_item == "Reading":
            query = "INSERT INTO Reading (item_id, isbn, author) VALUES (?, ?, ?)"
            self.cur.execute(query, (item_id, isbn, author))
        elif type_of_item == "Music":
            query = "INSERT INTO Music (item_id, artist, num_songs) VALUES (?, ?, ?)"
            self.cur.execute(query, (item_id, artist, num_songs))
        self.con.commit()


    def get_recommended_events(self, user_id) -> list:
        query = """
            SELECT E.* 
            FROM Events E
            JOIN RecommendedFor R ON E.event_id = R.event_id
            JOIN Audience A ON R.audience_id = A.audience_id
            WHERE A.audience_id = (
                SELECT audience_id 
                FROM BelongsTo 
                WHERE user_id = ?
            )
            """
        self.cur.execute(query, (user_id,))
        return self.cur.fetchall()

    def get_all_events(self) -> list:
        query = "SELECT * FROM Events"
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def register_user_for_event(self, user_id, event_id) -> bool:
        # Ensure the event exists
        event_query = "SELECT 1 FROM Events WHERE event_id = ?"
        self.cur.execute(event_query, (event_id,))
        if not self.cur.fetchone():
            self.con.commit()
            return False
        
        # Check if the user has already registered for the event
        attending_query = "SELECT 1 FROM Attending WHERE user_id = ? AND event_id = ?"
        self.cur.execute(attending_query, (user_id, event_id))
        if self.cur.fetchone():
            self.con.commit()
            return False
        
        # Register the user for the event
        insert_query = "INSERT INTO Attending (user_id, event_id) VALUES (?, ?)"
        self.cur.execute(insert_query, (user_id, event_id))
        self.con.commit()
        return True
    
    def get_library_info(self) -> list:
        query = "SELECT * FROM Library"
        self.cur.execute(query)
        return self.cur.fetchall()
        
    def register_volunteer(self, user_id) -> bool:
        check_query = "SELECT 1 FROM Employee WHERE user_id = ?"
        self.cur.execute(check_query, (user_id,))
        if self.cur.fetchone():
            return False # Means user already exists in Employee table
        # If we get here, register new volunteer
        insert_query =    """INSERT INTO Employee (user_id, salary, job_title)
                          VALUES (?, 0, 'Volunteer')
                          """
        self.cur.execute(insert_query, (user_id,))
        self.con.commit()
        return True
