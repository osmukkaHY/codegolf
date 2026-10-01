INSERT INTO Users (username, password_hash) VALUES ('user1', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');
INSERT INTO Users (username, password_hash) VALUES ('user2', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');
INSERT INTO Users (username, password_hash) VALUES ('user3', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');
INSERT INTO Users (username, password_hash) VALUES ('user4', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');

INSERT INTO Posts (poster_id, title, language_name, description) VALUES (1, 'post1', 1, 'this is a post');
INSERT INTO Posts (poster_id, title, language_name, description) VALUES (2, 'post2', 2, 'this is a post');
INSERT INTO Posts (poster_id, title, language_name, description) VALUES (3, 'post3', 3, 'this is a post');
INSERT INTO Posts (poster_id, title, language_name, description) VALUES (4, 'post4', 4, 'this is a post');

INSERT INTO Filters (language_name) VALUES ("C");
INSERT INTO Filters (language_name) VALUES ("C++");
INSERT INTO Filters (language_name) VALUES ("Python");
INSERT INTO Filters (language_name) VALUES ("Haskell");
