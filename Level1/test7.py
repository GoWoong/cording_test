def solution(absolutes, signs):
    answer = 0
    for i in range(0, len(absolutes)):
        if signs[i] == True:
            answer += absolutes[i]
        if signs[i] == False:
            answer -= absolutes[i]
    return answer

case1 = [4,7,12]
case2 = [1,2,3]
signs1 = [True,False,True]
signs2 = [False,False,True]

print(solution(case1, signs1))
print(solution(case2, signs2))