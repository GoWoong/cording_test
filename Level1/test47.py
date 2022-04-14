from math import sqrt
def solution(n):
    answer = []
    l = False
    for i in range(2,n+1):
        sq = int(sqrt(i))
        if sq == 1:
            answer.append(i)
        else:
            for j in range(2,sq+1):
                if i % j == 0:
                    l = False
                    break
                else:
                    l = True
            if l == True:
                answer.append(i)
                l = False
    return len(answer)

n = 10
print(solution(n))