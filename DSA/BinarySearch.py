'''
ALGORITHM BinarySearch
1. Start.
2. Input sorted array A and the target element to search for.
3. Initialize left to 0 and right to length of A - 1.
4. While left is less than or equal to right:
    a. Set mid to (left + right) // 2.  // Calculate the middle index
    b. If A[mid] is equal to target:
        i. Print "Element found at index" mid.
        ii. Return (or exit).
    c. Else if A[mid] is less than target:
        i. Set left to mid + 1.  // Search in the right half
    d. Else:
        i. Set right to mid - 1.  // Search in the left half
5. Print "Element not found in the array."
6. End.
'''


def binary_search(array, target):
    # Step 3: Initialize left and right indices
    left = 0
    right = len(array) - 1

    # Step 4: While left is less than or equal to right
    while left <= right:
        # Step 4a: Calculate the middle index
        mid = (left + right) // 2

        # Step 4b: Check if the middle element is the target
        if array[mid] == target:
            print(f"Element found at index {mid}.")  # Step 4b.i
            return  # Exit the function
        
        # Step 4c: If the middle element is less than the target
        elif array[mid] < target:
            left = mid + 1  # Step 4c.i: Search in the right half
        # Step 4d: If the middle element is greater than the target
        else:
            right = mid - 1  # Step 4d.i: Search in the left half

    # Step 5: If the element was not found
    print("Element not found in the array.")  # Step 5

# Example usage:
sorted_array = [2, 3, 4, 5, 8]  # The array must be sorted
target = 5
binary_search(sorted_array, target)  # Should print "Element found at index 3."

target = 10
binary_search(sorted_array, target)  # Should print "Element not found in the array."
