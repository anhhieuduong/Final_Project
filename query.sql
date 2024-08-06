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
