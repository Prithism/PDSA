def sortInRange(L, r):
    """
    Sorts a list L of integers in place, where all elements are in the range [0, r).
    Achieves O(n + r) time complexity using Counting Sort logic.
    """
   
    count = [0] * r

        count[num] += 1

    
    insert_idx = 0
    for i in range(r):
      
        while count[i] > 0:
            L[insert_idx] = i
            insert_idx += 1
            count[i] -= 1


if __name__ == "__main__":
    L = [2, 0, 1, 1, 2, 3, 0, 2, 1, 0, 2, 3, 1, 2]
    r = 4
    
    print(f"Original L: {L}")
    
    sortInRange(L, r)
    
    print(f"Sorted L:   {L}")