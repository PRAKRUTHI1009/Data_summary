**SET UP INSTRUCTIONS:**
**1.Install Python Libraries**
pip install pandas
pip install requests
pip install pycountry

**2.Run the Data Extraction Script****
def fetch_worldbank_data(indicator_code, column_name):
url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page=2000"
 # Fetch indicators
df_life = fetch_worldbank_data("SP.DYN.LE00.IN", "life_expectancy")
df_gdp = fetch_worldbank_data("NY.GDP.PCAP.CD", "gdp_per_capita")
df_health = fetch_worldbank_data("SH.XPD.CHEX.GD.ZS", "health_expenditure")

**3.Load Data into PostgreSQL**
Create tables in PostgreSQL:
1.CREATE TABLE dim_country (country_code VARCHAR(3) PRIMARY KEY,country TEXT);
2.CREATE TABLE fact_country (country_code VARCHAR(3),year INT,life_expectancy FLOAT,gdp_per_capita FLOAT,health_expenditure FLOAT,
FOREIGN KEY (country_code) REFERENCES dim_country(country_code));
Import the CSV files into these tables.

**4.Connect to Power BI**
Open Power BI Desktop
Select Get Data → PostgreSQL
Import the tables:
dim_country
fact_country
Create relationship:
fact_country.country_code → dim_country.country_code

**API's Used:**
df_life = fetch_worldbank_data("SP.DYN.LE00.IN", "life_expectancy")
df_gdp = fetch_worldbank_data("NY.GDP.PCAP.CD", "gdp_per_capita")
df_health = fetch_worldbank_data("SH.XPD.CHEX.GD.ZS", "health_expenditure")

**Overview of Approach**
This project analyzes the relationship between economic indicators and health outcomes across countries.
The workflow followed in this project:
1.Data Extraction:Data was collected using the World Bank API for multiple global indicators.
2.Data Processing:Python was used to clean and transform the data.
Multiple indicators were merged into a single dataset.
Country codes were standardized.
3.Data Modeling:A simple analytical data model was designed using:
Fact Table → health and economic indicators
Dimension Table → country information
4.Data Storage:Processed data was stored in PostgreSQL.
5.Data Visualization:The dataset was connected to Power BI to create an interactive dashboard.

**Example Insights**
Life Expectancy and Economic Development
Countries with higher GDP per capita generally show higher life expectancy, suggesting a link between economic development
and health outcomes.
Health Investment Patterns
Countries that spend a higher percentage of GDP on healthcare tend to show better overall health indicators.




