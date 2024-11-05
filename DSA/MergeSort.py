'''
ALGORITHM MergeSort(A)
1. Start.
2. If length of A <= 1:
    a. Return A.
3. Set mid = length of A // 2.
4. Set leftHalf = MergeSort(A[0:mid]).
5. Set rightHalf = MergeSort(A[mid:]).
6. Return Merge(leftHalf, rightHalf).

ALGORITHM Merge(left, right)
1. Start.
2. Create an empty list result.
3. While left and right are not empty:
    a. If left[0] <= right[0]:
        i. Append left[0] to result.
        ii. Remove left[0] from left.
    b. Else:
        i. Append right[0] to result.
        ii. Remove right[0] from right.
4. Append remaining elements of left or right to result.
5. Return result.
6. End.
'''


def merge_sort(arr):
    if len(arr) <= 1:  # Base case: if the list is empty or has one element
        return arr

    mid = len(arr) // 2  # Find the middle index
    left_half = merge_sort(arr[:mid])  # Recursively sort the left half
    right_half = merge_sort(arr[mid:])  # Recursively sort the right half

    return merge(left_half, right_half)  # Merge the sorted halves

def merge(left, right):
    result = []  # Resulting list to hold the merged output
    while left and right:  # While both halves have elements
        if left[0] <= right[0]:  # Compare the first elements
            result.append(left.pop(0))  # Append the smaller element
        else:
            result.append(right.pop(0))  # Append the smaller element

    # Append any remaining elements from left or right
    result.extend(left)
    result.extend(right)

    return result  # Return the merged list

# Example usage
if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("Original array:", data)
    sorted_data = merge_sort(data)
    print("Sorted array:", sorted_data)
