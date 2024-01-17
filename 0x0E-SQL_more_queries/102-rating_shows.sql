-- Use the hbtn_0d_tvshows_rate database
-- Select shows from tv_shows by their rating sum

SELECT tv_shows.title, SUM(rating) AS rating
FROM tv_shows
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY tv_shows.id
ORDER BY rating DESC;
