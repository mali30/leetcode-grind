def mergeSort(arr_to_sort):
    print('spliting', arr_to_sort)

    if len(arr_to_sort) > 1:
        middle = len(arr_to_sort) // 2

        lefthalf = arr_to_sort[:middle]
        righthalf = arr_to_sort[middle:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i,j,k = 0,0,0

        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                arr_to_sort[k] = lefthalf[i]
                i+=1
                
            else:
                arr_to_sort[k] = righthalf[j]
                j+=1
            k+=1


        while i < len(lefthalf):
            arr_to_sort[k] = lefthalf[i]
            i+=1
            k+=1
        while j < len(righthalf):
            arr_to_sort[k] = righthalf[j]
            j+=1
            k+=1

    print('merging list' , arr_to_sort)

my_list = [54,21,45,67,88,54,32,11,21]
my_sorted = mergeSort(my_list)
print(my_sorted)


my name is jim and this is my story I am a very nice guy and I really like to type fast 
















