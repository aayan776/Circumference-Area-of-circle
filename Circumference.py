print("Choose option")
print("1. Circumference")
print("2. Area")
choice = input("Enter choice: ")
alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
if choice in alphabet_upper or choice in alphabet_lower:
    print("Input not a number")
else:
    int_choice = int(choice)
#choice 1
if int_choice == 1:
    r = input("Enter radius of circle: ")
    if r in alphabet_upper or r in alphabet_lower:
        print("Input not a number")
    else:
        int_r = int(r)
        result = 2 * 3.1416 * int_r
        print(result)
#choice 2
elif int_choice == 2:
    r = input("Enter radius of circle: ")
    if r in alphabet_upper or r in alphabet_lower:
        print("Input not a number")
    else:
        int_r = int(r)
        result = 3.1416 * int_r ** 2
        print(result)