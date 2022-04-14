def solution(arr):
    tmp = []
    answer = []
    result = []
    for i in range(0, len(arr)):
        if i == 0:
            result.append(arr[i])
        else:
            if arr[i-1] == arr[i]:
                result.append(arr[i])
            else:
                tmp.append(list(set(result)))
                result =[]
                result.append(arr[i])
    if len(result) != 0:
        tmp.append(list(set(result)))
    for j in tmp:
        answer.append(j[0])
    return answer

arr1 = [1,1,3,3,0,1,1]
print(solution(arr1))