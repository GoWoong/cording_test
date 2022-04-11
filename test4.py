def solution(numbers, hand):
    answer = ''
    dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
        4: [1, 0], 5: [1, 1], 6: [1, 2],
        7: [2, 0], 8: [2, 1], 9: [2, 2],
        '*':[3, 0], 0: [3, 1], '#': [3, 2]}
    left_hand = dic['*']
    right_hand = dic['#']

    for i in numbers:
        now = dic[i]
        if i in [1,4,7]:
            answer += "L"
            left_hand = now
        elif i in [3,6,9]:
            answer += "R"
            right_hand = now
        else:
            left_d = 0
            right_d = 0
            
            # 좌표 거리 계산해주기
            for a, b, c in zip(left_hand, right_hand, now):
                left_d += abs(a-c)
                right_d += abs(b-c)
            
            # 왼손이 더 가까운 경우
            if left_d < right_d:
                answer += 'L'
                left_hand = now
                
            # 오른손이 더 가까운 경우
            elif left_d > right_d:
                answer += 'R'
                right_hand = now
            
            # 두 거리가 같은 경우
            else:
                # 왼손잡이 경우
                if hand == 'left':
                    answer += 'L'
                    left_hand = now
                    
                # 오른손잡이 경우
                else:
                    answer += 'R'
                    right_hand = now
    return answer




case1 = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(case1, hand))