DROP TABLE IF EXISTS cards;
DROP TABLE IF EXISTS users;

create table users (
	user_id INT GENERATED ALWAYS AS IDENTITY,
	email VARCHAR(255),
	PRIMARY KEY(user_id)	
);

create table cards (
	card_id INT GENERATED ALWAYS AS IDENTITY,
	user_id INT,
	card_provider VARCHAR(255),
	card_number INT,
	card_pin INT,
	PRIMARY KEY(card_id),
	FOREIGN KEY(user_id) REFERENCES users(user_id)
);