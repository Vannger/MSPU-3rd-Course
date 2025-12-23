DELETE FROM rentals
WHERE status = 'Cancelled'
  AND return_date < '2019-01-01'
  AND customer_name ILIKE '%test%';
SELECT *
FROM rentals
WHERE customer_name ILIKE '%test%';
