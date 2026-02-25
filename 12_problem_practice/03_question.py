# Write a program that takes a number from the user and prints "Even" if it is even, otherwise "Odd".

a=int(input("Enter a number :"))


if(a%2==0):  
    # every number leaves reminder 0 when divided by 2 is known as even number
    print("The number is Even.")

else:
    print("The number is Odd")