class Ratings:
    def __init__(self, ratings=None):
        if ratings is None:
            self.__ratings = []
        else:
            self.__ratings = ratings

    def get_ratings(self):
        return self.__ratings

    def add_rating(self, rating):
        self.__ratings.append(rating)
