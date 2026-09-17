value= float(input("Enter a number: "))

match value:
    
    case 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9:
        print("The number is a single digit.")

    case _:
        print("The number is not a single digit.")
