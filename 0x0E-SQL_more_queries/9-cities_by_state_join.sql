--lists all cities contained on the database.
SELECT cities.id, cities.name , states.name
FROM hbtn_0d_usa.cities
INNER JOIN hbtn_0d_usa.states
ON cities.states_id = states.id
ORDER BY cities.id ASC;
