# import _thread
# import time


# def thread_task(threadName, delay):
#     for count in range(1,6):
#         time.sleep(delay)
#         print("ThreadName: {}, count: {}".format(threadName,count))
    

# try:
#     _thread.start_new_thread(thread_task, ("thread-1",2,))
#     _thread.start_new_thread(thread_task,("thread-2",4))
# except:
#     print("Error: unable to start thread")
# while True:
#     pass

# import threading

# # Define a custom thread class
# class myThread(threading.Thread):
#     def __init__(self, name):
#         threading.Thread.__init__(self)
#         self.name = name

#     # Override the run method to define the thread's behavior
#     def run(self):
#         print("Thread name: {}".format(self.name))

# # Create an instance of the custom thread class
# thread1 = myThread("Thread-1")

# # Start the thread
# thread1.start()














# import threading
# import time

# def print_numbers():
#     for i in range(5):
#         time.sleep(1)
#         print(i)

# def print_letters():
#     for letter in 'ABCDE':
#         time.sleep(1)
#         print(letter)

# # Create two threads
# thread1 = threading.Thread(target=print_numbers)
# thread2 = threading.Thread(target=print_letters)

# # Start the threads
# thread1.start()
# thread2.start()

# # Wait for both threads to finish
# thread1.join()
# thread2.join()






# from ast import arg
# import threading
# import time
# from tracemalloc import start 

# def print_odd_number():
#     for i in range(1,10,2):
#         time.sleep(1)
#         print("Odd Number: ",i)

# def print_even_number():
#     for i in range(2,10,2):
#         time.sleep(1)
#         print("Even Number: ",i)

# thread1 = threading.Thread(target=print_odd_number)
# thread2 = threading.Thread(target=print_even_number)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()






# import threading
# import time 


# def countdownTimer(start):
#     while start > 0:
#         time.sleep(1)
#         print("Countdown: ", start)
#         start -= 1

# thread1 = threading.Thread(target=countdownTimer, args=(10,))


# thread1.start()

# thread1.join()




# import threading
# import time 


# def task_a():
#     for i in range(3):
#         time.sleep(1)
#         print("task A - Step: ", i)

# def task_b():
#     for i in range(5):
#         time.sleep(1)
#         print("task B - Step: ",i)


# thread1 = threading.Thread(target=task_a)
# thread2 = threading.Thread(target=task_b)

# thread1.start()
# thread2.start()

# thread1.join()
# thread2.join()



# import sched
# import time 

# scheduler = sched.scheduler(time.time,time.sleep)

# def scheduler_event(name,start):
#     now = time.time()
#     elapsed = int(now - start)
#     print("elapsed: ",elapsed, "name: ",name)

# start = time.time()
# print("START: ", time.ctime(start))
# scheduler.enter(2,1,scheduler_event,("EVENT_1",start))
# scheduler.enter(5,1,scheduler_event,("EVENT_2",start))
# scheduler.run()

# from time import sleep
# from random import random, randint
# from threading import Thread
# from queue import PriorityQueue

# queue = PriorityQueue()

# def producer(queue):
#    print('Producer: Running')
#    for i in range(5):

#       # create item with priority
#       value = random()
#       priority = randint(0, 5)
#       item = (priority, value)
#       queue.put(item)
#    # wait for all items to be processed
#    queue.join()

#    queue.put(None)
#    print('Producer: Done')

# def consumer(queue):
#    print('Consumer: Running')

#    while True:

#       # get a unit of work
#       item = queue.get()
#       if item is None:
#          break

#       sleep(item[1])
#       print(item)
#       queue.task_done()
#    print('Consumer: Done')

# producer = Thread(target=producer, args=(queue,))
# producer.start()

# consumer = Thread(target=consumer, args=(queue,))
# consumer.start()

# producer.join()
# consumer.join()




# import socket
# server = socket.socket()

# server.bind(('localhost',12345))
# server.listen()

# client, addr = server.accept()
# print("connection request from : "+  str(addr))
# host = "127.0.0.1"
# port = 3800
# obj = socket.socket()
# obj.connect((host,port))
# client.send(bytes)
# client.recv(bytes)



# import socket 
# host = "127.0.0.1"
# port = 3000
# server = socket.socket()
# server.bind((host,port))
# server.listen()
# conn,addr = server.accept()
# print("Connection from: "+ str(addr))
# while True:
#     data = conn.recv(1024).decode()
#     if not data:
#         break
#     data = str(data).upper()
#     print(" from Client:"+ str(addr))
#     data = input("type message: ")
#     conn.send(data.encode())
# conn.close()




# from email import message
# import socket 
# host = "127.0.0.1"
# port = 3000
# obj = socket.socket()
# obj.connect((host,port))
# message = input("type message: ")   
# while message != 'q':
#     obj.send(message.encode())
#     data = obj.recv(1024).decode()
#     print("Received from server: "+ data)
#     message = input("type message: ")
# obj.close()

import socket

# Create a socket object
s = socket.socket()

# Set the server host and port
host = "127.0.0.1"
port = 5001

# Connect to the server
s.connect((host, port))

# Send a message to the server
s.send("Hello server!".encode())

# Open a file to write received data
with open('recv.txt', 'wb') as f:
    while True:
        print('Receiving data...')
        data = s.recv(1024)
        if not data:
            break
        f.write(data)

print('Successfully received')

# Close the file and socket
f.close()
s.close()

print('Connection closed')
