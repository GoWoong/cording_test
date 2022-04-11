def solution(board, moves):
    answer = 0
    result = []
    for a in moves:
        for i in range(0,len(board)):
            if board[i][a-1] != 0:
                result.append(board[i][a-1])
                board[i][a-1] = 0
                if len(result) > 1:
                    if result[len(result)-2] == result[len(result)-1]:
                        result.pop()
                        result.pop()
                        answer += 2
                break

    
    return answer



board = [
    [0,0,0,0,0],
    [0,0,1,0,3],
    [0,2,5,0,1],
    [4,2,4,4,2],
    [3,5,1,3,1]
]
moves = [1,5,3,5,1,2,1,4]
print(solution(board, moves))