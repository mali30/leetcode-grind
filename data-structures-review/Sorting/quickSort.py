def quickSort(sequence):

    if len(sequence) <= 1:
        return sequence
    else:
        pivot = sequence.pop()

    low_list, high_list = [],[]
    for val in sequence:
        if val > pivot:
            high_list.append(val)
        else:
            low_list.append(val)
    
    return quickSort(low_list) + [pivot] + quickSort(high_list)

print(quickSort([4,5,2,8,7,1,4,9,0,5]))