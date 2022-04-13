def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1,arr2):
        tmp = str(bin(num1 | num2))[2:]
        if len(tmp) < n:
            tmp = '0'*(n-len(tmp)) + tmp
        tmp = tmp.replace('1','#')
        tmp = tmp.replace('0',' ')
        answer.append(tmp)
    return answer

n1 = 6
arr1_1 = [46, 33, 33 ,22, 31, 50]
arr2_2 = [27 ,56, 19, 14, 14, 10]
print(solution(n1,arr1_1,arr2_2))