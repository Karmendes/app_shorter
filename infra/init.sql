-- Create the schema
CREATE SCHEMA IF NOT EXISTS sc_shorter;

-- create the table
CREATE TABLE sc_shorter.tb_shorters_link (
  id INT PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
  short_code VARCHAR(6) UNIQUE NOT NULL,
  url VARCHAR(2048) NOT NULL,
  dt_created TIMESTAMP,
  dt_updated TIMESTAMP
);

