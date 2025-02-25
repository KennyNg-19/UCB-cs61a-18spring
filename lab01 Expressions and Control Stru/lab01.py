"""Lab 1: Expressions and Control Structures"""

# Coding Practice

def repeated(f, n, x):
    """Returns the result of composing f n times on x.

    >>> def square(x):
    ...     return x * x
    ...
    >>> repeated(square, 2, 3)  # square(square(3)), or 3 ** 4
    81
    >>> repeated(square, 1, 4)  # square(4)
    16
    >>> repeated(square, 6, 2)  # big number
    18446744073709551616
    >>> def opposite(b):
    ...     return not b
    ...
    >>> repeated(opposite, 4, True)
    True
    >>> repeated(opposite, 5, True)
    False
    >>> repeated(opposite, 631, 1)
    False
    >>> repeated(opposite, 3, 0)
    True
    """
    "*** YOUR CODE HERE ***"
    # simple recursion
    if n == 1:
        return f(x)
    else:
        return f(repeated(f, n-1, x))

def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    """
    "*** YOUR CODE HERE ***"
    base, sum = 10, 0 # 十进制
    while n !=0 : # = 0 说明 已经过最后一位了
        n, sum = n // base, sum + n % base
    return sum

def double_eights(n):
    """Return true if n has two eights in a row.
    >>> double_eights(8)
    False
    >>> double_eights(88)
    True
    >>> double_eights(2882)
    True
    >>> double_eights(880088)
    True
    >>> double_eights(12345)
    False
    >>> double_eights(80808080)
    False
    """
    "*** YOUR CODE HERE ***"
    base = 10
    while n // base != 0: # when it comes the leftmost digit, stop
        # print(n // base, ' ', n % base)
        n, digit1 = n // base, n % base
        if digit1 == 8:
            # print(n // base, ' ', n % base)
            n, digit2 = n // base, n % base
            if digit1 ==  digit2:
                return True
        # digit1 != 8, continue
    return False # 更简便：return '88' in str(n)
    

        

