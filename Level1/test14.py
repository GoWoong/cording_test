def solution(numbers):
    result = []
    answer = []
    for i in range(0, len(numbers)-1):
        for j in range(i+1,len(numbers)):
            result.append(numbers[i] + numbers[j])
    answer = list(set(result))
    answer.sort()
    return answer

numbers1 = [2,1,3,4,1]
numbers2 = [5,0,2,7]
print(solution(numbers1))
print(solution(numbers2))