# tuple, set, dictionary(map), list
# carry values - tuple

# single value is stored in each variable
age = 54
name = "superman"

# name, age, address, marks
stdTuple = ("Ramesh", 21, "Pune", 89)
#               0     1     2      3 -> index
#               1     2     3      4 -> position

print(type(stdTuple))
print(stdTuple)
# print(f"Name: {stdTuple[5]}") # IndexError: tuple index out of range
print(f"Score: {stdTuple[-1]}") 
lastIndex = len(stdTuple) - 1
print(f"Score: {stdTuple[lastIndex]}") 

# print(f"Student name is {stdTuple[0]} who is {stdTuple[1]} years old, lives in {stdTuple[2]} and scored {stdTuple[3]} score.")

stdTuple[0] = "Mahesh" # not possible
print(f"Name: {stdTuple[0]}")