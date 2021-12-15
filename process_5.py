# Input a collection of numbers, create 3 extra processes, one for adding 2 to each element, 2-nd for calculating number
# of positive elements in result of 1-st, 3-rd to calculate power 5 of result of 2-nd and print the result.
from multiprocessing import Process, Pipe

input_numbers = input('Please enter some numbers here with a space:')
collection = input_numbers.split(' ')
numbers_collection = list(map(int, collection))


def first_calculate(numbers: list, pipeline):
    for idx in range(len(numbers)):
        numbers[idx] += 2
    pipeline[0].send(numbers)
    print(numbers)


def second_calculate(first_pipeline, second_pipeline):
    counter = 0
    numbers = first_pipeline[1].recv()
    for number in numbers:
        if number > 0:
            counter += 1
    second_pipeline[0].send(numbers)
    print(counter)


def third_calculate(pipeline):
    numbers = pipeline[1].recv()
    for idx in range(len(numbers)):
        numbers[idx] **= 5
    print(numbers)


first_pipeline = Pipe()
second_pipeline = Pipe()

process1 = Process(target=first_calculate, args=(numbers_collection, first_pipeline))
process2 = Process(target=second_calculate, args=(first_pipeline, second_pipeline))
process3 = Process(target=third_calculate, args=(second_pipeline, ))

process1.start()
process2.start()
process3.start()
