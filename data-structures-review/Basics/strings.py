statement = "welcome to python"
print(statement)

# Capitalize - capitalizes first letter
print(statement.capitalize())

# lowercase version of string
all_uppercase = "ALLCAP"
print(all_uppercase.lower())

# capitalize all letters 
make_upper = "make me upper"
print(make_upper.upper())

all_lowercase = "lower"
# tells you if their are alphabetic charactes in the string
print(all_lowercase.isalpha())

# isdigiti()
# isspace

# check if string starts with paramter
print(all_lowercase.startswith("all"))

# check if string ends with paramater
print(all_lowercase.endswith("cap"))

# will return the first index of paramater passed
print(all_lowercase.find("cap"))

# replacs what you have with what you want
print(all_lowercase.replace("cap" , "HELLO"))

# joins elements in the given list together
another_string = "abc123"
print(another_string.join(["okay we are joing" , "456"]))

dummy_string = "hello there"
if "hello" in dummy_string:
    print("okay you got me")


# LeetCode Remove Vowels from a String
# Time Complexity: O(N^2) 
# Space Complexity: O(N)
def removeVowels(my_string):
    if my_string is None or my_string is "":
        return "I am empty"
    my_vowels = ["a","e","i","o","u"]
    iter = list(my_string)
    new_string = ""
    for val in iter:
        if val in my_vowels:
            new_string = iter.remove(val)
            return new_string
    return iter

print(removeVowels("aeiou"))
print(removeVowels("bcdfghjk"))
print(removeVowels(""))


more_strings = "abcde"

print(more_strings.upper())
print(more_strings.lower())
print(more_strings.startswith("b"))
print(more_strings.endswith("z"))
if 'a' in more_strings:
    print("yes")

print(more_strings.title())

print(more_strings.count("a"))


#############
my_name = "Mohamed"
print(my_name)

print(my_name.lower())
print(my_name.upper())
print(my_name.isalpha())
print(my_name.capitalize())
print(my_name.endswith("d"))
print(my_name.startswith("a"))
print(my_name.strip())
replace_me = "I like food"
print(replace_me.replace("food", "chicken"))

