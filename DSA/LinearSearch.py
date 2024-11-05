'''
ALGORITHM LinearSearch
1. Start.
2. Input array A and the element to search for (target).
3. Set found to false.
4. For each index i from 0 to length of A - 1:
    a. If A[i] is equal to target:
        i. Set found to true.
        ii. Print "Element found at index" i.
        iii. Break the loop.
5. If found is still false:
    a. Print "Element not found in the array."
6. End.
'''



def linear_search(array, target):
    found = False  # Step 3: Initialize found as False

    # Step 4: Iterate through the array
    for i in range(len(array)):
        # Step 4a: Check if the current element is the target
        if array[i] == target:
            found = True  # Step 4b.i: Set found to True
            print(f"Element found at index {i}.")  # Step 4b.ii
            break  # Step 4b.iii: Exit the loop

    # Step 5: Check if the element was not found
    if not found:
        print("Element not found in the array.")

# Example usage:
array = [5, 3, 8, 4, 2]
target = 4
linear_search(array, target)  # Should print "Element found at index 3."

target = 10
linear_search(array, target)  # Should print "Element not found in the array."
