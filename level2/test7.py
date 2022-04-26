def numberOneSearch(binNum):
    oneCount = 0
    for i in range(2,len(binNum)):
        if binNum[i] == "1":
            oneCount += 1
    return oneCount

def solution(n):
    answer = 0
    binN = numberOneSearch(str(bin(n)))
    while answer != binN:
        n += 1
        answer = numberOneSearch(str(bin(n)))
    return n

n = 15
print(solution(n))