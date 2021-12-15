## Process & Multiprocessing
* Process is a program at running stage
* Multiprocessing refers to the ability of a system to support more than one process at the same time.

## Why Multiprocessing
* Multicore systems allows to perform several tasks at the same time.
* Some time we need to perform several tasks simultaneously or almost simultaneously.
* Python Multiprocessing unlike Threading allows to use the CPU cores more effectively, but also requires more resources
and have less convenient mechanisms for sharing data.

## Multiprocessing Adapted Hardware
* Computer with more than one processor
* Computer with two or more processor cores.

## Multiprocessing in Python
In Python, the "multiprocessing" module includes a very simple and intuitive API for dividing work between multiple processes.

## Wait for process
When we run process it runs simultaneously with other processes, we can wait for process to finish with join() method 
called on it.

## Porcesses & Memory
By default, processes have separate memory, if we try to use some variable in child process from main then a new variable 
in child memory will be created.

## Sharing data between processes
There are 2 main approaches for processes to have shared data:
* Shared Memory
* Server Process

## Shared Memory
Multiprocessing provides `Array` and `Value` objects for sharing data.

## Server Process
* Whenever a python program starts, a server process is also started.
* A manager object returned by Manager() from multiprocessing controls a server process which holds Python objects and
allows other processes to manipulate them using proxies.
* A manager returned by Manager() will support types list, dict, Namespace, Lock, RLock, Semaphore, BoundSemaphore, 
Condition, Event, Queue, Value and Array.

## Server process features
* Single manager can be shared by processes on different computers over a network.
* Server Process is slower than using shared memory.

## Exchanging Objects Between processes
2 types of communication channels are supported:
* Queue (FIFO)
* Pipe

## Pipes
A pipe can have only two endpoints, hence it is preferred over queue when only two-way communication is required.

## Multiprocessing Pipe
* Multiprocessing module provides Pipe() function which returns a pair of connection objects connected by a pipe.
* The two connection objects returned by Pipe() represent the two ends of the pipe.
* Each connection object has `send()` and `recv()` methods.

## Processes Synchronization
Process synchronization is defined as a mechanism which ensures that two or more concurrent processes do not simultaneously
execute some particular program segment known as `critical section` if it's not secure.

## Critical Section
* Critical section refers to the parts of the program where the shared resource is accessed.
* Critical section usage is not secure if there is write access.

## Race Condition
* Concurrent accesses to shared resource can lead to `race condition`.
* A race condition occurs when two or more processes can access shared data, and they try to change it at the same time.
As a result, the values of variables may be unpredictable and vary depending on the timing of context switches of the 
processes.
* One process can read the value while another changes it, this is one of the issues.

## Lock
* Multiprocessing has Lock class for locking code based on Semaphore.
* Semaphore is an object containing a value that should be checked by processes before accessing code.

## Process Pool
Proccess Pool is mechanism for controlling process automatically creating them and assigning tasks to them.

## Multithreading Pool
* Pool class represents pool of worker processes.
* User doesn't create processes explicitly
* We can implement Process Pool other with multiprocessing or concurrent.futures.