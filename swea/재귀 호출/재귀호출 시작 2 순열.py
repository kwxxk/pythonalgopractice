def KFC(lev):
    if lev == n: # level:n
        print(*path)
        return

    for i in range(1, 7): # branch:6
        if used[i] == 1: continue
        used[i] = 1
        path.append(i)
        KFC(lev + 1)
        path.pop()
        used[i] = 0

n = int(input()) # level
path = []
used = [0] * 7 # 1부터 6까지
KFC(0)