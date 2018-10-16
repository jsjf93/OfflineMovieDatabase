class MovieDatabase:
    def __init__(self, movie_list=None):
        if movie_list is None:
            self.__movie_database = []
        else:
            self.__movie_database = movie_list

    def get_movie_database(self):
        return self.__movie_database

    def add_movie(self, movie):
        self.__movie_database.append(movie)

    def print_all(self):
        for movie in self.__movie_database:
            print(movie.get_movie_title(), ',',
                  movie.get_year(), ',',
                  movie.get_age_rating(), ',',
                  movie.get_genres(), ',',
                  movie.get_length())
