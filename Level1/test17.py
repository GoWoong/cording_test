def solution(a, b):
    mounth = {1:31,2:29,3:31,4:30,5:31,6:30,7:31,8:31,9:30,10:31,11:30,12:31}
    total_day = 0
    first_Day = 0
    answer = ''
    day = ["FRI","SAT",'SUN',"MON","TUE","WED","THU"]
    for i in range(0,a):
        if i != 0:
            total_day += mounth[i]
    total_day += b-1
    f,c = divmod(total_day, 7)
    if first_Day + c > 6:
        answer += day[(first_Day+c)-5]
    else:
        answer += day[first_Day+c]
    return answer

print(solution(5,24))