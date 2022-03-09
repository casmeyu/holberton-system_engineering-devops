-- 8. cities of california
-- Selects all the cities from California with a subquery
SELECT * FROM cities
WHERE (SELECT id FROM states WHERE states.name = "California") = cities.state_id
ORDER BY cities.id; 
