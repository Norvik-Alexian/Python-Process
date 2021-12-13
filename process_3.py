# Create a collection of numbers and simultaneously add 2 to elements on even positions and multiply by 3 elements on odd positions, print the result.
from multiprocessing import Process, Queue

numbers_collection = [5, 1, 9, 8, 19, 30]


def first_calculation(collection: list):
    new_collection = []
    for number in collection:
        if collection.index(number) % 2 == 0:
            number += 2
            new_collection.append(number)
        else:
            new_collection.append(number)
    print(new_collection)


def second_calculation(collection: list):
    new_collection = []
    for number in collection:
        if collection.index(number) % 2 == 1:
            number *= 3
            new_collection.append(number)
        else:
            new_collection.append(number)
    print(new_collection)


process1 = Process(target=first_calculation, args=(numbers_collection, ))
process2 = Process(target=second_calculation, args=(numbers_collection, ))

process1.start()
process2.start()

