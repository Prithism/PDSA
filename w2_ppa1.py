def binarySearchIndexAndComparisons(L, k):
    left = 0
    right = len(L) - 1
    numComparisons = 0
    
    while left <= right:
        numComparisons += 1
        mid = (left + right) // 2
        
        if L[mid] == k:
            return (True, numComparisons)
        elif L[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
            
    return (False, numComparisons)
