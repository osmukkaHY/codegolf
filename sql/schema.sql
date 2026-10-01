CREATE TABLE Users (
    id            INTEGER PRIMARY KEY,
    username      TEXT UNIQUE NOT NULL,
    password_hash TEXT NOT NULL
);

CREATE TABLE Posts (
    id          INTEGER PRIMARY KEY,
    poster_id   REFERENCES Users(id) NOT NULL,
    title       TEXT NOT NULL,
    language_name TEXT REFERENCES LanguageFilters(id),
    category_name TEXT REFERENCES CategoryFilters(id),
    description TEXT NOT NULL
);

CREATE TABLE LanguageFilters (
    id INTEGER PRIMARY KEY,
    language_name TEXT
);

CREATE TABLE CategoryFilters (
    id INTEGER PRIMARY KEY,
    category_name TEXT
);
