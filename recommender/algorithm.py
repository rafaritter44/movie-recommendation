from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import file_reader

df = file_reader.load_and_merge_data()

# Convert the keywords list into a space-separated string for each movie.
df['keywords_str'] = df['keywords'].apply(lambda keywords: " ".join(keywords))

# Initialize TF-IDF vectorizer.
tfidf_vectorizer = TfidfVectorizer(stop_words='english')

# Convert the keywords strings into TF-IDF vectors.
tfidf_matrix = tfidf_vectorizer.fit_transform(df['keywords_str'])

# Calculate the cosine similarity between movies.
cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

def get_movie_index_by_title(title):
    idx = df[df['title'].str.lower() == title.lower()].index
    if len(idx) == 0:
        raise ValueError(f"Movie with title '{title}' not found.")
    return idx[0]

def get_similar_movies_by_title(movie_title, top_n):
    movie_index = get_movie_index_by_title(movie_title)

    # Get the cosine similarities for the given movie.
    sim_scores = list(enumerate(cosine_similarities[movie_index]))

    # Sort movies based on similarity score (excluding the movie itself).
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:]

    # Get the top_n most similar movies.
    similar_movies = [(df.iloc[i[0]]['title'], i[1]) for i in sim_scores[:top_n]]

    return similar_movies
