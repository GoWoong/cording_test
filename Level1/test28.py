def solution(s):
    result = []
    a = ""
    for i in s:
        result.append(i)
    result = sorted(result, reverse=True)
    print(result)
    for j in result:
        a += j
    return a

s1 = "Zbcdefg"
print(solution(s1))