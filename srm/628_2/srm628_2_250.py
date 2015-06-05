class BishopMove:
    def howManyMoves(self, r1, c1, r2, c2):
        if r1 == r2 and c1 == c2:
            return 0
        if r1 > r2:
            k = r1 - r2
        else:
            k = r2 - r1
        if c1 > c2:
            num2 = c1 - c2;
        else:
            num2 = c2 - c1;
        if num2 == k:
            return 1
        elif (num2 + k) %2 == 0:
            return 2
        else:
            return -1
