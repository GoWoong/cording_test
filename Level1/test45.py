def solution(arr):
    temp = arr[0]
    answer = []
    for i in range(len(arr)):
        if temp > arr[i]:
            temp = arr[i]
    for j in arr:
        if j != temp:
            answer.append(j)
    if len(answer) == 0:
        answer.append(-1)
    return answer

arr = [10]
print(solution(arr))