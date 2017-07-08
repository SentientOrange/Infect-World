# 5 city state in one country and one infection
city1 = City("City1", 0, 50000, 0, 1, "Nation1")
city2 = City("City2", 0, 40000, 0, 2, "Nation1")
city3 = City("City3", 0, 30000, 0, 3, "Nation1")
city4 = City("City4", 0, 20000, 0, 4, "Nation1")
city5 = City("City5", 0, 10000, 0, 1, "Nation1")

cities = {
    "city1" : city1,
    "city2" : city2,
    "city3" : city3,
    "city4" : city4,
    "city5" : city5
    }

temp = {}

routes = {
    'City1': ["City2", "City3"],
    'City5': ["City1", "City2", "City3", "City4"],
    'City4': ["City5"],
    'City3': ["City1", "City4"],
    'City2': ["City5", "City1", "City3"]
}

infection = Infection("BestInfection",0.02, 0.03)

Nation1 = Country("Nation1", 0.05)

countries = {"Nation1" : Nation1}

World1 = World(cities, countries, routes)

INITIAL_STATE = State(World1, infection)