'''
ALGORITHM DeleteKthElementFromLinearArray
1. Set ITEM := LA[K].
2. Repeat for J = K to N - 1:
    // Move J+1st element upward
    Set LA[J] := LA[J + 1].  // End of loop.
3. // Reset the number N of elements in LA
   Set N := N - 1.
4. Exit.
'''




def delete_kth_element(LA, K, N):
    # Step 1: Store the item to be deleted
    ITEM = LA[K]
    
    # Step 2: Move elements upward
    for J in range(K, N - 1):
        LA[J] = LA[J + 1]  # Move the next element to the current position
    
    # Step 3: Decrease the size of the array
    N -= 1
    
    # Optional: Return the updated array and new size
    return LA[:N], N

# Example usage:
LA = [10, 20, 30, 40, 50]  # Initial array
K = 2                       # Index of element to delete (0-based index)
N = len(LA)                 # Current number of elements in LA

updated_LA, new_N = delete_kth_element(LA, K, N)

print("Updated Array:", updated_LA)
print("New Size of Array:", new_N)
