# 다리 만들기 2
from collections import deque
import sys
input = sys.stdin.readline
MAX = sys.maxsize
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
N, M = map(int, input().split())

land = []   # 땅인 부분
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))
    for j in range(M):
        if arr[i][j] == 1:
            land.append((i, j))


def find_land(visited, a, b, num):
    q = deque()
    q.append((a, b))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny] and arr[nx][ny] == 1:
                visited[nx][ny] = True
                arr[nx][ny] = num
                start.append((nx, ny, num))
                q.append((nx, ny))


def find_parent(x):
    if x != island[x]:
        island[x] = find_parent(island[x])
    return island[x]


def union_parent(x, y):
    a, b = find_parent(x), find_parent(y)
    if a > b:
        island[a] = b
    if a < b:
        island[b] = a

# 바다이면 temp에 다리의 길이를 넣어주고 dfs, 땅이고 길이가 2이상이면 bridge에 append
def make_straight(nx, ny, dx, dy, num, temp):
    global result
    nx += dx
    ny += dy
    if 0 <= nx < N and 0 <= ny < M:
        if arr[nx][ny] == 0:
            temp[nx][ny] = temp[nx - dx][ny - dy] + 1
            make_straight(nx, ny, dx, dy, num, temp)
        elif temp[nx-dx][ny-dy] >= 2:
            bridge.append((temp[nx-dx][ny-dy], num, arr[nx][ny]))
            return

# start의 값을 가지고 dfs(make_straight)로 다리를 이을 수 있는지 체크
def make_bridge():
    for x, y, num in start:
        temp = [[0] * M for _ in range(N)]
        for dx, dy in direction:
            make_straight(x, y, dx, dy, num, temp)

def check_all_connected():
    temp = 0
    for i in range(1, num_island+1):
        if i == 1:
            temp = find_parent(i)
        elif temp != find_parent(i):
            return False
    return True

start = []
visited = [[False] * M for _ in range(N)]
num_island = 1      # 구역의 개수
# 각 땅을 돌면서 bfs(find_land)로 연결된 땅에 구역 번호를 매겨준다.
for i, j in land:
    if not visited[i][j]:
        visited[i][j] = True
        arr[i][j] = num_island
        start.append((i, j, num_island))    # (x좌표, y좌표, 구역 번호)
        find_land(visited, i, j, num_island)
        num_island += 1
num_island -= 1

direction = [[0, -1], [-1, 0], [0, 1], [1, 0]]
# 구역의 부모리스트 자기 자신으로 설정
island = [i for i in range(num_island+1)]


bridge = []     # 연결할 수 있는 다리의 정보(다리의 길이, 시작구역 번호, 도착구역 번호)
make_bridge()
bridge.sort()   # 다리길이가 짧은 순서로 정렬

result = 0
for len, start, end in bridge:
    # 각 구역의 부모가 다르면
    if find_parent(start) != find_parent(end):
        result += len
        union_parent(start, end)

# 모든 구역의 부모가 같은지 확인
if check_all_connected():
    print(result)
else:
    print(-1)


"""
구현, BFS, DFS, Union-Find

1. 입력을 받으면서 1(땅)인 부분을 land에 append

2. 각 땅(land리스트)를 돌면서 BFS(find_land)로 연결된 땅에 구역 번호를 매겨준다, num_island : 구역의 개수

    - start에 각 땅의 좌표와 구역의 번호를 넣어준다 (x좌표, y좌표, 구역 번호)

3. island : 구역의 부모리스트 초기값은 자기자신으로 설정

4. make_bridge() : start의 값을 가지고 DFS(make_straight)로 다리를 이을 수 있는지 체크

    - make_straight() : 바다이면 temp에 다리의 길이를 넣어주고 dfs, 땅이고 길이가 2이상이면 bridge에 append

5. bridge : 연결할 수 있는 다리의 정보 (다리의 길이, 시작구역번호, 도착구역번호)

6. bridge의 다리길이가 짧은 순서로 정렬

7. Union-Find

    - island를 이용해서 각 구역의 부모가 다르면 result에 다리길이를 더해주고 Union

8. check_all_connected() : 모든 구역의 부모가 같은지 확인

    - 같으면 모두 연결됐다는 뜻이므로 print(result)

    - 다르면 print(-1)

"""