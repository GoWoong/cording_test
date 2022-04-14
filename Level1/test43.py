def solution(n):
    answer = 0
    for i in range(0, n):
        if n % (i+1) == 0:
            answer += i+1
    return answer

n = 12
print(solution(n))