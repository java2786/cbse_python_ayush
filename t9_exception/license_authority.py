try:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    if(age>=18 and age<=75):
        print("License applied successfully")
    else:
        raise ValueError("Invalid age, valid range (18 - 75)")
except ValueError as e:
    print(f"License failed: {e}")
else:
    print("no error")
finally:
    pass    