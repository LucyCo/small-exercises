def squares(x):
    squares_list = []
    for num in range(1, x+1):
        squares_list.append(num*num)
    return squares_list


def dict_squares(x):
    dict_squares_list = {}
    for num in range(1, x+1):
        dict_squares_list[num] = num*num
    return dict_squares_list


def main():
    print squares(3)
    print dict_squares(3)


if __name__ == '__main__':
    main()