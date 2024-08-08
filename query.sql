-- Identify the most popular songs in playlists:
SELECT 
    t.name AS track_name,
    a.name AS artist_name,
    COUNT(pt.track_id) AS playlist_count
FROM 
    tracks t
JOIN 
    playlist_tracks pt ON t.id = pt.track_id
JOIN 
    artists a ON t.artist_id = a.id
GROUP BY 
    t.name, a.name
ORDER BY 
    playlist_count DESC
LIMIT 10;

-- Analyze featured artists in playlists:
SELECT 
    a.name AS artist_name,
    COUNT(t.id) AS total_tracks,
    AVG(f.popularity) AS avg_popularity,
    SUM(a.followers) AS total_followers
FROM 
    artists a
JOIN 
    tracks t ON a.id = t.artist_id
JOIN 
    features f ON t.id = f.id
GROUP BY 
    a.name
ORDER BY 
    total_tracks DESC, avg_popularity DESC
LIMIT 10;

-- Analyze song release trends over time
SELECT 
    strftime('%Y', t.release_date) AS year,
    COUNT(t.id) AS total_tracks
FROM 
    tracks t
GROUP BY 
    year
ORDER BY 
    year DESC;