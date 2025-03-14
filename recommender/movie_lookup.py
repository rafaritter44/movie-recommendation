import preprocessing

df, cosine_similarities = preprocessing.preprocess_data()

def get_movie_by_title(title):
    movie_row = df[df['title'].str.lower() == title.lower()]
    if movie_row.empty:
        raise ValueError(f"Movie with title '{title}' not found.")

    movie_index = movie_row.index[0]
    # Use the title from the DataFrame, which is guaranteed to be properly capitalized.
    title = movie_row.iloc[0]['title']
    release_year = movie_row.iloc[0]['release_year']

    return movie_index, title, release_year

def get_similar_movies(movie_index, top_n):
    # Get the cosine similarities for the given movie.
    sim_scores = list(enumerate(cosine_similarities[movie_index]))

    # Sort movies based on similarity score (excluding the movie itself).
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]

    # Get the top_n most similar movies.
    similar_movies = [(df.iloc[i[0]]['title'], df.iloc[i[0]]['release_year'], i[1])
                      for i in sim_scores[:top_n]]

    return similar_movies
