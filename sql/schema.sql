CREATE TABLE Users (
    id            INTEGER PRIMARY KEY,
    username      STRING UNIQUE,
    password_hash STRING
);

CREATE TABLE Posts (
    id INTEGER PRIMARY KEY,
    poster_id REFERENCES Users(id),
    title STRING
);

