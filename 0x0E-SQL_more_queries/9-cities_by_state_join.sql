-- Lists all cities contained on the database.
-- Order by city id
SELECT cities.id, cities.name , states.name
FROM cites
INNER JOIN states
ON cities.id = states.state_id
ORDER BY cities.id ASC;
