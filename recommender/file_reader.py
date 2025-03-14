import pandas as pd
import ast

def load_and_merge_data():
    # Load the CSV files into DataFrames.
    keywords_df = pd.read_csv('data/keywords.csv', low_memory=False)
    movies_metadata_df = pd.read_csv('data/movies_metadata.csv', low_memory=False)

    # Convert the 'keywords' column from string to list of dictionaries.
    keywords_df['keywords'] = keywords_df['keywords'].apply(ast.literal_eval)

    # Extract only the 'name' of each keyword from the list of dictionaries.
    keywords_df['keywords'] = keywords_df['keywords'].apply(lambda keywords: [keyword['name'] for keyword in keywords])

    # Ensure the 'id' columns in both DataFrames are of the same type (convert them to strings).
    keywords_df['id'] = keywords_df['id'].astype(str)
    movies_metadata_df['id'] = movies_metadata_df['id'].astype(str)

    # Extract only the year from 'release_date'.
    movies_metadata_df['release_year'] = movies_metadata_df['release_date'].astype(str).str[:4]

    # Merge the DataFrames on the 'id' column.
    merged_df = pd.merge(movies_metadata_df[['id', 'title', 'release_year']],
                         keywords_df[['id', 'keywords']], on='id', how='inner')

    # Select only the relevant columns.
    merged_df = merged_df[['id', 'title', 'release_year', 'keywords']]

    return merged_df
