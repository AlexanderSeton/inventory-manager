DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS vendors;

CREATE TABLE vendors (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    active BOOLEAN
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255),
    description VARCHAR(255),
    stock_quantity INT,
    buying_cost DECIMAL(19, 2),
    selling_price DECIMAL(19, 2),
    vendor_id INT REFERENCES vendors(id)
);
