UPDATE rentals
SET status = 'Confirmed'
WHERE status = 'Booked'
  AND daily_rate BETWEEN 40 AND 70
  AND pickup_city NOT ILIKE '%test%';
  
SELECT id, customer_name, daily_rate, pickup_city, status
FROM rentals
ORDER BY id;
