def main():
    for i in range(0,5):
        n = iterativePower(3.3, i)
        print("n", n)
    for i in range(0,5):
        n = recursivePower(3.3, i)
        print("n", n)

def iterativePower(base, exp):
    '''
    base: int or float
    exp: int >= 0

    return: int or float, base ^ exp
    '''
    power = 1
    for _ in range(exp):
        power *= base
    return power

def recursivePower(base, exp):
    '''
    base: int or float
    exp: int >= 0

    return: int or float, base ^ exp
    '''
    if exp == 0:
        return 1
    else:
        return base * recursivePower(base, exp-1)


if __name__ == "__main__":
    main()
