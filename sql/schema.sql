CREATE TABLE Users (
    id            INTEGER PRIMARY KEY,
    username      STRING UNIQUE,
    password_hash STRING
);
