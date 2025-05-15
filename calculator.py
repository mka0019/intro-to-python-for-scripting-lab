print("Let's Calulate x and y")

x = int(input("what is x: "))
# assign the first number to x
y = int(input("what is y: "))
# assign the second numer to y

operator = input("Enter the operator (+, -, *, /): ")
# user will chose what operator they want to utilize. 

if operator == "+":
    output = x + y 
elif operator == "-":
    output = x - y
elif operator == "*":
    output = x * y
elif operator == "/":
    output = x / y
else:
    print("Invalid")

# how this works > user chose the x and y through command line. Then the statements run. 
# if the user choose "*", it will run through the statments until it finds the corresponding one. 
# Then the artimetic will run. Otherwise, it will be invalid


# Using the output variable to store the result of the calculation. 
print("Output:", output)

# note to self: unlike bash, python still outputs decimals. It doesn't round like bash does.
# Dsicvery > its an updated to python3, to allow decimals to be printed. 


