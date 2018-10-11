try:
    val = int(input("enter a number: "))
    print("you input", val)
except ValueError as err:
    print("invalid input: ", err)
