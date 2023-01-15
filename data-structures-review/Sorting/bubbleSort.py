def bubbleSort(input_array):
    for row in range(len(input_array) - 1, 0 , -1):
        for col in range(row):
            if input_array[col] > input_array[col + 1]:
                temp = input_array[col]
                input_array[col] = input_array[col + 1]
                input_array[col + 1] = temp
    return input_array

ll = [8,7,4,9,1,2]
print(bubbleSort(ll))