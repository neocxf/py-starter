def main():
    a = [1, 2, 3]
    print(a)
    a.extend([4, 5, 6])
    print(a)
    a.append(7)
    print(a)
    print(a.pop())
    a.reverse()
    print(a)
    a.insert(-1, 8)
    print(a)
    a.sort()
    print(a)


if __name__ == '__main__':
    main()
