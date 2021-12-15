# Define a shared collection of numbers, create 2 extra processes, one for adding 10 to each element 5.000 times,
# another for subtracting 5 to each element 10.000 times, print result array.
from multiprocessing import Array, Process

numbers = Array('i', [5, 7, 9, 9, 7, 7])


def first_calculate(numbers):
    for _ in range(5000):
        for i in range(len(numbers)):
            numbers[i] += 10
    print(numbers[:])


def second_calculate(numbers):
    for _ in range(10000):
        for i in range(len(numbers)):
            numbers[i] -= 5
    print(numbers[:])


process1 = Process(target=first_calculate, args=(numbers, ))
process2 = Process(target=second_calculate, args=(numbers, ))

process1.start()
process1.join()

process2.start()
