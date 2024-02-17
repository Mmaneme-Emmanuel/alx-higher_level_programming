-- Selects the id and name of cities located in the state of California 
-- from the database, ordered by city id in ascending order.
SELECT id, name FROM cities WHERE state.id = (SELECT id FROM states WHERE name = 'California') ORDER BY id ASC;
