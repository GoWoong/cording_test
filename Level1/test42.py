def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] in "Kim":
            answer = "김서방은 {0}에 있다".format(i)
    return answer

seoul = ["Jane", "Kim"]
print(solution(seoul))