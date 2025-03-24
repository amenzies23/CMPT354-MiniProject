import sqlite3

class LibraryManager:
    def __init__(self):
        self.con = sqlite3.connect("library.db")
        self.cur = self.con.cursor()

    def find_user_id(self, uid) -> bool:
        res = self.cur.execute("SELECT user_id FROM User WHERE user_id = ?", (uid,))
        return res.fetchone() is not None
    
    def get_recommended_events(self, user_id):
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

    def get_all_events(self):
        query = "SELECT * FROM Events"
        self.cur.execute(query)
        return self.cur.fetchall()
    
    def register_user_for_event(self, user_id, event_id):
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
        

