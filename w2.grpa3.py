def mergeInPlace(A, B):
    n = len(A)
    m = len(B)

    # Iterate through every element of A
    for i in range(n):
        # Compare current element of A with the smallest element of B
        if A[i] > B[0]:
            # Swap them so the smaller value goes into A
            A.swap(i, B, 0)
            
            # Re-sort B to move the new B[0] to its correct position
            # This maintains B as a sorted list
            first = B[0]
            k = 1
            while k < m and B[k] < first:
                B.swap(k - 1, B, k)
                k += 1
