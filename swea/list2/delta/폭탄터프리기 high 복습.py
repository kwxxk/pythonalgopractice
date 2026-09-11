N, M = map(int, input().split())
K = int(input())
arr = [list(input()) for _ in range(N)]

def bomb(arr, y, x):
    dy = [0, 0, -1, 1]
    dx = [1, -1, 0, 0]

    for i in range(4): # 방향 4방향
        for k in range(1, K + 1): # 폭탄 터지는 파워
            ny = y + dy[i] * k
            nx = x + dx[i] * k
            if ny < 0 or nx < 0 or ny >= N or nx >= M: continue
            if arr[ny][nx] == '_': arr[ny][nx] = '%' # 폭탄 터뜨리기
            if arr[ny][nx] == '#': break # 벽만나면 break

    arr[y][x] = '%' # 현재위치 폭탄터지기


# 행순회
for y in range(N):
    for x in range(M):
        if arr[y][x] == '@': bomb(arr, y, x) # 폭탄 터져라

for row in arr:
    print(*row, sep='')