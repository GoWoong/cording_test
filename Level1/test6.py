def solution(numbers):
    num = [1,2,3,4,5,6,7,8,9]
    answer = 0
    for i in num:
        if not i in numbers:
            answer += i
    return answer

case1 = [1,2,3,4,6,7,8,0]
case2 = [5,8,4,0,6,7,9]
print(solution(case1))
print(solution(case2))