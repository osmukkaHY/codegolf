CREATE TABLE Users (
    id            INTEGER PRIMARY KEY,
    username      TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE Posts (
    id          INTEGER PRIMARY KEY,
    poster_id   REFERENCES Users(id) NOT NULL,
    title       TEXT NOT NULL,
    description TEXT NOT NULL
);

