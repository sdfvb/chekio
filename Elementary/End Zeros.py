def end_zeros(num: int) -> int:
    count_zeros = 0
    for letter in [x for x in str(num)][::-1]:
        if letter == '0':
            count_zeros += 1
        else:
            break

    return count_zeros

def end_zeros(number):
    n = str(number)
    return len(n) - len(n.strip('0'))

def end_zeros(number):
    import re
    return len(re.search('0*$', str(number)).group())

def end_zeros(number):
    number = str(number)
    if number[-1:] != '0':
        return 0
    return 1 + end_zeros(number[:-1])

def end_zeros(number):
    if not number:
       return 1
    if not number % 10:
       return 1 + end_zeros(number // 10)
    return 0

def end_zeros(number):
    result = not number
    while number and not number % 10:
        number /= 10
        result += 1
    return result

def end_zeros(number):
    en = enumerate(str(number)[::-1])
    return not number or next(i for i, x in en if x != '0')

def end_zeros(number):
    from itertools import takewhile
    number = str(number)[::-1]
    return len(list(takewhile(lambda x: x == '0', number)))


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(100100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
