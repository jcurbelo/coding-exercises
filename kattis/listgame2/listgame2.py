def distinct_factors_count(n):
    i = 2
    count = 0
    rem = []
    while i * i <= n:
        consec = 0
        while n % i == 0:
            consec += 1
            n /= i

        cur = 0
        while consec - cur > 0:
            count += 1
            cur += 1
            consec -= cur
            # print 'cur: %s consec: %s FAC: %s' % (cur, consec, str(i) * cur)

        if consec != 0:
            l = len(rem)
            for j in xrange(l):
                if rem[j]:
                    rem[j] -= 1
                    consec -= 1
                    count += 1
                if not consec:
                    break
            if consec:
                rem.append(consec)
        # print rem
        i += 1

    return count + 1 if n > 1 else count


def main():
    n = input()
    print distinct_factors_count(n)


if __name__ == '__main__':
    main()
