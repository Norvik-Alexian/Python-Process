from multiprocessing import Process, Queue

# Create 2 processes: 1. calculate sum of list of numbers and print it; 2. calculate count of even elements in list of numbers and print it.
l1 = [0, 2, 5, 8, 3, 8, 4, 2, 1, 5]
l2 = [5, 7, 9, 9, 7, 7, 1, 3, 9, 7]


def summation(numbers):
    global l1, l2
    for i, j in zip(l1, l2):
        numbers.put(i + j)


def even_odd(numbers: Queue):
    even = []
    odd = []

    for _ in range(numbers.qsize()):
        num = numbers.get()
        if num % 2 == 0:
            even.append(num)
        if num % 2 != 0:
            odd.append(num)
    print(f"Even Elements: {even}\nCount of Even Elements: {len(even)}")
    print(f"Odd Elements: {odd}\nCount of Odd Elements: {len(odd)}")


q = Queue(len(l1))
p1 = Process(target=summation, args=(q,))
p2 = Process(target=even_odd, args=(q,))

p1.start()
p1.join()

p2.start()
