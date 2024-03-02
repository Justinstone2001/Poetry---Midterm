import pandas as pd

df = pd.read_csv('countries.csv')

print(df.head())

df['Population in Millions'] = df['Population'] / 1_000_000

df_sorted = df.sort_values('Population', ascending=False)

print("\nCountries sorted by population:")
print(df_sorted)


total_population = df['Population'].sum()
print(f"\nTotal population from the dataset: {total_population} people")

average_population = df['Population in Millions'].mean()
print(f"Average population: {average_population:.2f} million people")

max_population_country = df.loc[df['Population'].idxmax()]
print(f"\nCountry with the highest population: {max_population_country['Country']} ({max_population_country['Population']} people)")
print("hello")