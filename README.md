# Movie Recommendation POC

## Usage

- `$ python3 recommender/cli.py "A Man for All Seasons"`
- `$ python3 recommender/cli.py "It's a Wonderful Life" --top_n 10`
- `$ python3 recommender/cli.py "titanic" --release_year 1953`

## Limitations

1. There are some movies with no keywords or very few keywords. Recommendations are pretty poor for those movies.
2. Except for capitalization, the provided title must match exactly the title in the `movies_metadata.csv` file.

## Improvement ideas

1. Receive multiple movies instead of just one and give recommendations based on that combination of movies. The list could be ordered from favorite to least favorite and each could have a different weight (for instance, 100% for the favorite and 10% less for each of the following).
2. Consider other fields instead of only considering keywords. And give each of them a different weight. For instance:
   1. Keywords: 40%
   2. Genres: 30%
   3. Overview: 20%
   4. Release date: 10%
3. Cache the algorithm preprocessing on disk so that subsequent CLI calls are faster.
