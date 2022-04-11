def solution(s):
    i=0
    now = ""
    answer = ""
    numlist = {
        "zero":"0",
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    }
    while i < len(s):
        if s[i].isdigit():
            answer += s[i]
        else:
            now += s[i]
            if now in numlist:
                answer += numlist[now]
                now = ""
        i += 1
    
    return int(answer)



randnum = "123"
print(solution(randnum))
