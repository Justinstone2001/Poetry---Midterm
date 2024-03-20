import pandas as pd

### Example of a simple pandas execution for poetry test

# Read in .csv file
df = pd.read_csv('populations.csv')
print(df.head())

# Convert population to millions
df['Population in Millions'] = df['Population'] / 1_000_000

# Sort dataframe by population in decending order
df_sorted = df.sort_values('Population', ascending=False)
print("\nCountries sorted by population:")
print(df_sorted)

# Calculate total population
total_population = df['Population'].sum()
print(f"\nTotal population from the dataset: {total_population} people")

# Calculate average population
average_population = df['Population in Millions'].mean()
print(f"Average population: {average_population:.2f} million people")

# Calculate highest population 
max_population_country = df.loc[df['Population'].idxmax()]
print(f"\nCountry with the highest population: {max_population_country['Country']} ({max_population_country['Population']} people)")
