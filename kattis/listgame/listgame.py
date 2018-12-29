def prime_factors_count(n):
    i = 2
    count = 0
    while i * i <= n:
        while n % i == 0:
            count += 1
            n /= i
        i += 1
    return count + 1 if n > 1 else count


def main():
    n = input()
    print prime_factors_count(n)


if __name__ == '__main__':
    main()
