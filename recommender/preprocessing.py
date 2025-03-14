from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import file_reader

def preprocess_data():
    df = file_reader.load_and_merge_data()

    # Convert the keywords list into a space-separated string for each movie.
    df['keywords_str'] = df['keywords'].apply(lambda keywords: " ".join(keywords))

    # Initialize TF-IDF vectorizer.
    tfidf_vectorizer = TfidfVectorizer(stop_words='english')

    # Convert the keywords strings into TF-IDF vectors.
    tfidf_matrix = tfidf_vectorizer.fit_transform(df['keywords_str'])

    # Calculate the cosine similarity between movies.
    cosine_similarities = cosine_similarity(tfidf_matrix, tfidf_matrix)

    return df, cosine_similarities