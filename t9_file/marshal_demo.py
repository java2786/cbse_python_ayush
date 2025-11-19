import marshal

isWrite = False 

# write
if(isWrite):
    scores = [92, 89, 73, 85, 93]
    with open("scores.dat", "wb") as file:
        marshal.dump(scores, file)

    print("Data is written successfully")

# read
else:
    with open("scores.dat", "rb") as file:
        data = marshal.load(file)
    
    print(data)