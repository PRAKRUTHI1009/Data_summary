1.create the raw table
CREATE TABLE worldbank_raw (
    country_code VARCHAR(3),country TEXT,year INT,life_expectancy FLOAT,
    gdp_per_capita FLOAT,health_expenditure FLOAT);

2.Imported file worldapi.csv 

3.SELECT * FROM worldbank_raw LIMIT 10;

4.//created the dim table
CREATE TABLE dim_country AS SELECT DISTINCT country_code, country
FROM worldbank_raw;

5.//created the fact table
CREATE TABLE fact_country AS
SELECT country_code,year,life_expectancy, gdp_per_capita,
health_expenditure FROM worldbank_raw;

6.//checking tables
SELECT COUNT(*) FROM dim_country;
SELECT COUNT(*) FROM fact_country;

//dim_country
------------
country_code
country

        |
        |
        v

fact_country
------------
country_code
year
life_expectancy
gdp_per_capita
health_expenditure

//checked null values
SELECT * FROM fact_country WHERE life_expectancy IS NULL;
//checked duplicate values
SELECT country_code, year, COUNT(*) FROM fact_country GROUP BY country_code, year
HAVING COUNT(*) > 1;

//joins
SELECT d.country,f.year,f.life_expectancy FROM fact_country f
JOIN dim_country d ON f.country_code = d.country_code LIMIT 10;

//range checks
1.Life Expectancy Range
SELECT *
FROM fact_country
WHERE life_expectancy < 40 OR life_expectancy > 90;

2.GDP per Capita Range
SELECT *
FROM fact_country
WHERE gdp_per_capita < 0 OR gdp_per_capita > 200000;

3. Health Expenditure Range
SELECT *
FROM fact_country
WHERE health_expenditure < 0 OR health_expenditure > 100;