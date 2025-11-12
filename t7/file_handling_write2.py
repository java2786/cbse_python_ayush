# relative path
filename = 't7/student.csv'

# 'w' is used to open file in write mode but it makes file empty and then write
# mode = 'w'

# 'a' is append mode
mode = 'a'
with open(filename, mode) as f_obj:
    # f_obj.write("Name,Roll\n")
    f_obj.write("Ramesh,815\n")
    
