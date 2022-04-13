def solution(array, commands):
    arr = []
    answer = []
    for i in commands:
        arr = array[i[0]-1:i[1]]
        arr.sort()
        answer.append(arr[i[2]-1])
    return answer

case1 = [1, 5, 2, 6, 3, 7, 4]
commands1 = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(case1, commands1))