from operator import add, sub

def a_plus_abs_b(a, b):
    """Return a+abs(b), but without calling abs.

    >>> a_plus_abs_b(2, 3)
    5
    >>> a_plus_abs_b(2, -3)
    5
    """
    if b < 0:
        f = sub
    else:
        f = add
    return f(a, b)

def two_of_three(a, b, c):
    """Return x*x + y*y, where x and y are the two largest members of the
    positive numbers a, b, and c.

    >>> two_of_three(1, 2, 3)
    13
    >>> two_of_three(5, 3, 1)
    34
    >>> two_of_three(10, 2, 8)
    164
    >>> two_of_three(5, 5, 5)
    50
    """
    return max(a*a + b*b, a*a + c*c, b*b + c*c)

def largest_factor(n):
    """Return the largest factor of n that is smaller than n.

    >>> largest_factor(15) # factors are 1, 3, 5
    5
    >>> largest_factor(80) # factors are 1, 2, 4, 5, 8, 10, 16, 20, 40
    40
    >>> largest_factor(13) # factor is 1 since 13 is prime
    1
    """
    "*** YOUR CODE HERE ***"
    i = n - 1
    while i < n:
        if n % i == 0:
            return i
        i -= 1


# ============================Control flow and SICP=================================
# 正规if
def with_if_statement():
    """
    >>> with_if_statement()
    1
    """
    if c():
        return t()
    else:
        return f()

# 不完全等于if的函数
def if_function(condition, true_result, false_result):
    """Return true_result if condition is a true value, and
    false_result otherwise.

    >>> if_function(True, 2, 3)
    2
    >>> if_function(False, 2, 3)
    3
    >>> if_function(3==2, 3+2, 3-2)
    1
    >>> if_function(3>2, 3+2, 3-2)
    5
    """
    if condition:
        return type(true_result)
    else:
        return false_result

def with_if_function():
    return if_function(c(), t(), f())

# The function with_if_function uses a CALL expression, 
# which guarantees that all of its operand subexpressions will be evaluated 
# before if_function is applied to the resulting arguments. 
# Therefore, even if c returns False, the function t will be called. 
# 重点是，在执行return if_function(c(), t(), f())时，
# 解释器会首先evaluate3个函数c(), t(), f()的expression，并将函数返回值作为参数传入if_function，
# c()的返回值不会影响t()和f()的执行。
#  
# By contrast, with_if_statement will never call t if c returns False.



def c():
    "*** YOUR CODE HERE ***"
    return True

def t():
    "*** YOUR CODE HERE ***"
    print(1)

def f():
    "*** YOUR CODE HERE ***"
    print(0)
#=============================================================================== 

def hailstone(n):
    """Print the hailstone sequence starting at n and return its
    length.

    >>> a = hailstone(10) 
    10
    5
    16
    8
    4
    2
    1
    >>> a
    7
    """
    "*** YOUR CODE HERE ***"
    count = 1
    while n != 1:
        print(n)
        if n % 2 == 0:
            n = n // 2 # py3 use // to do flooring division
        else:
            n = n * 3 + 1
        count += 1

    print(n)
    return count
