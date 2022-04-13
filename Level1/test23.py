def solution(arr, divisor):
    answer = []
    for i in arr:
        if i % divisor == 0:
            answer.append(i)
    answer.sort()
    if len(answer) == 0:
        answer.append(-1)
    return answer

arr1 = [5, 9, 7, 10]
arr2 = [2, 36, 1, 3]
arr3 = [3,2,6]
divisor1 = 5
divisor2 = 1
divisor3 = 10
print(solution(arr1,divisor1))
print(solution(arr2,divisor2))
print(solution(arr3,divisor3))