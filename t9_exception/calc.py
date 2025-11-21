try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    
    with open("test.py", "r") as file:
        # num1 = file.read()
        pass

    task = input("Enter task: ")
    result = 0
    if(task=="+"):
        result = num1+num2
        print("Sum:",result)
    elif(task=="*"):
        result = num1*num2
        print("Mul:",result)
    elif(task=="/"):
        result = num1/num2
        print("Div:",result)
    else:
        print("Invalid task")

    # with open("test.py", "w") as file:
    #     file.write(f"{result}")
        
except(ValueError):
    print("Invalid input")
except(ZeroDivisionError):
    print("Can not divide by zero")
except:
    print("Some other error occurred")