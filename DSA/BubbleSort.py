'''
ALGORITHM BubbleSort(A)
1. Start.
2. Set n = length of A.
3. For i from 0 to n-1:
    a. Set swapped = false.
    b. For j from 0 to n-i-2:
        i. If A[j] > A[j+1]:
            1. Swap A[j] and A[j+1].
            2. Set swapped = true.
    c. If swapped = false:
        Break the loop (the array is sorted).
4. End.
'''



def bubble_sort(arr):
    n = len(arr)  # Get the length of the array
    for i in range(n):
        swapped = False  # Flag to detect if a swap occurred
        for j in range(0, n - i - 1):  # Last i elements are already sorted
            if arr[j] > arr[j + 1]:  # Compare adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap if in wrong order
                swapped = True  # Set the flag to True since a swap occurred
        if not swapped:  # If no swaps occurred, the array is sorted
            break

# Example usage
if __name__ == "__main__":
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", data)
    bubble_sort(data)
    print("Sorted array:", data)
