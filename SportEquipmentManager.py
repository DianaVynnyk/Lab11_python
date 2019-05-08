from models.SportEquipment import SportEquipment
from models.Diving import Diving
from models.DivingEquipment import DivingEquipment
from models.Experience import Experience
from models.RockClimbing import RockClimbing
from models.Season import Season
from models.Snowboarding import Snowboarding
from models.SnowboardingEquipment import SnowboardingEquipment

class SportEquipmentManager:
    def __init__(self, *args):
        self.SportEquipment = args


    def filter_By_Season(self, season):
        return list(filter(lambda Equipment: Equipment.season == season, self.SportEquipment))

    def filter_By_Experience(self, experience):
        return list(filter(lambda Equipment: Equipment.experience == experience, self.SportEquipment))

    def filter_By_Name(self, name):
        return list(filter(lambda Equipment: Equipment.name == name, self.SportEquipment))

    def filter_By_Price(self, price):
        return list(filter(lambda Equipment: Equipment.price == price, self.SportEquipment))

    @staticmethod
    def sort_By_Price(SportEquipment, descending=False):
        return sorted(SportEquipment, key=lambda Equipment: Equipment.price, reverse=descending)

    @staticmethod
    def sort_By_Rating(SportEquipment, descending=False):
        return sorted(SportEquipment, key=lambda Equipment: Equipment.rating, reverse=descending)
def main():
    SportEquipment = [
    Diving("overalls", 17, Experience.ADVANCED, Season.SUMMER, 300, 3.5, 1000, None),
    Snowboarding("gloves", 16, Experience.BEGINNER, Season.WINTER, 200, 3, 1000, SnowboardingEquipment.HELMET),
    RockClimbing("glasses", 28, Experience.PROFESSIONAL, Season.FALL, 100, 5, 0),
    RockClimbing("helmet", 20, Experience.ADVANCED, Season.SPRING, 100, 4, 0),
    Diving("", 25, Experience.PROFESSIONAL, Season.SUMMER, 700, 5, 0, DivingEquipment.MASK)
    ]
    manager = SportEquipmentManager(*SportEquipment)

    filteredList = manager.filter_By_Price(0)
    for x in filteredList:
        print(x)
    print()

    sortedList = SportEquipmentManager.sort_By_Rating(SportEquipment)
    for x in sortedList:
        print(x)
    print()

    sortedFilteredList = SportEquipmentManager.sort_By_Rating(filteredList)
    for x in sortedFilteredList:
        print(x)

if __name__ == '__main__':
    main()
