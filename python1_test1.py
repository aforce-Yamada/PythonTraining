def sum(x,y):
    return x + y


def difference(x,y):
    return x - y


def product(x,y):
    return x * y


def quotient(x,y):
    return x // y


def surplus(x,y):
    return x % y

x = 11
y = 3

sum = sum(x,y)
print("11 + 3 = " + str(sum))

difference = difference(x,y)
print("11 - 3 = " + str(difference))

product = product(x,y)
print("11 × 3 = " + str(product))

quotient = quotient(x,y)
surplus = surplus(x,y)
print("11 ÷ 3 = " + str(quotient) + " 余り " + str(surplus))