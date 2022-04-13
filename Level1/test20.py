def solution(price, money, count):
    answer = 0
    result = 0
    for i in range(1,count+1):
        result += price * i
    if money < result:
        answer = result - money
    return answer

price1 = 3
money1 = 20
count1 = 4
print(solution(price1,money1,count1))