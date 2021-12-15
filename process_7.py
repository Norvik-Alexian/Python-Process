# Create a variable storing integer, create 2 extra processes, one should add 3 to value 1000 times and transfer
# the result to another process which prints it.
from multiprocessing import Process, Pipe

number = 50


def calculate(number, pipeline):
    for _ in range(1000):
        number += 3
    pipeline[0].send(number)


def print_result(pipline):
    print(f'the result of calculation is: {pipline[1].recv()}')


pipeline = Pipe()

process1 = Process(target=calculate, args=(number, pipeline))
process2 = Process(target=print_result, args=(pipeline, ))

process1.start()
process2.start()