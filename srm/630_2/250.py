class DoubleLetter(object):
    def ableToSolve(self, S):
        flag = False
        if len(S) == 0:
            return 'Possible'
        for i in range(len(S) - 1):
            if S[i] == S[i+1]:
                S = S[: i] + S[i+2: len(S) + 1]
                flag = True
                break
        if flag == False:
            return 'Impossible'
        return self.ableToSolve(S)

if __name__ == '__main__':
    aa = DoubleLetter()
    print aa.ableToSolve('aabccb')
