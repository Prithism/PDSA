def odd_one(L):
    # Initialize a dictionary to count the occurrences of each data type
    type_counts = {'int': 0, 'float': 0, 'str': 0, 'bool': 0}
    
    # Iterate through the list and increment the respective type counter
    for item in L:
        if type(item) == int:
            type_counts['int'] += 1
        elif type(item) == float:
            type_counts['float'] += 1
        elif type(item) == str:
            type_counts['str'] += 1
        elif type(item) == bool:
            type_counts['bool'] += 1
            
    # Find and return the data type that appeared exactly once
    for data_type, count in type_counts.items():
        if count == 1:
            return data_type
        