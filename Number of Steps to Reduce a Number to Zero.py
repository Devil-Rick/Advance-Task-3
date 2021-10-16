"""
Given an integer num, return the number of steps to reduce it to zero.

In one step, if the current number is even, you have to divide it by 2, 
otherwise, you have to subtract 1 from it.
"""


def out(x, c):
    if x > 0:
        if x % 2 == 0:
            x = x//2
        else:
            x -= 1
        c = c + 1
        return out(x, c)
    else:
        return c


if __name__ == '__main__':
    n = int(input('Number = '))
    c = 0
    print(out(n, c))
