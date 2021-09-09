# Defining a variable    
word = "Hello"

letters = []
# iterating over string "Hello"
for w in word:
    print(w)
    if w == "e":
        print("Beautiful letter.")

    letters.append(w)

print(letters)

# Looping over integers in a list.
numbers = [1, 2, 3, 4, 5, 6]

#for number in numbers:
    #print(number)

# range(start, stop, steps) function in loops.
for num in range(10):
    print(num)

# Example of range() function
Numbers = []

for num in range(1, 10, 2):
    Numbers.append(num)
    print(num)
print(Numbers)