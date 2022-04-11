def solution(board, moves):
    for a in range(0, len(moves)):
        for i in range(0,5):
            if board[i][moves[0]] != 0:
                print(board[i][moves[a-1]])
                break

    
    answer = []
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