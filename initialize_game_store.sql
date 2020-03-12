/* Create tables */


/* Entity tables */
CREATE TABLE customer (
	customer_id	integer primary key,
	first_name	varchar(20) not null,
	last_name	varchar(20) not null,
	address		varchar(40),
	city		varchar(20),
	zipcode		varchar(20)
);

CREATE TABLE online_order (
	order_id	integer primary key,
	cost		float(4)
);

CREATE TABLE game (
	game_id		integer primary key,
	game_title	varchar(30) not null,
	price		float(4) not null,
	game_genre	varchar(20)
);

CREATE TABLE locale (
	locale_id	integer primary key,
	city		varchar(20) not null,
	address		varchar(20),
	zipcode		integer
);

CREATE TABLE employee (
	employee_id	integer primary key,
	salary		float(4),
	first_name	varchar(20) not null,
	last_name	varchar(20) not null
);

CREATE TABLE manager (
	specialization	varchar(25),
	employee_id	integer primary key,
        foreign key(employee_id) references employee
);

CREATE TABLE cashier (
	register_id	integer,
	employee_id	integer primary key,
	foreign key(employee_id) references employee
);


/* Relationship tables */

CREATE TABLE places (
	order_id	integer primary key,	-- Primary Key
	customer_id	integer,		-- Foreign Key
	order_date	date,
	foreign key(customer_id) references customer,
	foreign key(order_id) references online_order
);

CREATE TABLE purchases (
	customer_id	integer,	-- Primary Key
	game_id		integer,	-- Primary Key
	purchase_date	date,
	locale_id	integer,
	primary key (customer_id, game_id),
	foreign key(locale_id) references locale,
	foreign key(customer_id) references customer,
	foreign key(game_id) references game
);

CREATE TABLE has_items (
	order_id	integer, -- Primary Key
	game_id		integer,  -- Primary Key
	primary key(order_id, game_id),
	foreign key(order_id) references online_order,
	foreign key(game_id) references game
);

CREATE TABLE holds_items (
	locale_id	integer,	-- Primary Key
	game_id		integer,	-- Primary Key
	quantity	integer,
	primary key(locale_id, game_id)
	foreign key(locale_id) references locale,
	foreign key(game_id) references game
);

CREATE TABLE works_at (
	employee_id	integer primary key,	-- Primary Key
	locale_id	integer,
	foreign key(locale_id) references locale,
	foreign key(employee_id) references employee
);

CREATE TABLE sale (
        start_date      date,		-- Primary Key
        end_date        date,		-- Primary Key
        discount        float(4),		-- Discount in dollars
        game_id         integer,		-- Primary Key
	primary key(start_date, end_date, discount, game_id),
	foreign key(game_id) references game
);

/* Insert dummy data */

INSERT INTO customer(
	customer_id, first_name, last_name, address, city, zipcode)
        VALUES (5555, 'John', 'Jack', '1211 S Apple St', 'Omaha', '68022');

INSERT INTO online_order(
	order_id, cost)
	VALUES (1212, 20.20);
INSERT INTO game (
	game_id, game_title, price, game_genre)
	VALUES (3333, 'Outlast', 00.01, 'Horror');

INSERT INTO locale (
	locale_id, city, address, zipcode)
	VALUES (2322, 'Omaha', '1111 S Orange Road', '22222');

INSERT INTO employee (
	employee_id, salary, first_name, last_name)
	VALUES (3331, 220.22, 'Lisa', 'Smith'),
	(3332, 400.00, 'Mike', 'Smith');

INSERT INTO manager (
	specialization, employee_id)
	VALUES ('retro games', 3332);

INSERT INTO cashier (
	register_id, employee_id)
	VALUES (2323, 3331);

INSERT INTO places (
	order_id, customer_id, order_date)
	VALUES (1212, 5555, '2020-02-26');

INSERT INTO purchases (
	customer_id, game_id, purchase_date, locale_id)
	VALUES (5555, 3333, '2020-02-26', 2322);

INSERT INTO has_items (
	order_id, game_id)
	VALUES (1212, 3333);

INSERT INTO holds_items (
	locale_id, game_id, quantity)
	VALUES (2322, 3333, 2);

INSERT INTO works_at (
	employee_id, locale_id)
	VALUES (3331, 2322);

INSERT INTO sale (
	start_date, end_date, discount, game_id)
	VALUES ('2020-02-26', '2020-02-26', 20.20, 3333),
	('2020-03-06', '2020-03-07', 10.50, 3590),
	('2020-01-06', '2020-01-07', 5.00, 3595),
	('2020-01-25', '2020-01-18', 10.00, 3599);
/*Copy over data */
\copy customer FROM './data/names_out.tsv' WITH NULL AS '-'
