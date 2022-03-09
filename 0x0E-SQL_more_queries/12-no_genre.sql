-- 12. no genre
-- Lists all the shows with no genre
SELECT s.title, g.genre_id AS genre_id FROM tv_shows AS s
LEFT JOIN tv_show_genres AS g ON g.show_id = s.id
WHERE g.genre_id IS NULL
ORDER BY s.title, g.genre_id;
