SELECT
    id,
    customer_name,
    vehicle_class,
    pickup_city,
    daily_rate,
    pickup_date,
    return_date,
    status
FROM rentals
WHERE pickup_city ILIKE '%new%'
  AND vehicle_class ILIKE 'suv%'
  AND pickup_date BETWEEN '2022-01-01' AND '2023-12-31'
ORDER BY pickup_date, customer_name;
