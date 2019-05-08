from models.SportEquipment import SportEquipment
from models.Season import Season
from models.Experience import Experience

class RockClimbing(SportEquipment):
    def __init__(self, name="", age=0, experience=Experience.ADVANCED, season=Season.WINTER,
                 price=0, rating=0, cliff_Height=0):
        self.name = name
        self.age = age
        self.experience = experience
        self.season = season
        self.price = price
        self.rating = rating
        self.cliff_Height = cliff_Height