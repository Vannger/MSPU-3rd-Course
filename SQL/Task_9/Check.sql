SELECT
    id,
    recipient_name,
    weight_kg,
    shipped_at,
    status,
    tracking_code
FROM shipments
ORDER BY id;
