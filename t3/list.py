# Ramesh -> scores
scores = [72, 82, 46, 98, 76, 58]

print(f"First: {scores[0]}")
print(f"Last: {scores[-1]}")
print(f"Last: {scores[len(scores)-1]}")

print(f"Scores: {scores}")
scores[2] = 67
print(f"Scores: {scores}")


# sum, max, min, avg
# sum = 0
# max = scores[0]
# min = scores[0]
# for i in range(len(scores)):
#     sum = sum + scores[i]
#     # find if current score is max
#     if(max<scores[i]):
#         max = scores[i]
#     if(min>scores[i]):
#         min = scores[i]
    
# print(f"Total score: {sum}")
# print(f"Max score: {max}")
# print(f"Min score: {min}")
# print(f"Average score: {sum/len(scores)}")

print(max(scores))