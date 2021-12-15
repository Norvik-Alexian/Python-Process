# Create a collection of country names with their temperature, simultaneously increment temperature of cities which
# name starts with ‘T’ or ‘I’, subtract by 5 temperature of countries which name starts with ‘A’ or ‘R’, print the result
from multiprocessing import Process

countries = {'Iran': 30, 'Tailand': 45, 'Armenia': 15, 'United States': 17, 'Russia': 10, 'Argentina': 20}


def first_country_collection():
    global countries
    for country in countries:
        if 'I' in country or 'T' in country:
            countries[country] += 5
    print(countries)


def second_country_collection():
    global countries
    for country in countries:
        if 'A' in country or 'R' in country:
            countries[country] -= 5
    print(countries)


process1 = Process(target=first_country_collection)
process2 = Process(target=second_country_collection)

process1.start()
process2.start()