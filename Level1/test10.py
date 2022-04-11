def solution(participant, completion):
    answer = []
    for i in participant:
        if not(i in completion):
            answer.append(i)
    if len(answer) == 0:
        for j in completion:
            if participant.count(j) > 1:
                answer.append(j)
    return answer.pop()

participate1 = ["leo", "kiki", "eden"]
participate2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
participate3 = ["mislav", "stanko", "mislav", "ana"]
completion1 = ["eden", "kiki"]
completion2 = ["josipa", "filipa", "marina", "nikola"]
completion3 = ["stanko", "ana", "mislav"]
print(solution(participate1,completion1))
print(solution(participate2, completion2))
print(solution(participate3, completion3))