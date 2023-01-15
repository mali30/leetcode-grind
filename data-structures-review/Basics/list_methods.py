my_list = [1,2,3,4]
print(my_list[0])
print(my_list[-1])

# checks if a number in the array
if 1 in my_list:
    print("YES")


# range - prints up to but no including that number

for val in range(my_list[0], len(my_list)):
    print(val)

# append - adds whatever passed in to the end of the array
my_list.append("MOHAMED")
print(my_list)

# insert - will insert based on index passed
my_list.insert(0,"I was here")
print(my_list)

# extend - adds list of elements to the end
my_list.extend([7,8,9])
print(my_list)

# sort - changes the actual list and returns a new one
my_list.sort()


# sorted - doens't change original list so you must store it
print(" now sorted" , sorted(my_list))
print("original list" , my_list)


# revesre - reverse in place. does not return not return it
last_list = [1,2,3,4]
new_list = last_list.reverse()
print("The reversed list is" , last_list)

# reversed - returns a reversed list. returns an iterator so loop over
another_list = [1,2,3,4]
my_rev = reversed(another_list)
for val in my_rev:
    print(val)


