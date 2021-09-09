
#TestList = ["First Element", "Second Element", "Third Element"]
# Indeces in lists starts with 0 as shown below
#TestList = [0, 1, 2]

# Example of list. Elements in a list are separated by commas.
Scores = [60, 80, 75, 66.5, 92]
print(Scores)

# Accessing elements using their indexes
print(Scores[0])
print(Scores[1])
print(Scores[2])
print(Scores[3])
print(Scores[4])

# To access the last element in the list we can do it as follows:
print("This is the last element: ", Scores[-1])
print("This is the second last element: ", Scores[-2])

# Accessing the first and the second element 
print(Scores[0:2]) # This means element in index 0 upto but not including element with index 2 

# Printing the list from index 2 all the way to the last element
print(Scores[2:])

#Changing the values in the list  
print("Initial values: ", Scores) 

Scores[0] = 65
print("Changed values: ", Scores)

"""NB: The elements in the list can be of different data types and a list can also contain other lists as elements."""

Scores[2] = ["Hello", "World"]
print(Scores)
print(Scores[2][0])

# Deleting values in the list 

Scores[1:3] = []
print(Scores)

# append method adds an element to the end of the list
Scores.append(85)
print(Scores)