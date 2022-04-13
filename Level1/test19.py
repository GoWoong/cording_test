from math import sqrt, pow
def solution(n):
    sq = 0
    first, second = divmod(n,n-1)
    sq = int(sqrt(n-1))
    
    if second == 1:
        if int(pow(sq,2)) == first:
            answer = sq
            print(sq)
        else:
            answer = n-1
    return answer

n1 = 10
print(solution(n1))