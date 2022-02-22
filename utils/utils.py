from modell.building import Building, BuildingConstruction


def building_from_string(raw_string: str) -> Building:

    building_name = ''
    building_level = 0

    for substring in raw_string.split():
        if substring != 'Level' and not substring.isdigit():
            building_name += substring
            building_name += ' '
        elif substring.isdigit():
            building_level = int(substring)

    return Building(building_name[0:-1], building_level)



