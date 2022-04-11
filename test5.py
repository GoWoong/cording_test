def solution(board, moves):
    answer = []
    for a in moves:
        for i in range(0,5):
            if board[i][a-1] != 0:
                print(board[i][a-1])
                board[i][a-1] = 0
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
solution(board, moves)