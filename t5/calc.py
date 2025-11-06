def add(x,y):
    return x+y
    
sum = add(4,5)
print(sum)


def mul(x,y):
    print(x*y)
    
mul(4,6)

print("***************")
def calculate(a,b,operator):
    if operator == '+':
        return a+b
    elif operator == '-':
        return a-b
    elif operator == '*':
        return a*b
    elif operator == '/':
        return a/b
    elif operator == '//':
        return a//b
    elif operator == '^':
        # 2^5
        return a**b
    else:
        print("Invalid operator")
        return 0

print(calculate(3,2,'+')) # 5
print(calculate(3,2,'-')) # 1
print(calculate(3,2,'*')) # 6
print(calculate(3,2,'/')) # 1.5
print(calculate(3,2,'//')) # 1
print(calculate(3,2,'^')) # 9
print(calculate(3,2,'%')) # 5



# print(calculate(3,0,'/')) # ?

""" 
when error occurs, you need to handle that
ErrorHandling
ExceptionHandling
"""
