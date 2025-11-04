# pair
# city - temp
# order => item - count
# phonebook -> name - number

# create {key: value}

phonebook = {
    "ramesh": "47857",
    "mahesh": "47857",
    "suresh": "47857",
    
    "ramesh": "898773",
    "suresh": "987898"
}

print(phonebook)

print(f"Ramesh's phone: {phonebook['ramesh']}")
print(f"Ramesh's phone: {phonebook.get('ramesh')}")
print(phonebook["ramesh"])
