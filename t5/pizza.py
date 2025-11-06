def make_pizza(toppings="onion"):
    print("Pizza with toppings:",toppings)
    
make_pizza("") # ?
make_pizza("oninon") 
my_toppings = "oninon","tomato","corn","paneer"
make_pizza(my_toppings) # ?
make_pizza(("corn","onion")) # ?

my_toppings_list = ["onion","paneer","capsicum"]
make_pizza(my_toppings_list) # ?


make_pizza() # ?
