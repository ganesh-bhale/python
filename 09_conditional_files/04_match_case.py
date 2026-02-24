a= int(input("Enter a number between 1 and10 :"))

match a :
    case 1:
        print ("You won a car:")
    case 2:
        print(" You won $4 ")
    case 5:
        print (" lucky person ")
    case _:
        print(" Better luck next time ")