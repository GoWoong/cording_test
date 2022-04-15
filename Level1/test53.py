def solution(participant, completion):
    answer = ""
    participant.sort()
    completion.sort()
    for i in range(0,len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            del participant[i]
    if len(answer) == 0:
        answer = participant[len(participant)-1]
    return answer

participant1 = ["mislav", "stanko", "mislav", "ana"]
completion1 = ["stanko", "ana", "mislav"]
print(solution(participant1,completion1))