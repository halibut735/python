chars = 'abcdefghijklmnopqrstuvwxyz+*/?'
charNum = [0 for i in range(30)]
opt = [[0 for i in range(30)] for j in range(30)]
pos = [[-1 for i in range(30)] for j in range(30)]

def cost(h, k):
    sum = 0
    for i in range(h, k):
        sum += charNum[i] * (i - h + 1)
    return sum

def dp(i, j):
    if opt[i][j] != -1:
        return opt[i][j]
    if i == j:
        for each in range(i):
            opt[i][i] = charNum[i]
    else:
        opt[i][j] = -1
        for k in range(i, j):
            q = dp(i-1, k-1) + cost(h, k)
            if q < opt[i][j]:
                opt[i][j] = q
                pos[i][j] = k
    return opt[i][j]

def ans():
    postion = pos[12][29]
    ret += chars[postion]
    while len(ret) < 11:
        postion = pos[12][postion]
        ret += chars[postion]
    return ret[::-1]
def main():
    cases = int(raw_input())
    for i in range(cases):
        count = int(raw_input())
        for j in range(count):
            str = raw_input()
            for each in str:
                if each == '+':
                    charNum[-4] += 1
                elif each == '*':
                    charNum[-3] += 1
                elif each == '/':
                    charNum[-2] += 1
                elif each == '?':
                    charNum[-1] += 1
                else:
                    charNum[each - 'a'] += 1
    dp(12, 30)
    print ans()
