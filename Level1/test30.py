def solution(s):
    result = ""
    a = ""
    answer = 0
    for i in s:
        if i.isdigit() == True:
            result += i
        else:
            a += i
    answer = int(result)
    if a == "-":
        answer *= -1
            
    return answer

s1 = "+1234"
print(solution(s1))