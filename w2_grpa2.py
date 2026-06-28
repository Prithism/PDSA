def findLargest(L):
    low = 0
    high = len(L) - 1
    
    # If the list is not rotated at all or has one element
    if L[low] <= L[high]:
        return L[high]
    
    while low <= high:
        mid = (low + high) // 2
        
        # If mid is the largest (next element is smaller)
        if mid < len(L) - 1 and L[mid] > L[mid + 1]:
            return L[mid]
        
        # If mid-1 is the largest (mid is the smallest)
        if mid > 0 and L[mid] < L[mid - 1]:
            return L[mid - 1]
        
        # Decide which half to search
        if L[mid] > L[low]:
            # Largest must be in the right half
            low = mid + 1
        else:
            # Largest must be in the left half
            high = mid - 1
            
    return L[low]
