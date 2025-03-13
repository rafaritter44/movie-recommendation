import algorithm
import argparse

def main():
    parser = argparse.ArgumentParser(description="Get similar movies based on keywords.")
    parser.add_argument("movie_title", type=str, help="The title of the movie.")
    parser.add_argument("--top_n", type=int, default=5, help="The number of similar movies to retrieve (default is 5).")

    args = parser.parse_args()

    try:
        similar_movies = algorithm.get_similar_movies_by_title(args.movie_title, args.top_n)

        print(f"Movies similar to '{args.movie_title}':")
        for i, (title, score) in enumerate(similar_movies, start=1):
            print(f"{i}. {title} (Similarity Score: {score:.4f})")

    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()
