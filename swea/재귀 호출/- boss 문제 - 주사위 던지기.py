def KFC(lev, start):
    if lev == n:
        print(*path)
        return
    for i in range(start,7):
        # if used[i] == 1: continue
        # used[i] = 1
        path.append(i)
        KFC(lev+1,i)
        path.pop()
        # used[i] = 0
n = int(input())
path = [] #stack 자료구조
# used = [0] * 7 #dat 자료구조
KFC(0,1)

# = 중복을 제외할경우