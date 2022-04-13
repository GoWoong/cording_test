def solution(left, right):
    result = []
    answer = 0
    for i in range(left, right+1):
        result.append(0)
        for j in range(1,i+1):
            if(i % j == 0):
                result[len(result)-1] += 1
        if result[len(result)-1] % 2 == 0:
            answer += i
        else:
            answer -= i
    return answer

left1 = 13
left2 = 24
right1 = 17
right2 = 27
print(solution(left1,right1))
print(solution(left2,right2))