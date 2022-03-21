-- CREATE TABLE actors(
-- actor_id SERIAL PRIMARY KEY,
-- first_name VARCHAR (50) NOT NULL,
-- last_name VARCHAR (100) NOT NULL,
-- age DATE NOT NULL,
-- number_oscars SMALLINT NOT NULL);
	
-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Matt','Damon','08/10/1970', 5);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('George','Clooney','06/05/1961', 2);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Emily','Blunt','23/02/1983', 3);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Katic','Stana','26/04/1978', 1);

-- INSERT INTO actors(first_name, last_name, age, number_oscars)
-- VALUES('Nathan','Fillion','27/04/1971', 1), ('Meghan','Markle','27/05/1981', 2), ('Albus','Wulfric Brian','27/04/1971', 5);
	
	
-- SELECT COUNT(*) FROM actors;

-- INSERT INTO actors(first_name, last_name, number_oscars)
-- VALUES('Gandalf','The gray', 1000);
-- ERROR:  null value in column "age" of relation "actors" violates not-null constraint. 
-- because we specified that this column cannot be Null we got an ERROR.



