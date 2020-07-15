# Course: CS261 - Data Structures
# Student Name: Joel Chenoweth
# Assignment: dynamic array
# Description: Stack evaluates the class Stack within the dynamic array allocating for data
# to be pushed or popped to the top


from dynamic_array import *


class StackException(Exception):
    """
    Custom exception to be used by Stack class
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass


class Stack:
    def __init__(self):
        """
        Init new stack based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

    def __str__(self) -> str:
        """
        Return content of stack in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "STACK: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def push(self, value: object) -> None:
        """
        this method adds elements to the stack(top) via .append(value)
        """
        self.da.append(value)

    def pop(self) -> object:
        """
       this method removes/returns element from the stack of elements
        """

        if self.da.is_empty():
            raise StackException
        return_object = self.da.get_at_index(self.da.size - 1) #returns object
        self.da.remove_at_index(self.da.size - 1)#removes object
        return return_object

    def top(self) -> object:
        """
       this method returns element to the top of the stack via.is_empty()
        """

        if self.da.is_empty():
            raise StackException
        return self.da.get_at_index(self.da.size - 1)

    def is_empty(self) -> bool:
        """
       this method returns true (bool) if stack is empty via. is_empty()
        """
        return self.da.is_empty()

    def size(self) -> int:
        """
      this method returns the value of elements(or size of elements) via self.size
        """
        return self.da.size


# BASIC TESTING
if __name__ == "__main__":
    pass

    # # push example 1
    # s = Stack()
    # print(s)
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s)

    # # pop example 1
    # s = Stack()
    # try:
    #     print(s.pop())
    # except Exception as e:
    #     print("Exception:", type(e))
    #
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    #
    # for i in range(6):
    #     try:
    #         print(s.pop())
    #     except Exception as e:
    #         print("Exception:", type(e))

    # # top example 1
    # s = Stack()
    # try:
    #     s.top()
    # except Exception as e:
    #     print("No elements in stack", type(e))
    # s.push(10)
    # s.push(20)
    # print(s)
    # print(s.top())
    # print(s.top())
    # print(s)

    # # is_empty example 1
    # s = Stack()
    # print(s.is_empty())
    # s.push(10)
    # print(s.is_empty())
    # s.pop()
    # print(s.is_empty())

    # # size example 1
    # s = Stack()
    # print(s.size())
    # for value in [1, 2, 3, 4, 5]:
    #     s.push(value)
    # print(s.size())
