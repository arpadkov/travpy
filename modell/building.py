import datetime


class Building:

    def __init__(self, name: str, level: str):
        self.name = name
        self.level = int(level)


class BuildingConstruction:

    def __init__(self, building: Building, building_for: str):
        self.building = building
        self.building_for = datetime.timedelta(seconds=int(building_for))

    def get_name(self):
        return self.building.name
