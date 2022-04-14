
def solution(n, m):
    answer = []
    for i in range(min(n,m), 0 , -1):
        if n % i ==0 and m%i ==0:
            answer.append(i)
            break
    for i in range(max(n,m),(n*m)+1):
        if i% n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer

n = 3
m = 12
print(solution(n,m))