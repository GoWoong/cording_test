def returnBin(s, count, returnCount):
    s = s.count("1")
    print(s)
    returnCount += 1
    s1 = ""
    if s == 1:
        return returnCount, count
    else:
        s = str(bin(s))
        for i in s[2:]:
            if i == "1":
                s1 += str(i)
            else:
                count += 1
        return returnBin(s,count,returnCount)
def solution(s):
    answer = [0,0]
    s1 = ""
    count = 0
    returnCount = 0
    for i in s:
        if i == "1":
            s1 += str(i)
        else:
            count += 1
    answer[0], answer[1] = returnBin(s1,count,returnCount)
    return answer

s = "110010101001"
print(solution(s))