INSERT INTO Users (username, password_hash) VALUES ('user1', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');
INSERT INTO Users (username, password_hash) VALUES ('user2', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');
INSERT INTO Users (username, password_hash) VALUES ('user3', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');
INSERT INTO Users (username, password_hash) VALUES ('user4', 'scrypt:32768:8:1$IUI6IDekdzOdezAT$2186fb11cdb0a7f945b90f2994541350deea6d7b78b72ecda11d5895c74b24368b6e3f3303f0f739fb326253cf803e3b9215e3c6acdc12ba815e06cf37110ebc');

INSERT INTO Posts (poster_id, title, language_name, category_name, description) VALUES (1, 'Implement a hw-level O(n) solution to the traveling salesman problem', 1, 1, 'Good luck');
INSERT INTO Posts (poster_id, title, language_name, category_name, description) VALUES (2, 'Optimized DOOM', 2, 2, 'Recreate doom in C++ in as few expressions as possible. Not lines, expressions.');
INSERT INTO Posts (poster_id, title, language_name, category_name, description) VALUES (3, 'The Worlds most important problem', 3, 3, 'Find out who asked.');
INSERT INTO Posts (poster_id, title, language_name, category_name, description) VALUES (4, 'Basic input', 4, 4, 'Get input from user without using the stdlib IO-monad.');

INSERT INTO LanguageFilters (language_name) VALUES ("C");
INSERT INTO LanguageFilters (language_name) VALUES ("C++");
INSERT INTO LanguageFilters (language_name) VALUES ("Python");
INSERT INTO LanguageFilters (language_name) VALUES ("Haskell");

INSERT INTO CategoryFilters (category_name) VALUES ("embedded");
INSERT INTO CategoryFilters (category_name) VALUES ("gamedev");
INSERT INTO CategoryFilters (category_name) VALUES ("algorithms");
INSERT INTO CategoryFilters (category_name) VALUES ("monads");

INSERT INTO Comments (commenter_id, post_id, content) VALUES (2, 1, 'Aint no way ts even possible son im crine :crying::peacesign:');
INSERT INTO Comments (commenter_id, post_id, content) VALUES (3, 2, '#include "d_main.h"\nint main(){\n    D_DoomMain();}');
INSERT INTO Comments (commenter_id, post_id, content) VALUES (4, 3, 'import asker\n\nprint(asker.who())');
INSERT INTO Comments (commenter_id, post_id, content) VALUES (1, 4, 'What is a monad?');
