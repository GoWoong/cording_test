def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer

n = 123
print(solution(n))