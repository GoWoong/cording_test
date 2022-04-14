def solution(s, n):
    result = []
    answer = ''
    for i in s:
        result.append(ord(i))
    print(result)
    for j in result:
        if j+n > 90 and j <= 90:
            answer += chr(((j+n)-90)+64)
        elif j+n > 122:
            answer += chr(((j+n)-122)+96)
        else:
            if j == 32:
                answer += " "
            else:
                answer += chr(j+n)
    return answer

s = "a B z"
n = 4
print(solution(s,n))