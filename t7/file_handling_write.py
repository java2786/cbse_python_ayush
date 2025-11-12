# relative path
filename = 't7/abc.txt'

# 'w' is used to open file in write mode but it makes file empty and then write
# mode = 'w'

# 'a' is append mode
mode = 'a'
with open(filename, mode) as f_obj:
    f_obj.write("This is from python.\n")
    f_obj.write("This is from python again.\n")
    
