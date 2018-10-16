class Rating:
    def __init__(self, timestamp, username, movie_title, rating):
        self.__timestamp = timestamp
        self.__username = username
        self.__movie_title = movie_title
        self.__rating = rating

    def get_timestamp(self):
        return self.__timestamp

    def get_username(self):
        return self.__username

    def get_movie_title(self):
        return self.__movie_title

    def get_rating(self):
        return self.__rating

    def print(self):
        return print(self.__timestamp.date(), self.__timestamp.time(), ', ',
                     self.__username, ', ', self.__movie_title, ', ', self.__rating)
