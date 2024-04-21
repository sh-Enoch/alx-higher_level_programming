--lists all cities contained on the database.
SELECT cities.id, cities.name , states.name
FROM hbtn_0d_usa.cities
INNER JOIN hbtn_0d_usa.states
ON cities.state_id = states.id
ORDER BY hbtn_0d_usa.cities.id ASC;
