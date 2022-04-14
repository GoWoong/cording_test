def solution(nums):
    nums.sort()
    answer = 0
    count = {}
    n = len(nums)//2
    for i in range(0, len(nums)):
        count[nums[i]] = 0
    for i in range(0, len(nums)):
        count[nums[i]] += 1
    count = sorted(count.items(), key=lambda x:x ,reverse=True)
    if len(count) >= n:
        answer = n
    else:
        answer = len(count)
    return answer

nums = [3,3,3,2,2,2]
print(solution(nums))