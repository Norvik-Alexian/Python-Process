# Create a program that simultaneously adds and subtracts numbers collection and prints a message at the end.
from multiprocessing import Process

collection_one = [1, 4, 5, 2, 8, 9]
collection_two = [5, 1, 9, 5, 19, 30]


def add(numbers_one: list, numbers_two: list):
    add_collection = []
    for number_one, number_two in zip(numbers_one, numbers_two):
        result = number_one + number_two
        add_collection.append(result)

    print(add_collection)


def subtraction(numbers_one: list, numbers_two: list):
    subtraction_collection = []
    for number_one, number_two in zip(numbers_one, numbers_two):
        result = number_one - number_two
        subtraction_collection.append(result)

    print(subtraction_collection)


process1 = Process(target=add, args=(collection_one, collection_two))
process2 = Process(target=subtraction, args=(collection_one, collection_two))

process1.start()
process2.start()