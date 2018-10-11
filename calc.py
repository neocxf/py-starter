def main():
    print("calculating...")
    num1 = eval(input("Enter a number: "))
    num2 = eval(input("Enter another number: "))
    num3 = num1 + num2

    num4 = input("Enter 3rd number: ")
    print(num3 + float(num4))
    sayHi('neo')
    print(cube(3))


def sayHi(user):
    print("hello world", user)


def cube(num):
    return num * num * num


if __name__ == '__main__':
    main()
