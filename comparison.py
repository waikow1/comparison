import sys


def compare(arg1) -> bool:
    return eval(arg1)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        print(compare(sys.argv[1]))
    else:
        print('Вы не ввели аргументы')

