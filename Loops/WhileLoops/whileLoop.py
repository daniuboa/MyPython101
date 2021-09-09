"""
while loop syntax
.........................
while(condition):
    Action 
    Action2
    Action3
..........................
"""
# addding values from 1 to 10                  
counter = 1
sum = 0
while (counter <= 10):
    print(counter)
    sum = sum + counter
    counter = counter + 1

print("Sum = ", sum)

print("................................................")

Letters = ["a", "b", "c", "d", "e"]
index = 0

while index < len(Letters):
    print(index)
    print(Letters[index])
    index += 1
