def solution(sizes):
    result = [0,0]
    for i in range(0,len(sizes)):
        if sizes[i][0] < sizes[i][1]:
            sizes[i] = [sizes[i][1],sizes[i][0]]
        if result[0] < sizes[i][0]:
            result[0] = sizes[i][0]
        if result[1] < sizes[i][1]:
            result[1] = sizes[i][1]
    answer = result[0] * result[1]
    return answer

sizes1 = [[60, 50], [30, 70], [60, 30], [80, 40]]
sizes2 = [[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]]
sizes3 = [[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]
print(solution(sizes1))
print(solution(sizes2))
print(solution(sizes3))