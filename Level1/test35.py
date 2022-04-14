def solution(n):
    result = []
    answer = ""
    for i in str(n):
        result.append(i)
    result = sorted(result, reverse=True)
    for j in result:
        answer += j
    return int(answer)

n = 118372
print(solution(n))