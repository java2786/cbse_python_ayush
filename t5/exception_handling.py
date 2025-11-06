def div1(x,y):
    return x/y
    
# print(div1(5,0))

# ************
def div2(x,y):
    if y==0:
        return "Not Defined"
    else:
        return x/y
    
print(div2(5,0))


# ************
def div3(x,y):
    result = 0
    try:
        result = x/y
        print("div is successfully done")
    except ZeroDivisionError:
        return "Undefined"
    else:
        return result
    
print(div3(5,1))
print(div3(5,0))

# ************
def div4():
    
    result = 0
    try:
        x = int(input("Enter first number: ")) # 'five'
        y = int(input("Enter second number: "))
        result = x/y
        print("div is successfully done")
    except ValueError:
        print("Invalid input")
        return None
    except ZeroDivisionError:
        return "Undefined"
    else:
        return result


print(div4())
