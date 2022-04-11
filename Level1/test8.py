def solution(a, b):
    answer = 0
    for i in range(len(a)):
        answer += a[i] * b[i]
    return answer

caseA = [1,2,3,4]
caseA2 = [-1,0,1]
caseB = [-3,-1,0,2]
caseB2 = [1,0,-1]

print(solution(caseA, caseB))
print(solution(caseA2, caseB2))