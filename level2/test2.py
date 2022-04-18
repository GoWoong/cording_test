def solution(s):
    answer = []
    result = []
    result1 = []
    num = ""
    for i in range(len(s)-1):
        if s[i].isdigit() and s[i+1].isdigit():
            num += s[i]
        elif s[i].isdigit() and not s[i+1].isdigit():
            num += s[i]
            result1.append(num)
            num = ""
        if s[i] == "}":
            result.append(result1)
            result1 = []
    result.sort(key=lambda x:len(x))
    for i in range(len(result)):
        for j in range(len(result[i])):
            if int(result[i][j]) not in answer:
                answer.append(int(result[i][j]))
    return answer

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
print(solution(s))