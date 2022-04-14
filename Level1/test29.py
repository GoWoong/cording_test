def solution(s):
    answer = True
    length = len(s)
    if length == 4 or length == 6:
        for j in s:
            if j.isdigit() != True:
                answer = False
                return answer
    else:
        answer = False
    return answer

s1 = "1234"
print(solution(s1))