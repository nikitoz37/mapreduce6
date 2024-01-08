
CREATE USER admin1 WITH PASSWORD '123';
CREATE DATABASE top_words_db;
GRANT ALL PRIVILEGES ON DATABASE top_words_db TO admin1;

CREATE TABLE IF NOT EXISTS "Top_words"
(
	"id" serial NOT NULL PRIMARY KEY,
	"name" varchar NOT NUll UNIQUE,
	"num" integer
);



