import scrapingutils


def main():
    t1 = (1, 2)
    print(t1)
    triple = (1, 2, 3)
    print(triple)
    print(triple[2])
    print(triple.__hash__())

    a = ['a', 'a1']
    b = ['b', 'b1']
    c = (a + b)
    print(c)

    print(scrapingutils.util.joke())


if __name__ == '__main__':
    main()
