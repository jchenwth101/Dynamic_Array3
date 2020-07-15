# Course: CS261 - Data Structures
# Student Name: Joel Chenoweth
# Assignment: bag_da.py portion in the dynamic_array cs261
# Description: This references bag data as bag() for dynamic array

from dynamic_array import *


class Bag:
    def __init__(self, start_bag=None):
        """
        Init new bag based on Dynamic Array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.da = DynamicArray()

        if start_bag is not None:
            for value in start_bag:
                self.add(value)

    def __str__(self) -> str:
        """
        Return content of bag in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "BAG: " + str(self.da.size) + " elements. "
        out += str(self.da.data[:self.da.size])
        return out

    def add(self, value: object) -> None:
        """
        this method adds object to bag via .append(value)
        """
        self.da.append(value)

    def remove(self, value: object) -> bool:
        """
       this method removes object from bag via .remove_at_index(index 'i')
        """

        for i in range(self.da.size):
            if self.da.data[i] == value:  # iteration of objects
                self.da.remove_at_index(i)
                return True
        return False

    def count(self, value: object) -> int:
        """
       this method counts the number of objects in the bag.  It iterates from an index
       in range function to return a value.  It establishes count before iterating an index
       in range returning an updated count
        """

        count = 0
        for index in range(self.da.size):
            if self.da.data[index] == value:
                count += 1

        return count

    def clear(self) -> None:
        """
        this method clears or empties all elements or values within the bag.  It iterates and removes
        objects in sequence.
        """

        for i in range(self.da.size - 1, -1, -1):
            self.da.remove_at_index(i)

    def size(self) -> int:
        """
       this function returns the size of the bag including all elements within the bag via  returning
       self.size
        """
        return self.da.size

    def equal(self, second_bag: object) -> bool:
        """
       this function evaluates the first bag to the contents of the second bag and determines if it is equal to the
       former
        """

        if self.size() != second_bag.size():
            return False

        # loop to look for elements in second_bag
        for i_1 in range(self.size()):
            present = False
            i_2 = 0
            while present == False and i_2 < second_bag.size():
                if self.da.data[i_1] == second_bag.da.data[i_2]:
                    present = True
                else:
                    i_2 += 1
            if not present:
                return False
        return True


# BASIC TESTING
if __name__ == "__main__":
    pass

# add example 1
# bag = Bag()
# print(bag)
# values = [10, 20, 30, 10, 20, 30]
# for value in values:
#   bag.add(value)
#  print(bag)

# remove example 1
# bag = Bag([1, 2, 3, 1, 2, 3, 1, 2, 3])
# print(bag)
# print(bag.remove(7), bag)
# print(bag.remove(3), bag)
# print(bag.remove(3), bag)
# print(bag.remove(3), bag)
# print(bag.remove(3), bag)
