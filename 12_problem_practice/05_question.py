# Write a program using match case that simulates a simple calculator.

# Ask the user for two numbers and an operation (+, -, *, /).
# Perform the operation using match case.

a=int(input("Enter a first number"))

b=int(input("Enter a second number"))

operation=input("choose operation")

match operation:
    case "+":
        print("a + b = ", a+b )

    case "-":
        print("a - b = ", a-b )

    case "//":
        print("a // b = ", a//b )  
        # it gives only floor value