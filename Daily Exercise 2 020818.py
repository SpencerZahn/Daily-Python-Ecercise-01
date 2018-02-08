#Spencer Zahn - Python Daily Exercise 2 - 020818

# 2. Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. Clue input()
name = input("Enter your name: ")
age = int(input("Enter your age: ")) 
print (name + " you will be 100 in " + str(2018 - age + 100) + "." )
