from collections import defaultdict

my_dict = {'Mohamed':24, "Location" : "ATL"}
print(my_dict['Mohamed'])
print(my_dict['Location'])

# Update a value
my_dict['Location'] = "Stone Mountain"
my_dict['Favorite Sport'] = "Soccer"
print(my_dict["Location"])
print(my_dict['Favorite Sport'])

# Delete a value in a dictionary
del my_dict['Mohamed']
# print(my_dict['Mohamed'])

# removes all entries in dict
# my_dict.clear()
print(my_dict)

print('mohamed' in my_dict)

print(sorted(my_dict))

# Loop through a dictionary
another_dict = {'Ali' : 'Ahmed', "Age" : 22, "Favorite Food" : "Rice"}

# loop through keys
for keys in another_dict:
    print(keys)

print("######")

# loop though values
for values in another_dict.values():
    print(values)

# Loop through keys and values

for key,values in another_dict.items():
    print(key, values)
    

my_family_dict = {"Mohamed": 25}
print(my_family_dict)
my_family_dict["Mohamed"] = 26
print(my_family_dict)

for val in my_family_dict:
    print(val)

for val in my_family_dict.values():
    print(val)

for key, value in my_family_dict.items():
    print(key, value)

my_family_dict.pop("Mohamed")
print(my_family_dict)


default = defaultdict(set)
default['name'] = ('moe', 28)
print('default', default)

for key, value in default.items():
    print(key, value)
