# Ask the user to enter a day number (1–7) and print the corresponding day of the week using match case.

a=int(input("Enter a day "))

match a:
    case 1:
        print("sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Satuarday")

    case _:
        print(" Today is holliday")
