def squares(x):
    return [x**2 for x in range(1, x+1)]


def dict_squares(x):
    return {x: x**2 for x in range(1, x+1)}


def main():
    print squares(3)
    print dict_squares(3)


if __name__ == '__main__':
    main()