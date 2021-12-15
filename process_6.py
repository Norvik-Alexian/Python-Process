# Define a collection of 5.000 numbers, create 3 extra processes, 1-st to multiply each element by 10, 2-nd to get from
# result by 1-st elements which can be divided by 3, 3-rd to see if sum of the result of 1-st is positive.
from multiprocessing import Process, Pipe

numbers = [i for i in range(5000)]


def first_calculate(numbers, pipeline):
    for idx in range(len(numbers)):
        numbers[idx] *= 10
    pipeline[0].send(numbers)
    pipeline[0].send(numbers)
    print(numbers)


def second_calculate(pipline):
    numbers1 = pipline[1].recv()
    numbers2 = []
    for number in numbers1:
        if number % 3 == 0:
            numbers2.append(number)
    print(numbers2)


def third_calculate(pipeline):
    numbers = pipeline[1].recv()
    if sum(numbers) > 0:
        print('yes the summation of all the numbers is positive')


pipeline = Pipe()

process1 = Process(target=first_calculate, args=(numbers, pipeline))
process2 = Process(target=second_calculate, args=(pipeline, ))
process3 = Process(target=third_calculate, args=(pipeline, ))

process1.start()
process2.start()
process3.start()

