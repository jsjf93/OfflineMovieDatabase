class Movie:
    def __init__(self, movie_title, year, age_rating, genres, length):
        self.__movie_title = movie_title
        self.__year = year
        self.__age_rating = age_rating
        self.__genres = genres
        self.__length = length
        self.__sum_ratings = 0
        self.__num_ratings = 0

    def get_movie_title(self):
        return self.__movie_title

    def get_year(self):
        return self.__year

    def get_age_rating(self):
        return self.__age_rating

    def get_genres(self):
        return self.__genres

    def get_length(self):
        return self.__length

    def get_avg_rating(self):
        return self.__sum_ratings / self.__num_ratings

    def add_rating(self, rating):
        self.__sum_ratings += rating.get_rating()
        self.__num_ratings += 1
