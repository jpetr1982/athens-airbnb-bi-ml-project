SELECT
    neighbourhood_cleansed,
    COUNT(*) AS number_of_listings,
    ROUND(AVG(price), 2) AS average_price,
    ROUND(MIN(price), 2) AS minimum_price,
    ROUND(MAX(price), 2) AS maximum_price,
    ROUND(AVG(availability_365), 2) AS average_availability_365,
    ROUND(AVG(review_scores_rating), 2) AS average_review_score,
    ROUND(AVG(high_price_listing) * 100, 2) AS high_price_listing_share
FROM airbnb_listings
GROUP BY neighbourhood_cleansed
ORDER BY number_of_listings DESC;