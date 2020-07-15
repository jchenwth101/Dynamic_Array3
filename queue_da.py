# Course: CS261 - Data Structures
# Student Name: Joel Chenoweth
# Assignment: queue in dynamic array
# Description:  this provides a blueprint for adding a queue to a dynamic array by importing
#elements from dynamic array.py

from dynamic_array import *


class QueueException(Exception):
    """
    Custom exception to be used by Queue class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Queue:
    def __init__(self):
        """
        Init new queue based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "QUEUE: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def enqueue(self, value: object) -> None:
        """
        this method adds elements via .append() operation to the end of enqueue
        """
        self.da.append(value)

    def dequeue(self) -> object:
        """
        this method removes elements via. is_empty() operation to delete objects from the queue
        """

        if self.da.is_empty():
            raise QueueException
        first_element = self.da.get_at_index(0)
        self.da.remove_at_index(0)
        return first_element

    def is_empty(self) -> bool:
        """
        this method returns true if the queue is empty
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
        this method returns the size of the queue
        """
        return self.da.size

# BASIC TESTING
if __name__ == "__main__":
    pass

    # # enqueue example 1
    # q = Queue()
    # print(q)
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)

    # # dequeue example 1
    # q = Queue()
    # for value in [1, 2, 3, 4, 5]:
    #     q.enqueue(value)
    # print(q)
    # for i in range(6):
    #     try:
    #         print(q.dequeue())
    #     except Exception as e:
    #         print("No elements in queue", type(e))

    # # is_empty example 1
    # q = Queue()
    # print(q.is_empty())
    # q.enqueue(10)
    # print(q.is_empty())
    # q.dequeue()
    # print(q.is_empty())

    # # size example 1
    # q = Queue()
    # print(q.size())
    # for value in [1, 2, 3, 4, 5, 6]:
    #     q.enqueue(value)
    # print(q.size())