import requests
import pandas as pd
from pycountry import countries

def fetch_worldbank_data(indicator_code, column_name):
    url = f"https://api.worldbank.org/v2/country/all/indicator/{indicator_code}?format=json&per_page=20000"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        records = data[1]
        
        df = pd.json_normalize(records)
        df = df[['country.id', 'country.value', 'date', 'value']]
        df.columns = ['country_code', 'country', 'year', column_name]
        df = df.dropna()
        df['year'] = df['year'].astype(int)
        
        # Keep only actual countries
        iso2_list = [c.alpha_2 for c in countries]
        df = df[df['country_code'].isin(iso2_list)]
        
        # Convert ISO2 to ISO3
        def iso2_to_iso3(code):
            try:
                return countries.get(alpha_2=code).alpha_3
            except:
                return None
        
        df['country_code'] = df['country_code'].apply(iso2_to_iso3)
        
        return df
    else:
        print("Error fetching data")
        return None

# Fetch indicators
df_life = fetch_worldbank_data("SP.DYN.LE00.IN", "life_expectancy")
df_gdp = fetch_worldbank_data("NY.GDP.PCAP.CD", "gdp_per_capita")
df_health = fetch_worldbank_data("SH.XPD.CHEX.GD.ZS", "health_expenditure")

# Filter recent years
df_life = df_life[df_life['year'] >= 2017]
df_gdp = df_gdp[df_gdp['year'] >= 2017]
df_health = df_health[df_health['year'] >= 2017]

# Merge datasets
df_final = df_life.merge(df_gdp, on=['country_code','country','year'], how='inner')
df_final = df_final.merge(df_health, on=['country_code','country','year'], how='inner')

print(df_final.head())

df_final.to_csv("worldapi.csv", index=False)