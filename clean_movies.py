import pandas as pd
import numpy as np

# File path
file_path = r"C:\Users\Shalvi\OneDrive\Desktop\NOVITECH COURSES\INTERNSHIP\movies.csv"

# Load the dataset
df = pd.read_csv(file_path)

# Display initial info
print("Initial Dataset Preview:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# Step 1: Handle Missing Values
df['ONE-LINE'] = df['ONE-LINE'].replace('Add a Plot', pd.NA)
df['RATING'] = df['RATING'].fillna(df['RATING'].median())
df['RunTime'] = df['RunTime'].fillna(df['RunTime'].median())
df = df.dropna(subset=['ONE-LINE', 'GENRE'])
print("\nMissing Values:")
print(df.isnull().sum())

# Step 2: Standardize YEAR
def extract_start_year(year):
    if pd.isna(year):
        return pd.NA
    year = str(year).strip('()')
    if '–' in year:
        return year.split('–')[0]
    return year

df['YEAR'] = df['YEAR'].apply(extract_start_year)
df['YEAR'] = pd.to_numeric(df['YEAR'], errors='coerce')

# Step 3: Clean GENRE
df['GENRE'] = df['GENRE'].str.strip().str.replace(' ,', ',')
df['GENRE_LIST'] = df['GENRE'].str.split(', ')

# Step 4: Parse STARS
def split_stars(stars):
    if pd.isna(stars):
        return pd.NA, pd.NA
    if 'Director:' in stars:
        parts = stars.split('Director:')
        director = parts[1].split('|')[0].strip() if '|' in parts[1] else parts[1].strip()
        actors = parts[1].split('Stars:')[1].strip() if 'Stars:' in parts[1] else pd.NA
    else:
        director = pd.NA
        actors = stars.replace('Stars:', '').strip() if 'Stars:' in stars else stars.strip()
    return director, actors

df[['Director', 'Actors']] = df['STARS'].apply(split_stars).apply(pd.Series)
df = df.drop(columns=['STARS'])

# Step 5: Clean VOTES
df['VOTES'] = df['VOTES'].str.replace(',', '').astype(float).astype('Int64')

# Step 6: Clean Gross
def clean_gross(gross):
    if pd.isna(gross):
        return pd.NA
    gross = gross.replace('$', '').replace('M', '')
    return float(gross)

df['Gross'] = df['Gross'].apply(clean_gross)

# Step 7: Remove Duplicates
print("\nDuplicate Rows:")
print(df.duplicated(subset=['MOVIES', 'YEAR']).sum())
df = df.drop_duplicates(subset=['MOVIES', 'YEAR'], keep='first')

print("\nRATING and Gross Values Before Conversion:")
print(df[['RATING', 'Gross']].head(10))
print(df[['RATING', 'Gross']].dtypes)

# Step 8: Set Data Types
df['RATING'] = pd.to_numeric(df['RATING'], errors='coerce')
df['Gross'] = pd.to_numeric(df['Gross'], errors='coerce')

df = df.astype({
    'MOVIES': 'string',
    'YEAR': 'Int64',
    'GENRE': 'string',
    'ONE-LINE': 'string',
    'VOTES': 'Int64',
    'RunTime': 'Int64',
    'Director': 'string',
    'Actors': 'string'
}, errors='ignore')

# Step 9: Final Inspection
print("\nCleaned Dataset Info:")
print(df.info())
print("\nCleaned Dataset Preview:")
print(df.head())

# Step 10: Save Cleaned Dataset
cleaned_file_path = r"C:\Users\Shalvi\OneDrive\Desktop\NOVITECH COURSES\INTERNSHIP\movies_cleaned.csv"
df.to_csv(cleaned_file_path, index=False)
print(f"\nCleaned dataset saved to: {cleaned_file_path}")

excel_file_path = r"C:\Users\Shalvi\OneDrive\Desktop\NOVITECH COURSES\INTERNSHIP\movies_cleaned.xlsx"
df.to_excel(excel_file_path, index=False)
print(f"Cleaned dataset saved to: {excel_file_path}")
