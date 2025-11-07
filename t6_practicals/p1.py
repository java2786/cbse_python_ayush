# Sum of first N natural numbers
num = 5 # 15 -> AP
# num = 21 # 21*11 -> AP
sum = 0
for i in range(1,num+1):
    sum = sum + i
    # print(f"in loop for {i}: {bag}")
    
print(sum)


# second way

addition = (num*(num+1))//2
print(addition)