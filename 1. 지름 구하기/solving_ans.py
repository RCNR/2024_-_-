# 수뭉이는 직사각형을 그리고 그 안에 그릴 수 있는 원들 중 가장 큰 원을 그리려 한다.
# 그릴 수 있는 가장 큰 원의 반지름의 길이를 cm로 나타내어 보자

# 입력
# 첫째줄에 한 변의 길이 N과 다른 한 변의 길이 M이 주어진다
# 1 <= N, M <= 500

n, m = map(int, input().split())

s = min(n,m)    
print(s * 50)   
# print(int(s/2 * 100))