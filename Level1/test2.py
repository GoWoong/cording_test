def solution(new_id):
    answer = ''
    new_id = new_id.lower() #소문자로
    for c in new_id: 
        if c.isalpha() or c.isdigit() or c in "-_.": 
            answer += c
    while ".." in answer:
        answer = answer.replace("..",".")
    if answer[0] == ".":
        if len(answer) >= 2:
            answer = answer[1:]
        else:
            answer="."
    if answer[-1] == ".":
        answer = answer[:-1]
    if answer == "":
        answer = "a"
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == ".":
            answer = answer[:-1]
    while len(answer) < 3:
        answer += answer[-1]

    return answer



id = "...!@BaT#*..y.abcdefghijklm"
print(solution(id))