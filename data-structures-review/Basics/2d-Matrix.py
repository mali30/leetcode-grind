my_arr = [ [1,2,3], [4,5,6] , [7,8,9]  ]

# prints 2d matrix
for row in range(len(my_arr)):
    for col in range(len(my_arr[row])):
        print(my_arr[row][col])

# another way to print

for row in my_arr:
    for elem in row:
        print(elem , end=" ")
    print()


my_arr = [ [1,2,3] , [4,5,6] , [7,8,9]]

for row in my_arr:
    for col in row:
        print(col, end = '' )
    print()

# calculate sum of arrays

ans = 0
for row in my_arr:
    for col in row:
        ans += col
print(ans)