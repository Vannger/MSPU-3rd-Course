DROP TABLE IF EXISTS rentals;

CREATE TABLE rentals (
    id SERIAL PRIMARY KEY,
    customer_name TEXT NOT NULL CHECK (char_length(customer_name) >= 2),
    vehicle_class TEXT NOT NULL CHECK (vehicle_class IN (
        'Economy', 'Compact', 'SUV', 'SUV Premium', 'Premium'
    )),
    pickup_city TEXT NOT NULL,
    daily_rate NUMERIC(10,2) NOT NULL CHECK (daily_rate > 0),
    pickup_date DATE NOT NULL,
    return_date DATE NOT NULL CHECK (return_date >= pickup_date),
    status TEXT NOT NULL CHECK (status IN ('Booked', 'Confirmed', 'Completed', 'Cancelled'))
);
INSERT INTO rentals (customer_name, vehicle_class, pickup_city, daily_rate, pickup_date, return_date, status) VALUES
('Alice Newman', 'SUV', 'New York', 65, '2022-01-01', '2022-01-05', 'Confirmed'),
('Brian Cole', 'SUV Premium', 'New Haven', 72, '2023-12-31', '2024-01-05', 'Booked'),
('Cynthia Row', 'SUV', 'newark', 58, '2022-06-15', '2022-06-20', 'Completed'),
('David Hill', 'Compact', 'New York', 40, '2022-05-10', '2022-05-12', 'Booked'),          -- class not SUV
('Eva Holmes', 'SUV', 'Boston', 55, '2022-03-10', '2022-03-15', 'Booked'),               -- city not new
('Frank North', 'SUV', 'Newcastle', 60, '2021-12-31', '2022-01-05', 'Completed'),        -- date before range
('Grace Lee', 'Premium', 'New Town', 90, '2023-05-01', '2023-05-10', 'Booked'),          -- wrong class
('Henry Stone', 'Compact', 'Los Angeles', 50, '2023-04-10', '2023-04-15', 'Booked'),
('Ian Testman', 'Compact', 'Berlin', 70, '2024-01-10', '2024-01-13', 'Booked'),
('Julia Keen', 'Economy', 'London', 40, '2023-07-07', '2023-07-10', 'Booked'),
('Kyle Roger', 'Economy', 'Test City', 50, '2023-03-10', '2023-03-11', 'Booked'),        -- city contains Test
('Lisa Ben', 'Economy', 'Madrid', 39.99, '2022-05-01', '2022-05-04', 'Booked'),          -- too low rate
('Megan Ford', 'Economy', 'Oslo', 70.01, '2022-02-01', '2022-02-10', 'Booked'),          -- too high rate
('Nathan Fox', 'Economy', 'Rome', 60, '2023-09-01', '2023-09-03', 'Confirmed'),          -- wrong status
('Old Test User 1', 'Compact', 'Chicago', 30, '2018-01-01', '2018-01-10', 'Cancelled'),
('Old Test User 2', 'Premium', 'Dallas', 55, '2017-05-01', '2018-12-30', 'Cancelled'),
('Edge Date Test', 'SUV', 'Paris', 70, '2018-12-20', '2019-01-01', 'Cancelled'),         -- return_date = boundary
('Wrong Status Test', 'Compact', 'Rome', 55, '2018-07-01', '2018-07-10', 'Completed'),   -- wrong status
('Name no test', 'Economy', 'Vienna', 40, '2018-01-10', '2018-01-12', 'Cancelled'),      -- no 'test'
('Peter Long', 'Compact', 'Amsterdam', 52, '2022-08-10', '2022-08-15', 'Completed'),
('Quincy Hart', 'Premium', 'Budapest', 100, '2023-11-01', '2023-11-07', 'Booked'),
('Rita Prince', 'SUV', 'New Orleans', 68, '2022-04-10', '2022-04-18', 'Confirmed'),
('Sam Turner', 'Economy', 'Washington', 42, '2024-01-15', '2024-01-20', 'Booked'),
('Tom West', 'Compact', 'New Berlin', 55, '2023-03-01', '2023-03-05', 'Completed'),
('Uma King', 'SUV Premium', 'Miami', 85, '2022-02-02', '2022-02-08', 'Confirmed');
