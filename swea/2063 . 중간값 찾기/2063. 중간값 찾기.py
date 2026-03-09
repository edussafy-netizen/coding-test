import sys

sys.stdin = open("2063. 중간값 찾기.txt", "r")
n = int(input())        # n개의 점수
lists = sorted(list(map(int,input().split())))
print(lists)

print(lists[n//2])

# 중간값을 출력