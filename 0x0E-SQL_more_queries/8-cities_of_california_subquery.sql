-- lists all the cities of California that can be found in the database hbtn_0d_usa

SELECTcities.id,  cities.name
FROM cities
WHERE cities.id = (
	SELECT state.id
	FROM state
	WHERE states.name = 'California'
	)
ORDER BY cities.id ASC;
