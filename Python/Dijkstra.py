from queue import PriorityQueue  # 우선순위 큐
from math import inf  # INF 무한

pq = PriorityQueue()
PM = [[0, 1], [0, -1], [1, 0], [-1, 0]]

XE = 0
YE = 0


def BFS():
    while not pq.empty():
        Q = pq.get()
        cost_sum = Q[0]
        num = Q[1]
        x = Q[3]
        y = Q[2]
        for n in range(4):
            X = x + PM[n][1]
            Y = y + PM[n][0]
            if X < 0 or M <= X or Y < 0 or N <= Y or wall[Y][X] or visit[Y][X][0] == True:
                continue
            if visit[Y][X][0] == False and visit[Y][X][2] > cost_sum + cost[Y][X]:
                visit[Y][X][2] = cost_sum + cost[Y][X]
                visit[Y][X][1] = num + 1
                visit[Y][X][0] = True
                pq.put((visit[Y][X][2], visit[Y][X][1], Y, X))
    print()
    for n in range(N):
        for m in range(M):
            if visit[n][m][0] == True:
                print(visit[n][m][1], end=" ")
            else:
                print("X", end=" ")
        print()

    print()
    for n in range(N):
        for m in range(M):
            if visit[n][m][0] == True:
                print(visit[n][m][2], end=" ")
            else:
                print("X", end=" ")
        print()


N, M = map(int, input().split())

visit = [[[False, inf, inf] for _ in range(M)] for _ in range(N)]   # 방문 체크       # False : 방문 X    # True : 방문 O
wall = [[False for _ in range(M)] for _ in range(N)]                # 벽 위치 체크    # False : 벽 존재 X  # True : 벽 존재 O
cost = [[0 for _ in range(M)] for _ in range(N)]                    # 각 지형 위치 별 비용 지정

for n in range(N):
    s = input().split()
    for m in range(M):
        if s[m] == "#":
            wall[n][m] = True
        elif s[m] == "+":
            cost[n][m] = -2
        elif s[m] == "-":
            cost[n][m] = 0
        elif s[m] == "~":
            cost[n][m] = 1
        elif s[m] == "^":
            cost[n][m] = 3
        elif s[m] == "S":
            visit[n][m][0] = True  # 방문 체크
            visit[n][m][1] = 1     # 방문 순서
            visit[n][m][2] = 0     # 누적 비용
            pq.put((0, 1, n, m))
        elif s[m] == "F":
            XE = m
            YE = n

BFS()
