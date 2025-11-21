try:
    with open("test.py", "r") as file:
        data = file.read()
    print(data)
except(FileNotFoundError):
    print("Invalid file name")
    
    
#         try
        
#         Error
#     no          yes 
# continue       except