-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT t.name FROM tv_genres AS t
INNER JOIN tv_show_genres AS g
ON t.id = g.genre_id
JOIN tv_shows s
ON s.id = g.show_id
WHERE s.title = "Dexter"
ORDER BY t.name;
