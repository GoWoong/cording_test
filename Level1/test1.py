def solution(lottos, win_nums):
    answer = [0,0]
    result = [6,6,5,4,3,2,1]
    zeroCount = 0
    match = 0
    for i in lottos:
        if i == 0:
            zeroCount += 1
        if i in win_nums:
            match += 1
    
    else:
        answer[0] = result[zeroCount+ match]
        answer[1] = result[match]

    return answer


list1 = [45, 4, 35, 20, 3, 9]
list2 = [20, 9, 3, 45, 4, 35]
print(solution(list1, list2))