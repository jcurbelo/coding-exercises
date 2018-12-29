# Meta problem ;)
sol = {}
oper = ['+', '-', '*', '/']


def find_sols(sel, current):
    if current < 3:
        for i in xrange(4):
            sel[current] = i
            find_sols(sel, current + 1)
    s = '4 %s 4' % ' 4 '.join([oper[i] for i in sel])
    k = eval(s)
    sol[k] = '%s = %s' % (s, k)


# Pre computed solutions
ans_dict = {0: '4 / 4 / 4 / 4 = 0', 1: '4 / 4 * 4 / 4 = 1', 2: '4 / 4 + 4 / 4 = 2', 4: '4 / 4 / 4 + 4 = 4', 7: '4 - 4 / 4 + 4 = 7', 8: '4 / 4 * 4 + 4 = 8', 9: '4 / 4 + 4 + 4 = 9', 256: '4 * 4 * 4 * 4 = 256', 15: '4 * 4 - 4 / 4 = 15', 16: '4 / 4 * 4 * 4 = 16', 17: '4 / 4 + 4 * 4 = 17',
            24: '4 * 4 + 4 + 4 = 24', -60: '4 - 4 * 4 * 4 = -60', 32: '4 * 4 + 4 * 4 = 32', 60: '4 * 4 * 4 - 4 = 60', 68: '4 * 4 * 4 + 4 = 68', -16: '4 - 4 * 4 - 4 = -16', -15: '4 / 4 - 4 * 4 = -15', -8: '4 - 4 * 4 + 4 = -8', -7: '4 / 4 - 4 - 4 = -7', -4: '4 / 4 / 4 - 4 = -4', -1: '4 - 4 / 4 - 4 = -1'}


def main():
    m = input()
    ans = []
    for _ in xrange(m):
        n = input()
        ans.append(ans_dict.get(n, 'no solution'))
    for a in ans:
        print a


if __name__ == '__main__':
    main()
