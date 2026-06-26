def combinationSort(strList):
    
    L1 = sorted(strList, key=lambda x: x[0])

    # L2: Sort by letter (ascending), then by the remaining number (descending).
    # We convert the slice after the first character to an integer for numerical sorting.
    L2 = sorted(strList, key=lambda x: (x[0], -int(x[1:])))

    return L1, L2

# Example Usage:
input_list = ["d34", "g54", "d12", "b87", "g1", "c65", "g40", "g5", "d77"]
L1, L2 = combinationSort(input_list)

print("L1:", ", ".join(L1))
print("L2:", ", ".join(L2))
