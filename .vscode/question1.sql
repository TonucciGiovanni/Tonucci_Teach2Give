
/*Question 1 - Write a query that will display the results below (Note: some columns might be renamed
but use the column names above). It should only show 2020 data and order by driver
points.*/

CREATE DATABASE tonucci2give;

USE tonucci2give;

CREATE TABLE `Race_Results` (
    race_year INT,
    race_name VARCHAR(255),
    race_date DATE,
    circuit_location VARCHAR(255),
    driver_name VARCHAR(255),
    driver_number INT,
    driver_nationality VARCHAR(255),
    team VARCHAR(255),
    grid INT,
    fastest_lap TIME,
    race_time TIME,
    points INT,
    created_date DATE,
    year INT
);


SELECT race_year, race_name, race_date, circuit_location, driver_name, driver_number, 
       driver_nationality, team, grid, fastest_lap, race_time, points, created_date, year
FROM Race_Results
WHERE year = 2020
ORDER BY points DESC;

-- Solution
/*
In question 1 we first need to create a Database to store the data. The database will have the specific table in which we will use to filter out the data we need. 
To create a database use CREATE DATABASE which creates the database named tonucci2give.
The command USE tells the system to select the tonucci2give database so that the following table creation and other actions are applied to it.
To create a table use CREATE TABLE which Creates a table named Race_Results with all the appropriate column names and their data types which should be specified also.i.e. INT, VARCHAR, TIME, DATE

To write the query use the SQL Command SELECT to specify the columns you want to retrieve.
The Command "WHERE year = 2020" filters the data to only include records from the year 2020.
To order by driver points use the command "ORDER BY points DESC" which orders the data by the points column in descending order so that the highest points appear first.

*/
