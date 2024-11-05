'''
ALGORITHM InsertIntoLinearArray
1. [Initialize counter.] Set J := N.
2. Repeat Steps 3 and 4 while J >= K.
3. [Move Jth element downward.] Set LA[J + 1] := LA[J].
4. [Decrease counter.] Set J := J - 1. [End of Step 2 loop.]
5. [Insert element.] Set LA[K] := ITEM.
6. [Reset N.] Set N := N + 1.
7. Exit.
'''





def insert_element(array, size, maxSize, element, position):
    # Check if the array is full
    if size == maxSize:
        print("Array is full")
        return size  # Size remains unchanged if no insertion

    # Check if position is valid
    if position < 0 or position > size:
        print("Invalid position")
        return size  # Size remains unchanged if no insertion

    # Shift elements to the right from the last element up to the position
    for i in range(size - 1, position - 1, -1):
        array[i + 1] = array[i]

    # Insert the element at the given position
    array[position] = element
    size += 1  # Update the size
    print("Element inserted")
    return size  # Return the updated size of the array

# Example usage
maxSize = 10
array = [1, 2, 4, 5, 6, None, None, None, None, None]  # Initialized array with maxSize
size = 5  # Current size
element = 3
position = 2

size = insert_element(array, size, maxSize, element, position)
print("Updated array:", array[:size])  # Output only the used portion of the array
