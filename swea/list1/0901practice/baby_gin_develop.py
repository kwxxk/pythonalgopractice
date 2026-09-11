arr = list(map(int,input().split()))
used = [0] * 6
path = []

is_found_baby_gin = False

def is_baby_gin():
    cnt = 0
    # 앞의 3자리 확인
    a,b,c = path[0], path[1], path[2]
    if a == b == c: cnt+=1
    elif a ==(b-1) == (c-2): cnt+= 1
    #뒤의 3자리 확인
    a,b,c = path[3], path[4], path[5]
    if a == b == c: cnt +=1
    elif a == (b-1) == (c-2): cnt +=1

    return cnt ==2 #판별식 리턴으로 True or False

def KFC(lev):
    if lev == 6:
        if is_baby_gin(): is_found_baby_gin = True
        return

    for i in range(6):
        if used[i] == 1: continue
        used[i] = 1
        path.append(arr[i])
        KFC(lev+1)
        path.pop()
        used[i] = 0
KFC(0)

if is_found_baby_gin: print('Yes')
else: print('No')