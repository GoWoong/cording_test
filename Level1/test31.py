def solution(arr1, arr2):
    answer = []
    result = []
    for i, j in zip(arr1,arr2):
        for i_2, j_2 in zip(i,j):
            result.append(i_2 + j_2)
        answer.append(result)
        result = []
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1,arr2))