import re
import maya

from src.Movie import Movie
from src.MovieDatabase import MovieDatabase
from src.Rating import Rating
from src.Ratings import Ratings

# Read in the movies
movie_database = MovieDatabase()
movies_file = open("Data/movies.txt", "r")

for line in movies_file:
    current_line = re.split(r',(?=")|,(?=[0-9])', line)
    movie = Movie(current_line[0].replace('"', ''),             # title
                  int(current_line[1]),                         # year
                  current_line[2].replace('"', ''),             # age rating
                  current_line[3].replace('"', '').split('/'),  # genres
                  int(current_line[4].replace('\n', '')))       # length
    movie_database.add_movie(movie)

movies_file.close()

# Read in the ratings
ratings = Ratings()
ratings_file = open("Data/ratings.txt", "r")

for line in ratings_file:
    current_line = re.split(r',(?=")|,(?=[0-9])', line)
    rating = Rating(maya.parse(current_line[0]).datetime(),  # datetime
                    current_line[1].replace('"', ''),        # username
                    current_line[2].replace('"', ''),        # movie title
                    int(current_line[3].replace('\n', '')))  # rating
    ratings.add_rating(rating)

ratings_file.close()

# Add ratings to the appropriate movie
for movie in movie_database.get_movie_database():
    for rating in ratings.get_ratings():
        if rating.get_movie_title() == movie.get_movie_title():
            movie.add_rating(rating)

# Tasks:
# 1. Sort movies in ascending order of release date and display on the console
movie_database.get_movie_database().sort(key=lambda m: m.get_year())
movie_database.print_all()
print('\n')

# 2. Display the third longest Film-Noir
new_list = MovieDatabase([movie for movie in movie_database.get_movie_database() if 'Film-Noir' in movie.get_genres()])
print(sorted(new_list.get_movie_database(), key=lambda m: m.get_length(), reverse=True)[2].get_movie_title())
print('\n')

# 3. Display the 10th highest rated Sci-Fi movie
new_list = MovieDatabase([movie for movie in movie_database.get_movie_database() if 'Sci-Fi' in movie.get_genres()])
print(sorted(new_list.get_movie_database(), key=lambda m: m.get_avg_rating(), reverse=True)[9].get_movie_title())
print('\n')

# 4. Display the highest rated movie
print(max(movie_database.get_movie_database(), key=lambda m: m.get_avg_rating()).get_movie_title())
print('\n')

# 5. Display the movie with the longest title
print(max(movie_database.get_movie_database(), key=lambda m: len(m.get_movie_title())).get_movie_title())
print('\n')

# 6. Display the chronologically 101st user rating
sorted(ratings.get_ratings(), key=lambda r: r.get_timestamp(), reverse=True)[100].print()
print('\n')
