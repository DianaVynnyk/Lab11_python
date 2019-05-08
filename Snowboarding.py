from models.SportEquipment import SportEquipment
from models.Experience import Experience
from models.Season import Season
from models.SnowboardingEquipment import SnowboardingEquipment

class Snowboarding(SportEquipment):
    def __init__(self, name="", age=0, experience=Experience.ADVANCED, season=Season.WINTER, price=0, rating=0,
                 downhill_Height=0, SnowboardingEquipment=SnowboardingEquipment):
        self.name = name
        self.age = age
        self.experience = experience
        self.season = season
        self.price = price
        self.rating = rating
        self.downhill_Height = downhill_Height
        self.SnowboardingEquipment = SnowboardingEquipment