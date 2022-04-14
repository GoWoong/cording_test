def solution(s):
    answer = ''
    new_list = s.split(" ")
    for i in new_list:
        for j in range(0, len(i)):
            if j % 2 == 0:
                answer += i[j].upper()
            else:
                answer += i[j].lower()
        answer+= " "
    return answer[0:-1]

s = "try hello world"
print(solution(s))