def binSearch(arr,target):
    start = 0 
    end = len(arr) - 1
    found = False 
    while start <= end and not found:
        mid = (start + end) // 2
        if arr[mid] == target:
            found = True 
        if target < arr[mid]:
            end = mid - 1
        if target > arr[mid]:
            start = mid + 1
    return found 

print(binSearch([1,2,3,4,5] , 10))