def solution(N, stages):
    answer = []
    all_num = len(stages)
    num = {}
    for i in range(1, N+1):
        cnt = 0
        for step in stages:
            if step == i:
                cnt += 1
        if cnt == 0:
            num[i] = 0
        else:
            num[i] = (cnt/all_num)
        all_num = all_num - cnt
    answer = sorted(num, key=lambda x:num[x], reverse = True)
    return answer


N1 = 5
N2 = 4
stages1 = [2, 1, 2, 6, 2, 4, 3, 3]
stages2 = [4,4,4,4,4]
print(solution(N1,stages1))
print(solution(N2,stages2))
