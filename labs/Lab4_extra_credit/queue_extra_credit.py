# Author: Thomas Monfre
# Date: 11/8/17
# Course: Dartmouth College CS1, 17F
# Purpose: This program defines a class Queue that creates an object (list) in the form of a queue.

class Queue:
    # takes no given parameters for instance variables, because creating a Queue object simply makes an empty queue
    def __init__(self):
        self.queue = []

    # add item x to the queue
    def enqueue(self, x):
        self.queue.append(x)

    # remove and return an item to the queue if it isn't emtpy
    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            print("Queue is empty")

    # evaluate whether or not the queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # print the queue for the user
    def __str__(self):
        return str(self.queue)