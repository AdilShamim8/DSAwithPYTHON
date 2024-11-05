'''
ALGORITHM QuickSort(A, low, high)
1. Start.
2. If low < high:
    a. Set pivotIndex = Partition(A, low, high).
    b. QuickSort(A, low, pivotIndex - 1).  // Recursively sort the left sub-array
    c. QuickSort(A, pivotIndex + 1, high). // Recursively sort the right sub-array
3. End.

ALGORITHM Partition(A, low, high)
1. Start.
2. Set pivot = A[high]. // Choose the last element as pivot
3. Set i = low - 1. // Index of smaller element
4. For j = low to high - 1:
    a. If A[j] < pivot:
        i = i + 1.
        Swap A[i] with A[j].
5. Swap A[i + 1] with A[high] // Move pivot to its correct position
6. Return i + 1.
7. End.
'''



def quick_sort(arr, low, high):
    if low < high:
        # Partition the array and get the pivot index
        pivot_index = partition(arr, low, high)
        # Recursively sort the elements before and after partition
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1  # Pointer for the smaller element

    for j in range(low, high):
        if arr[j] < pivot:  # If current element is smaller than or equal to pivot
            i += 1  # Increment index of smaller element
            arr[i], arr[j] = arr[j], arr[i]  # Swap

    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Swap the pivot element with the element at i+1
    return i + 1  # Return the partitioning index

# Example usage
if __name__ == "__main__":
    data = [10, 7, 8, 9, 1, 5]
    print("Original array:", data)
    quick_sort(data, 0, len(data) - 1)
    print("Sorted array:", data)
