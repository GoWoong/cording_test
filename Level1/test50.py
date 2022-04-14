def solution(x):
    result = []
    answer = True
    sum = 0
    for i in str(x):
        result.append(int(i))
    for j in result:
        sum += j
    if x % sum == 0:
        answer = True
    else:
        answer = False
    return answer

arr = 13
print(solution(arr))