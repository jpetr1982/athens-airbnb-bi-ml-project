SELECT
    neighbourhood_cleansed,
    room_type,
    COUNT(*) AS number_of_listings,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(AVG(high_price_listing) * 100, 2) AS high_price_listing_share,
    ROUND(AVG(accommodates), 2) AS average_accommodates,
    ROUND(AVG(bedrooms), 2) AS average_bedrooms,
    ROUND(AVG(bathrooms), 2) AS average_bathrooms
FROM airbnb_listings
GROUP BY neighbourhood_cleansed, room_type
HAVING COUNT(*) >= 20
ORDER BY high_price_listing_share DESC, number_of_listings DESC;