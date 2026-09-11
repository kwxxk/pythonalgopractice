arr = ['A', 'B', 'C', 'D', 'E']

path = []

def KFC(lev, start):
    if lev == 3:
        print(*path)
        return
    for i in range(start, 5):
        path.append(arr[i])
        KFC(lev+1, i+1)
        path.pop()

KFC(0,0)