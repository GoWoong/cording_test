from math import sqrt
def solution(n):
    answer = 0
    num = int(sqrt(n))
    if num**2 == n:
        answer = (num+1)**2
    else:
        answer = -1
    return answer

n = 81
print(solution(n))