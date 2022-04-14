def solution(strings, n):
    return sorted(sorted(strings), key= lambda x:x[n])

strings1 = ["sun", "bed", "car"]
strings2 = ["abce", "abcd", "cdx"]
n1 = 1
n2 = 2
print(solution(strings1,n1))
print(solution(strings2,n2))