--lists all cities contained on the database.
SELECT cities.id, cities.name , states.name
FROM hbtn_0d_usa
INNER JOIN cities
ON states states.id = cities.states_id
ORDER BY cities.id ASC;
