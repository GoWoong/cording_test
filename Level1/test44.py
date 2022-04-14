def solution(x, n):
    answer = [0] * n
    for i in range(n):
        if i == 0:
            answer[i] = x
        else:
            answer[i] = answer[i-1] + x
    return answer

x = -4
n = 2
print(solution(x,n))