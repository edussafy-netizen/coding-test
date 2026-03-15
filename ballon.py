
import sys
sys.stdin = open("ballon.txt","r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    m, n = list(map(int,input().split())) # m세로 n가로
    listss = []
    for lists in range(m):
        listss.append(list(map(int,input().split())))









# 델타탐색 할수있는 상하좌우 만들기
