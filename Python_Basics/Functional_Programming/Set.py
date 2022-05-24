
num_set = {1, 1, 2, 3, 4, 5}
print(type(num_set))
print(num_set)
word_set = set(["spam", "eggs", "sausage"])

print(3 in num_set)
print("spam" not in word_set)


first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}




print(first | second) #Union
print(first & second) #Intersection
print(first - second) #difference
print(second - first)
print(first ^ second) #symmetric_difference