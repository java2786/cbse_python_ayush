import json

std = {"name":"Himesh", "roll": 162, "marks": 74}

with open("std.json", "w") as file:
    json.dump(std, file)
    
print("Written successfully")


with open("std.json", 'r') as file:
    data = json.load(file)
    
print("Read is complete")
print(data)