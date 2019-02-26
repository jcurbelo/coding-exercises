# https://projecteuler.net/problem=5


def main():
    divisors = [5, 7, 9, 11, 13, 16, 17, 19]
    g, m = 5, 1

    for d in divisors:
        g = gcd(g, d)
        m *= d

    print(m/g)

# taken from fractions
def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a


if __name__ == '__main__':
    main()
