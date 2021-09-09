# Defining a list  
Participants = ["Dani", "Jane", "Chris", "Romeo", "Joe"]
position = 0

for name in Participants:
    if name == "Chris":
        print("About to break.")
        break
    print("About to increment.")
    position += 1

print(position)