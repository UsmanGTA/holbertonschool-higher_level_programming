-- Counts the number of shows associated
-- with each and every genre.
SELECT tv_genres.name AS genre, count(*) as number_of_shows
	FROM tv_show_genres LEFT JOIN tv_genres
	ON tv_show_genres.genre_id = tv_genres.id
	GROUP BY tv_genres.name
	ORDER BY number_of_shows;
