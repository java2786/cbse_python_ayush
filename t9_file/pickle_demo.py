import pickle

stds = [
    {"name":"Ramesh", "roll": 73, "marks": 91},
    {"name":"Mukesh", "roll": 182, "marks": 63},
    {"name":"Mahesh", "roll": 312, "marks": 87},
    {"name":"Himesh", "roll": 162, "marks": 74},
]

# write binary -> mode -> wb
with open("students.dat", 'wb') as file:
    pickle.dump(stds, file)
    
print("Data written successfully")