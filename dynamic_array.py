#Course: CS261 - Data Structures
#Joel Chenoweth
#07-12-2020
#Dynamic Array
#Provides solutions for appending, sorting, resizing, getting, and removing new elements and data for
#Dynamic Arrays that evolve over time.

class DynamicArrayException(Exception):
    """
    Custom exception class to be used by Dynamic Array
    DO NOT CHANGE THIS METHOD IN ANY WAY
    """
    pass

class DynamicArray:
    def __init__(self, start_array=None):
        """
        Initialize new dynamic array
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        self.size = 0
        self.capacity = 4
        self.data = [None] * self.capacity

        # populate dynamic array with initial values (if provided)
        # before using this feature, implement append() method
        if start_array is not None:
            for value in start_array:
                self.append(value)

    def __str__(self) -> str:
        """
        Return content of dynamic array in human-readable form
        DO NOT CHANGE THIS METHOD IN ANY WAY
        """
        out = "DYN_ARR Size/Cap: "
        out += str(self.size) + "/"+ str(self.capacity)
        out += " " + str(self.data[:self.size])
        return out

    def resize(self, new_capacity: int) -> None:
        """This method will allow for an increase in size of data while current elements
        are copied/this provides capacity to change storage of underlying elements."""

        if not isinstance(new_capacity, int) or new_capacity < 1:
            return

        if new_capacity < self.size:
            return

        #1_a.1 creates list, references, alternative data via copy
        val = 0
        alt_data = [None] * new_capacity
        for i in range(self.size):
            alt_data[i] = self.data[i]
        self.capacity = new_capacity
        self.data = alt_data
        return

    def append(self, value: object) -> None:
        """this method allows for the repositioning of data while adding elements to the value
        if needed.  If internal storage is full, the capacity is increased by double."""
        if self.size == self.capacity:
           self.resize(self.capacity * 2)
           self.data[self.size] = value
           self.size += 1
        return

    def insert_at_index(self, index: int, value: object) -> None:
        """this method inserts elements specified by data as values/objects.  It is inserted at specified
        pos in array.  Index 0 refers to the beginning of the array."""
        if index < 0 or index > self.size:
            raise DynamicArrayException  #exception handle
        if self.size == self.capacity:
            self.resize(self.capacity * 2)
        for num in range(self.size, index - 1, -1):
            self.data[num] = self.data[num - 1]
        self.data[index] = value
        self.size += 1
        return


    def get_at_index(self, index: int) -> object:
        """this method returns object at index after integer argument is taken as input.  Index 0 refers
        to the beginning of the array"""
        if not isinstance(index, int) or index < 0 or index > self.size - 1:
            raise DynamicArrayException
        return self.data[index]

    def remove_at_index(self, index: int) -> None:
        """this removes object at index after integer argument is added as input.  Index 0 refers to
        beginning of array.  Elements stored is less than current capacity by no more than 10 elements"""
        if not isinstance(index, int) or index < 0 or index > self.size - 1:
            raise DynamicArrayException
        if self.capacity <= 10:
            pass
        elif self.size < (self.capacity / 4) and self.size * 2 >= 10:
            self.resize(self.size * 2)
        elif self.size < (self.capacity / 4) and self.size * 2 < 10:
            self.resize(10)
        for elt in range(index, self.size - 1, 1):
            self.data[elt] = self.data[elt + 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return

    def is_empty(self) -> bool:
        """this method returns determining if data is empty by indicating True or False.  It only returns true if
        there are "No" elements in the array."""
        if self.data[0] == None:
            return True
        else:
            return False

    def length(self) -> int:
        """this method determines the amount of objects/elements in stored array and returns the size in an integer."""
        return self.size

    def slice(self, start_index: int, quantity: int) -> object:
        """This method outputs Dynamic Array with consideration to arguments
        It contributes with integers from index and returns new Dynamic Array
        from previous Dynamic Array starting with element at start index."""
        if not isinstance(start_index, int) or start_index < 0 or start_index > self.size - 1:
            raise DynamicArrayException
        if (start_index + quantity - 1) > self.size - 1:
            raise DynamicArrayException
        end_index = start_index + quantity
        initializer = [self.data[i] for i in range(start_index, end_index, 1)]
        return DynamicArray(initializer)

    def reverse(self) -> None:
        """this method reverses the positions of objects in data"""
        swp_rnge = 0
        if self.size % 2 == 0:
            swp_rnge = int(self.size / 2)
        else:
            swp_rnge = int((self.size - 1) / 2)
        for i in range(swp_rnge):
            temp = self.data[i]
            self.data[i] = self.data[self.size - i - 1]
            self.data[self.size - i - 1] = temp
        return

    def sort(self):
        """this method sorts data for Dynamic Array in non descending order"""
        return


    def merge(self, another_list: object) -> None:
        """this method adds objects from input to current Dynamic Array it appends all elements from second array
        into the current array in the same order as they are stored."""
        # for loop to iterate through data to add/append Dynamic Array
        for i in range(another_list.size):
            self.append(another_list.data[i])
        return



# BASIC TESTING
if __name__ == "__main__":
    pass

    # resize - example 1
    da = DynamicArray()
    print(da.size, da.capacity, da.data)
    da.resize(10)
    print(da.size, da.capacity, da.data)
    da.resize(2)
    print(da.size, da.capacity, da.data)
    da.resize(0)
    print(da.size, da.capacity, da.data)

    # # resize - example 2
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8])
    # print(da)
    # da.resize(20)
    # print(da)
    # da.resize(4)
    # print(da)

    # # append - example 1
    # da = DynamicArray()
    # print(da.size, da.capacity, da.data)
    # da.append(1)
    # print(da.size, da.capacity, da.data)
    # print(da)

    # # append - example 2
    # da = DynamicArray()
    # for i in range(9):
    #     da.append(i + 101)
    #     print(da)
    #
    # # append - example 3
    # da = DynamicArray()
    # for i in range(600):
    #     da.append(i)
    # print(da.size)
    # print(da.capacity)

    # # insert_at_index - example 1
    # da = DynamicArray([100])
    # print(da)
    # da.insert_at_index(0, 200)
    # da.insert_at_index(0, 300)
    # da.insert_at_index(0, 400)
    # print(da)
    # da.insert_at_index(3, 500)
    # print(da)
    # da.insert_at_index(1, 600)
    # print(da)

    # # insert_at_index example 2
    # da = DynamicArray()
    # try:
    #     da.insert_at_index(-1, 100)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # da.insert_at_index(0, 200)
    # try:
    #     da.insert_at_index(2, 300)
    # except Exception as e:
    #     print("Exception raised:", type(e))
    # print(da)

    # # insert at index example 3
    # da = DynamicArray()
    # for i in range(1, 10):
    #     index, value = i - 4, i * 10
    #     try:
    #         da.insert_at_index(index, value)
    #     except Exception as e:
    #         print("Can not insert value", value, "at index", index)
    # print(da)

    # # get_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50])
    # print(da)
    # for i in range(4, -1, -1):
    #     print(da.get_at_index(i))

    # # get_at_index example 2
    # da = DynamicArray([100, 200, 300, 400, 500])
    # print(da)
    # for i in range(-1, 7):
    #     try:
    #         print("Index", i, ": value", da.get_at_index(i))
    #     except Exception as e:
    #         print("Index", i, ": exception occured")

    # # remove_at_index - example 1
    # da = DynamicArray([10, 20, 30, 40, 50, 60, 70, 80])
    # print(da)
    # da.remove_at_index(0)
    # print(da)
    # da.remove_at_index(6)
    # print(da)
    # da.remove_at_index(2)
    # print(da)

    # # remove_at_index - example 2
    # da = DynamicArray([1024])
    # print(da)
    # for i in range(17):
    #     da.insert_at_index(i, i)
    # print(da.size, da.capacity)
    # for i in range(16, -1, -1):
    #     da.remove_at_index(0)
    # print(da)

    # # remove_at_index - example 3
    # da = DynamicArray()
    # print(da.size, da.capacity)
    # [da.append(1) for i in range(100)]          # step 1 - add 100 elements
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(68)]  # step 2 - remove 69 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                      # step 3 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 4 - remove 1 element
    # print(da.size, da.capacity)
    # [da.remove_at_index(0) for i in range(14)]  # step 5 - remove 14 elements
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 6 - remove 1 element
    # print(da.size, da.capacity)
    # da.remove_at_index(0)                       # step 7 - remove 1 element
    # print(da.size, da.capacity)
    #
    # for i in range(14):
    #     print("Before remove_at_index(): ", da.size, da.capacity, end="")
    #     da.remove_at_index(0)
    #     print(" After remove_at_index(): ", da.size, da.capacity)

    # # is_empty - example 1
    # da = DynamicArray()
    # print(da.is_empty(), da)
    # da.append(100)
    # print(da.is_empty(), da)
    # da.remove_at_index(0)
    # print(da.is_empty(), da)

    # # length - example 1
    # da = DynamicArray()
    # print(da.length())
    # for i in range(10000):
    #     da.append(i)
    # print(da.length())
    # for i in range(9999, 5000, -1):
    #     da.remove_at_index(i)
    # print(da.length())

    # # slice example 1
    # da = DynamicArray([1, 2, 3, 4, 5, 6, 7, 8, 9])
    # da_slice = da.slice(1, 3)
    # print(da, da_slice, sep="\n")
    # da_slice.remove_at_index(0)
    # print(da, da_slice, sep="\n")

    # slice example 2
    # da = DynamicArray([10, 11, 12, 13, 14, 15, 16])
    # print("SOUCE:", da)
    # slices = [(0, 7), (-1, 7), (0, 8), (2, 3), (5, 0), (5, 3)]
    # for i, cnt in slices:
    #     print("Slice", i, "/", cnt, end="")
    #     try:
    #         print(" --- OK: ", da.slice(i, cnt))
    #     except:
    #         print(" --- exception occurred.")

    # # merge example 1
    # da = DynamicArray([1, 2, 3, 4, 5])
    # da2 = DynamicArray([10, 11, 12, 13])
    # print(da)
    # da.merge(da2)
    # print(da)

    # merge example 2
    # da = DynamicArray([1, 2, 3])
    # da2 = DynamicArray()
    # da3 = DynamicArray()
    # da.merge(da2)
    # print(da)
    # da2.merge(da3)
    # print(da2)
    # da3.merge(da)
    # print(da3)

    # # reverse example 1
    # da = DynamicArray([4, 5, 6, 7, 8, 9])
    # print(da)
    # da.reverse()
    # print(da)
    # da.reverse()
    # print(da)

    # # reverse example 2
    # da = DynamicArray()
    # da.reverse()
    # print(da)
    # da.append(100)
    # da.reverse()
    # print(da)

    # sort example 1
    #da = DynamicArray([1, 10, 2, 20, 3, 30, 4, 40, 5])
    #print(da)
    #da.sort()
    #print(da)
