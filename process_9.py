# Create a collection of numbers with size 10.000, create a function for multiplying each element by 5.
from multiprocessing import Process

numbers = [i for i in range(10000)]


def calculate(numbers):
    for idx in numbers:
        numbers[idx] *= 5
    print(numbers)


process = Process(target=calculate, args=(numbers, ))
process.start()