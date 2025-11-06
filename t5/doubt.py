# input string, split, each word - len

# Hi user how can i help you
# 2,4,3,3,1,4,3
def word_len(input):
    # ["Hi","user","how","can","i","help","you"]
    words = input.split(" ")

    lengths = tuple(len(word) for word in words)
    return lengths
        
        
print(word_len("Hi user how can i help you"))