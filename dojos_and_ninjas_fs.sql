SELECT * FROM dojos;

INSERT INTO dojos (name)
VALUES ('sneaky dojo'),('fast dojo'),('strong dojo');

-- DELETE FROM dojos
-- WHERE id IN = (1, 2, 3);

DELETE FROM dojos
WHERE id = 1;

DELETE FROM dojos
WHERE id = 2;

DELETE FROM dojos
WHERE id = 3;

INSERT INTO dojos (name)
VALUES ('quite dojo'),('swift dojo'),('swole dojo');

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Ajani', 'Goldmane', 50, 4), ('Jace', 'Beleren', 27, 4), ('Vraska', 'Snake', 35, 4);

SELECT * FROM ninjas;

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Swifty', 'McGee', 30, 5), ('Flash', 'The Sloth', 8, 5), ('Sonic', 'Hedgehog', 29, 5);

INSERT INTO ninjas (first_name, last_name, age, dojo_id)
VALUES ('Edward', 'Elric', 18, 6), ('Alphonse', 'Elric', 15, 6), ('Alex', 'Armstrong', 36, 6);

SELECT *
FROM ninjas
WHERE dojo_id = 4;

SELECT *
FROM ninjas
WHERE dojo_id = 6;

SELECT dojos.name
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 9;

SELECT * 
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id
WHERE ninjas.id = 6;

SELECT * 
FROM ninjas
JOIN dojos ON dojos.id = ninjas.dojo_id;

-- select = column
-- from which table
-- join (combining tables)
-- where (filtering) 