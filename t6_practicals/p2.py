# check if given number is prime
num = 15
isPrime = True 

for i in range(2, (num//2)+1):
    if (num % i == 0):
        print(f"{num} is divisible by {i}")
        isPrime = False 
        break
        
if(isPrime):
    print(f"{num} is prime")
else:
    print(f"{num} is not prime")
