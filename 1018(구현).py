n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())
count = []  # 바뀐 체스판의 개수를 담는 리스트(W로 시작할 경우, B로 시작할 경우)

# 전체 체스판의 시작점을 잡기위한 반복문
for a in range(n - 7):      # 8*8로 잘라야하므로, 행으로 i-7, 열로 j-7만큼 고정
    for b in range(m - 7):
        # 시작점 (0, 0)이 W일경우와 B일경우, 두 경우 밖에 없음
        first_w = 0     # W로 시작하는 경우
        first_b = 0     # B로 시작하는 경우
        for i in range(a, a + 8):       # 행과열의 시작점을 a,b를 기준으로 8칸씩 모두 체크
            for j in range(b, b + 8):
                # 현재 행 i + 현재 열 j: 짝수이면 시작점의 색과 같고, 홀수이면 다른색을 칠해야 한다.
                # 따라서 (i + j)가 짝수일경우, 시작이 W인 경우 board[i][j]가 W가 아니면, first_w += 1
                # 시작이 B인 경우 board[i][j]가 B가 아니면, first_b += 1
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':      # 시작이 W인 경우
                        first_w += 1
                    if board[i][j] != 'B':      # 시작이 B인 경우
                        first_b += 1
                else:       # 홀수인 경우 시작점의 색깔과 다르지 않은 경우 체크
                    if board[i][j] != 'B':      # 시작이 W인 경우
                        first_w += 1    
                    if board[i][j] != 'W':      # 시작이 B인 경우
                        first_b += 1
        count.append(min(first_w, first_b))

print(min(count))


""" 
ex) 4*4 체스판

0,0	0,1	0,2	0,3
1,0	1,1	1,2	1,3
2,0	2,1	2,2	2,3
3,0	3,1	3,2	3,3
체스판 색의 인덱스(i,j)

0(짝)	1(홀)	2(짝)	3(홀)
1(홀)	2(짝)	3(홀)	4(짝)
2(짝)	3(홀)	4(짝)	5(홀)
3(홀)	4(짝)	5(홀)	6(짝)
"""

# 브루트 포스 알고리즘