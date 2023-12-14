DROP TABLE IF EXISTS accounts;

CREATE TABLE accounts (
    id INTEGER PRIMARY KEY,
    website TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL
);