# Write a program that keeps asking the user to enter a password until they enter the correct one.

password = "ganu"

entered_pass=input("Enter a password")

while(entered_pass != password):
    entered_pass = input("wrong password try again:")

print("successfully you are logged in ..")