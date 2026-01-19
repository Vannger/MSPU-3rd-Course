
ALTER TABLE shipment_raw
RENAME TO shipments;

ALTER TABLE shipments
ALTER COLUMN weight_grams
TYPE numeric(10,3)
USING weight_grams / 1000.0;

ALTER TABLE shipments
RENAME COLUMN weight_grams TO weight_kg;

ALTER TABLE shipments
ADD COLUMN tracking_code text;

UPDATE shipments
SET tracking_code =
    'TRK-' ||
    to_char(shipped_at, 'YYYYDDD') ||
    '-' ||
    lpad(id::text, 5, '0');

ALTER TABLE shipments
DROP COLUMN deprecated_flag;