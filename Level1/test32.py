def solution(phone_number):
    answer = len(phone_number)
    last = phone_number[-4:]
    return "*"*(answer-4) + last
    
phone_number1 = "01033334444"
print(solution(phone_number1))