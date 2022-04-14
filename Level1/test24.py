def solution(dartResult):
    answer = 0
    result = []
    num = ""
    area = {"S":1,"D":2,"T":3}
    for i in range(0,len(dartResult)):
        if dartResult[i].isdigit():
            num += dartResult[i]
        if dartResult[i].isalpha():
            num = int(num)**int(area[dartResult[i]])
            result.append(num)
            num = ""
        if dartResult[i].isalnum() == False:
            if dartResult[i] == "*" and len(result) != 1:
                result[len(result)-1] *= 2
                result[len(result)-2] *= 2
            elif dartResult[i] == "*" and len(result) == 1:
                result[len(result)-1] *= 2
        if dartResult[i].isalnum() == False:
            if dartResult[i] == "#":
                result[len(result)-1] *= -1
    for re in result:
        answer += re
    return answer


dartResult1 = "1T2D3D#"
print(solution(dartResult1))