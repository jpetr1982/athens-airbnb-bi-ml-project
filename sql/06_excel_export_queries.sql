-- Main analytical table for Excel / Power BI

SELECT
    id,
    neighbourhood_cleansed,
    room_type,
    property_type,
    accommodates,
    bedrooms,
    bathrooms,
    beds,
    amenities_count,
    price,
    availability_365,
    review_scores_rating,
    number_of_reviews,
    reviews_per_month,
    host_is_superhost,
    instant_bookable,
    high_price_listing
FROM airbnb_listings
WHERE price IS NOT NULL
ORDER BY price DESC;