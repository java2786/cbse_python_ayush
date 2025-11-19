import pickle

# read binary -> mode -> rb
with open('students.dat', 'rb') as file:
    data = pickle.load(file)
    
# print(data)
for student in data:
    if(student['marks']>80):
        print(student)