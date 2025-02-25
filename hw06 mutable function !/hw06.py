passphrase = '*** PASSPHRASE HERE ***'

def survey(p):
    """
    You do not need to understand this code.
    >>> survey(passphrase)
    '3d2eea56786a3d9e503a4c07dd667867ef3d92bfccd68b2aa0900ead'
    """
    import hashlib
    return hashlib.sha224(p.encode('utf-8')).hexdigest()

class Fib():
    """A Fibonacci number.

    >>> start = Fib()
    >>> start
    0
    >>> start.next()
    1
    >>> start.next().next()
    1
    >>> start.next().next().next()
    2
    >>> start.next().next().next().next()
    3
    >>> start.next().next().next().next().next()
    5
    >>> start.next().next().next().next().next().next()
    8
    >>> start.next().next().next().next().next().next() # Ensure start isn't changed
    8
    """

    def __init__(self, value=0):
        self.value = value

    # 因为能连续call next(): 必须返回一个Fib() instance
    def next(self):
        "*** YOUR CODE HERE ***"

        # 赋值属性，不能先写！报错local variable 'next_fib' referenced before assignment
        # next_fib.previous = self.value 

        # base case
        if self.value == 0:
            next_fib = Fib(1)
        else:
            next_fib = Fib(self.previous + self.value)

        next_fib.previous = self.value # 难点，这为了下次，后赋值：(从 0 开始)，先保存value到next_fib的属性里！！！方便下次调用

        return next_fib # 必须返回一个Fib() instance

    # 保证初始call start, 也有返回值
    def __repr__(self): 
        return str(self.value)

class VendingMachine:
    """A vending machine that vends some product for some price.

    >>> v = VendingMachine('candy', 10)
    >>> v.vend()
    'Machine is out of stock.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'
    >>> v.restock(2)
    'Current candy stock: 2'
    >>> v.vend()
    'You must deposit $10 more.'
    >>> v.deposit(7)
    'Current balance: $7'
    >>> v.vend()
    'You must deposit $3 more.'
    >>> v.deposit(5)
    'Current balance: $12'
    >>> v.vend()
    'Here is your candy and $2 change.'
    >>> v.deposit(10)
    'Current balance: $10'
    >>> v.vend()
    'Here is your candy.'
    >>> v.deposit(15)
    'Machine is out of stock. Here is your $15.'

    >>> w = VendingMachine('soda', 2)
    >>> w.restock(3)
    'Current soda stock: 3'
    >>> w.restock(3)
    'Current soda stock: 6'
    >>> w.deposit(2)
    'Current balance: $2'
    >>> w.vend()
    'Here is your soda.'
    """
    "*** YOUR CODE HERE ***"
    def __init__(self, good, price):
        self.good = good
        self.price = price
        self.stock = 0
        self.balance = 0

    def vend(self):
        price = self.price
        if self.stock == 0:
            return 'Machine is out of stock.'
        elif self.balance < price:
            return 'You must deposit ${0} more.'.format(price - self.balance)
        else:
            # buy successful
            self.stock -= 1
            change = self.balance - price

            # renew
            self.balance = 0

            if change == 0:
                return 'Here is your {0}.'.format(self.good)
            else: # change > 0
                return 'Here is your {0} and ${1} change.'.format(self.good, change)

    def deposit(self, money):
        if self.stock == 0:
            # fail to deposit
            return 'Machine is out of stock. Here is your ${0}.'.format(money + self.balance)
        else:
            # deposit            
            self.balance += money
            return 'Current balance: ${0}'.format(self.balance)

    def restock(self, quant):
        self.stock += quant
        return 'Current {0} stock: {1}'.format(self.good, self.stock)