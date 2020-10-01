def squarer(number):
    """
    A squaring function that can be used by a process
    """
    result = number ** 2
    print('{} squared to {}'.format(number, result))
if __name__ == '__main__':
    numbers = [2, 3, 4, 5, 6]
    for number in numbers:
        squarer(number)

