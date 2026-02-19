

from abc import ABC, abstractmethod

from typing_extensions import override


class Media(ABC):
    def __init__(self, title, year, minutes):
        self.title = title
        self.year = year
        self.minutes = minutes

# SHAPE HEKEF ABC --> CIRCLE HEKEF IMPLEMENTED
    @abstractmethod
    def get_rating(self):
        pass

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, value):
        if value and not value.isspace() and len(value) >= 2:
            self.__title = value
        else:
            print ("bad title")

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value > 1880:
            self.__year = value
        else:
            print("invalid year")

    @property
    def minutes(self):
        self.__minutes

    @minutes.setter
    def minutes(self, value):
        if value > 0:
            self.__minutes = value
        else:
            print("invalid minute")

    def __str__(self):
        return f"Media title:{self.title} year:{self.year} minutes:{self.minutes}"

class Movie(Media):
    def __init__(self, title, year, minutes, time_cinema):
        super().__init__(title, year, minutes)
        self.__time_cinema = time_cinema

    @property
    def time_cinema(self):
        return self.__time_cinema

    @time_cinema.setter
    def time_cinema(self, value):
        if value > 0:
            self.__time_cinema = value
        else:
            print("time cannot be zero or less")

    @override
    def get_rating(self):
        if self.time_cinema > 100:
            return "Excellent"
        else:
            return "Regular"

class LongSeasons(ABC):
    @abstractmethod
    def is_long_seasons(self):
        pass

class Series(Media, LongSeasons):
    def __init__(self, title, year, minutes, seasons, episodes):
        super().__init__(title, year, minutes)
        self.__seasons = seasons
        self.__episodes = episodes

    @property
    def seasons(self):
        return self.__seasons

    @seasons.setter
    def seasons(self, value):
        if value > 0 and value > self.episodes:
            self.__seasons = value
        else:
            print("invalid seasons")

    @property
    def episodes(self):
        return self.__episodes

    @episodes.setter
    def episodes(self, value):
        if value > 0 and value > self.seasons:
            self.__episodes = value
        else:
            print("invalid episodes")

    @override
    def get_rating(self):
        if self.seaons > 8:
            return "Excellent"
        else:
            return "Regular"

    @override
    def is_long_seasons(self):
        return self.episodes // self.seasons > 10


batman = Movie('Batman', 2014, 120, 101)
print(batman.get_rating())
breaking_bad = Series('Breaking bad', 2020,
                      800, 8, 82)
'''
Implement __eq__: compare title.lower() + year
  if the same --> return true otherwise false
Implement __gt__: compare minutes 
        __ge__ __lt__ le__  >= > < <=
class Movie inherits Media 
  field __director getter setter check len(director) > 4
  field __budget getter setter check > 0
class Series inherites Media
  field __seasons __episodes
     season > 0 episodes > 0
     season > episodes
__str__
'''