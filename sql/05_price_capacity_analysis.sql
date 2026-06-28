SELECT
    accommodates,
    COUNT(*) AS number_of_listings,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(MIN(price), 2) AS minimum_price,
    ROUND(MAX(price), 2) AS maximum_price,
    ROUND(AVG(bedrooms), 2) AS average_bedrooms,
    ROUND(AVG(bathrooms), 2) AS average_bathrooms,
    ROUND(AVG(high_price_listing) * 100, 2) AS high_price_listing_share
FROM airbnb_listings
GROUP BY accommodates
ORDER BY accommodates;