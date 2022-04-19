def solution(arr1, arr2):
    x = len(arr2[0])
    y = len(arr1)
    answer = []
    for i in range(y):
        x_list = []
        for j in range(x):
            number = 0
            for k in range(len(arr1[0])):
                nf1 = arr1[i][k]
                nf2 = arr2[k][j]
                number += nf1 * nf2
            x_list.append(number)
        answer.append(x_list)
    return answer
arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]

print(solution(arr1,arr2))