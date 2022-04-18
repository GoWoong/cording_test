def solution(arr):
    arrmax = 1
    allpass = 0
    answer = 0
    for maxnum in arr:
        arrmax *= maxnum
    for i in range(max(arr), arrmax+1):
        for j in range(0,len(arr)):
            if i % arr[j] == 0:
                allpass += 1
        if allpass == len(arr):
            answer = i
            break
        allpass = 0
    return answer

arr = [1,2,3]
print(solution(arr))