def find_Min_Difference(L, P):
    # If there aren't enough elements, we can't choose P elements
    if len(L) < P or P <= 0:
        return 0
    
    # Step 1: Sort the list
    L.sort()
    
    # Initialize the minimum difference with a very large value
    min_diff = float('inf')
    
    # Step 2 & 3: Slide a window of size P across the sorted list
    # The loop stops when the end of the window reaches the end of the list
    for i in range(len(L) - P + 1):
        # The window starts at index i and ends at index i + P - 1
        current_diff = L[i + P - 1] - L[i]
        
        # Update min_diff if we found a smaller spread
        if current_diff < min_diff:
            min_diff = current_diff
            
    return min_diff

# --- Example Testing ---
L = [3, 4, 1, 9, 56, 7, 9, 12, 13]
P = 5
print("Output:", find_Min_Difference(L, P))  # Expected Output: 6