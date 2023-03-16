-- A script that lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
SELECT DISTINCT t.title
FROM tv_shows AS t
LEFT JOIN tv_show_genres AS s
ON t.id = s.show_id

LEFT JOIN tv_genres AS g
ON g.id = s.genre_id
WHERE t.title NOT IN (
	SELECT t.title
	FROM tv_shows AS t
	INNER JOIN tv_show_genres as s
	ON t.id = s.show_id
	
	INNER JOIN tv_genres AS g
	ON g.id = s.genre_id
	WHERE g.name = 'Comedy')
ORDER BY t.title;
