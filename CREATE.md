- not sure if we need any foreign key constraint actions
- trigger needs to be added for user favourite_genre
- look to add check constraints


CREATE TABLE Library (
    library_name TEXT,
    address TEXT, 
    phone_number TEXT,
    email TEXT,
    PRIMARY KEY (library_name, address)
);

CREATE TABLE Item (
    item_id INTEGER PRIMARY KEY,
    category_id INTEGER,
    library_name TEXT,
    address TEXT,
    title TEXT,
    status TEXT,
    genre TEXT,
    location TEXT,
    publisher_name TEXT,
    FOREIGN KEY (category_id)
        REFERENCES ItemCategory (category_id)
    FOREIGN KEY (library_name)
        REFERENCES Library (library_name),
    FOREIGN KEY (address) 
        REFERENCES Library (address)
);

CREATE TABLE ItemCategory (
    category_id INTEGER PRIMARY KEY,
    category_name TEXT
);

CREATE TABLE Reading (
    item_id INTEGER PRIMARY KEY,
    isbn INTEGER,
    author TEXT,
    FOREIGN KEY (item_id)
        REFERENCES Item (item_id)
);

CREATE TABLE Music (
    item_id INTEGER PRIMARY KEY,
    artist TEXT,
    num_songs INTEGER,
    FOREIGN KEY (item_id)
        REFERENCES Item (item_id)
);

CREATE TABLE User (
    user_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    birthdate DATE NOT NULL,
    phone_number TEXT NOT NULL,
    address TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    member_since DATE DEFAULT (datetime('now', 'localtime')),
    favourite_genre TEXT
);

CREATE TABLE Employee (
    user_id INTEGER PRIMARY KEY,
    job_title TEXT,
    salary INTEGER
    FOREIGN KEY (user_id)
        REFERENCES User (user_id)
);

CREATE TABLE Events (
    event_id INTEGER PRIMARY KEY,
    library_name TEXT,
    address TEXT,
    room_number INTEGER,
    description TEXT,
    event_date DATE,
    start_time TEXT,
    end_time TEXT,
    FOREIGN KEY (library_name, address)
        REFERENCES Library (library_name, address)
);

CREATE TABLE Audience (
    audience_id INTEGER PRIMARY KEY,
    type TEXT,
    genre TEXT
);

CREATE TABLE Borrows (
    user_id INTEGER,
    item_id INTEGER,
    borrow_date DATE DEFAULT (datetime('now', 'localtime')),
    due_date DATE,
    return_date DATE,
    fine INTEGER,
    PRIMARY KEY (user_id, item_id, borrow_date),
    FOREIGN KEY (user_id)
        REFERENCES User (user_id),
    FOREIGN KEY (item_id)
        REFERENCES Item (item_id)
);

CREATE TABLE Attending (
    user_id INTEGER,
    event_id INTEGER,
    PRIMARY KEY (user_id, event_id),
    FOREIGN KEY (user_id)
        REFERENCES User (user_id),
    FOREIGN KEY (event_id)
        REFERENCES Events (event_id)
);

CREATE TABLE RecommendedFor (
    event_id INTEGER,
    audience_id INTEGER,
    PRIMARY KEY (event_id, audience_id),
    FOREIGN KEY (event_id)
        REFERENCES Events (event_id),
    FOREIGN KEY (audience_id)
        REFERENCES Audience (audience_id)
);

CREATE TABLE BelongsTo (
    user_id INTEGER,
    audience_id INTEGER,
    PRIMARY KEY (user_id, audience_id),
    FOREIGN KEY (user_id)
        REFERENCES User (user_id),
    FOREIGN KEY (audience_id)
        REFERENCES Audience (audience_id)
);





