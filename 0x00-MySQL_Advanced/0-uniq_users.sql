--  creates a table called users in the database
CREATE TABLE IF NOT EXIST `users` (
    `id` int NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `email` varchar(255) NOT NULL UNIQUE,
    `name` varchar(255)
);
