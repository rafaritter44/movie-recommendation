import movie_lookup
import argparse

def main():
    parser = argparse.ArgumentParser(description="Get similar movies based on keywords.")
    parser.add_argument("title", type=str, help="The title of the movie.")
    parser.add_argument("--top_n", type=int, default=5, help="The number of similar movies to retrieve (default is 5).")
    parser.add_argument("--release_year", type=int, help="The release year of the movie (optional).")


    args = parser.parse_args()

    try:
        movie_index, title, release_year = movie_lookup.get_movie_by_title(args.title, args.release_year)
        similar_movies = movie_lookup.get_similar_movies(movie_index, args.top_n)

        print(f"Movies similar to {title} ({release_year}):")
        for i, (title, release_year, score) in enumerate(similar_movies, start=1):
            print(f"{i}. {title} ({release_year}) (Similarity score: {score:.4f})")

    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
