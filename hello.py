import sys
import math
from m1 import *
import m1


def main():
    pharse = "Giraffe Academy"
    print(pharse.lower().islower())
    print(pharse.index("ffe"))
    print(pharse.replace("Giraffe", "Elephant"))
    print(pharse[0])
    print("hello world" + str(3))
    print(sys.argv)
    print(abs(-4))
    print(None)
    print(math.e)
    print(a)
    print(sys.modules)
    print(m1.__all__)
    print(m1.b)
    print(globals())
    print(locals())

    name = input("enter your name: ")
    print("your name is : " + name)

    age = input("enter your age: ")
    print("your age is : " + age)


if __name__ == '__main__':
    main()
