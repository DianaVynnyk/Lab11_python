from models.SportEquipment import SportEquipment
from models.Season import Season
from models.Experience import Experience
from models.DivingEquipment import DivingEquipment

class Diving(SportEquipment):
    def __init__(self, name="", age=0, experience=Experience.ADVANCED, season=Season.WINTER,
                 price=0, rating=0, maximum_Time_Under_Water=0, divingEquipment=DivingEquipment):
        self.name = name
        self.age = age
        self.experience = experience
        self.season = season
        self.price = price
        self.rating = rating
        self.maximum_Time_Under_Water = maximum_Time_Under_Water
        self.DivingEquipment = DivingEquipment