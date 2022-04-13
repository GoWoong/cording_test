def solution(n):
    base = ""
    answer = 0
    while n>0:
        n,mod = divmod(n,3)
        base += str(mod)
    answer = int(base,3)
    return answer

n = 45
print(solution(n))