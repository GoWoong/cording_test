def solution(s):
    s = s.lower()
    count = [0,0]
    answer = True
    for i in s:
        if i in "PpYy":
            if i == 'p':
                count[0] +=1
            elif i == 'y':
                count[1] +=1
        else:
            answer = True
    if count[0] == count[1] and len(count) != 0:
        answer = True
    else:
        answer = False
    return answer

s1 = ""
print(solution(s1))