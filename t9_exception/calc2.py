isError = True

while isError==True:
    try:
        num1 = int(input("Enter first number: "))
        num2 = int(input("Enter second number: "))

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
        isValid = True
    except(ValueError):
        print("Invalid input, please try again")
        isValid = False
    except(ZeroDivisionError):
        print("Can not divide by zero, please try again")
        isValid = False
    except:
        print("Some other error occurred")
        isValid = False
    finally:
        if isValid == True:
            isError = False
        else:
            isError = True