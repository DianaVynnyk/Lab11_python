from models.Season import Season
from models.Experience import Experience

class SportEquipment:

    def __init__(self, name="", age=0, experience=Experience.ADVANCED, season=Season.WINTER, price=0, rating=0):
      self.name = name
      self.age = age
      self.experience = experience
      self.season = season
      self.price = price
      self.rating = rating
    def __str__(self):
        return ("Name: " + self.name + ", Age: " + str(self.age) + ", Experience: " + str(self.experience)
             + ", Season: " + str(self.season) + ", Price: " + str(self.price) + ", Rating: " + str(self.rating))