def solution(n):
    for i in range(1,n):
        if n%i==1:
            return i
n1 = 10
print(solution(n1))