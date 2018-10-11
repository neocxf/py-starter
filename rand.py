import os
import random


def main():
    print("main")

    isTall = False
    isMale = True
    if isTall:
        print("tall")
    elif isMale and not isTall:
        print("male and not tall")
    else:
        print("not tall")

    # random.seed(os.urandom(10))
    print(random.random())
    print(random.random())


if __name__ == '__main__':
    main()
